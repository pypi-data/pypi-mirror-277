import malmo.MalmoPython as MalmoPython
from typing import Union
from malmoext.scenario_builder import AgentBuilder
from malmoext.types import Mob, Item, Inventory, Entity, Vector, Rotation
from malmoext.utils import Utils
import math

class Agent:
    '''An Agent wraps a client connection to a Malmo Minecraft instance, and represents a
    player agent in a scenario. The various methods of this class represent the different
    agent actions that can be performed.
    
    Instances of this class should not be constructed directly. Instead, they will be
    automatically constructed when a scenario is ran.'''

    ATTACK_KEEP_DISTANCE = 3
    '''Distance tolerance (in number of blocks) when attacking an entity'''

    GIVE_KEEP_DISTANCE = 4
    '''Distance tolerance (in number of blocks) when giving an item to an entity'''

    TRADE_IGNORE_DISTANCE = 3
    '''Distance (in number of blocks) from recent trade positions that items will be ignored'''

    TRADE_IGNORE_TIME = 70
    '''Number of clock ticks an agent will ignore recently traded items for'''


    def __init__(self, builder: AgentBuilder):
        '''Constructor'''
        self.__name = builder.get_name()
        self.__observable_distances = builder.get_observable_distances()
        self.__host = MalmoPython.AgentHost()
        self.__recent_trade_positions = {}        # type: dict[Vector, int]
        self.state = None                         # type: AgentState


    def get_name(self):
        '''Returns the name of this agent'''
        return self.__name
    

    def get_observable_distances(self):
        '''Returns the observable distance of this agent in the x, y, and z directions'''
        return self.__observable_distances


    def get_host(self):
        '''Returns a reference to the Malmo AgentHost connection to the Minecraft server'''
        return self.__host


    def is_mission_active(self) -> bool:
        '''Returns true if this agent's mission is still active. Returns false otherwise.'''
        return self.__host.peekWorldState().is_mission_running


    def do_nothing(self):
        '''Halts all movement and ongoing actions for this agent.'''
        self.__host.sendCommand('turn 0')
        self.__host.sendCommand('pitch 0')
        self.__host.sendCommand('strafe 0')
        self.__host.sendCommand('move 0')


    def equip(self, item_type: Item) -> bool:
        '''Equips an item from this agent's inventory. If the item does not already exist in the agent's hotbar,
        it will be swapped with an item from the hotbar. Returns true if successful. Returns false otherwise.'''
        
        inventory_item = self.state.get_inventory_item(item_type)
        if inventory_item is None:
            return False
        
        # Malmo keys are 1-indexed
        item_index = inventory_item.slot.value
        target_index = item_index

        # If item is not already in the hotbar...
        if not Inventory.HotBar.contains(item_index):
            
            # Try to move item into an empty hotbar slot. Otherwise, swap item with what is currently equipped
            target_slot = self.state.get_available_hotbar_slot()
            if target_slot is None:
                target_slot = self.state.get_currently_equipped_slot()
            target_index = target_slot.value
            self.__host.sendCommand('swapInventoryItems {} {}'.format(target_index, item_index))

        # Equip (Malmo keys are 1-indexed)
        self.__host.sendCommand('hotbar.{} 1'.format(target_index + 1))
        self.__host.sendCommand('hotbar.{} 0'.format(target_index + 1))
        return True


    def look_at(self, entity: Union[str, Mob, Item, Entity]) -> bool:
        '''Initiates camera movement of this agent's POV to face another entity, specified either by name or by reference.
        If multiple entities exist with the given name, the closest one will be targeted.
        
        Because this transition does not occur instantaneously, this method is intended to be called repeatedly as part
        of the simulation loop.
        
        Returns true if the agent is currently facing the entity (and thus no further camera change will occur). Returns
        false if the agent is not yet facing the entity, or an entity with the given name does not exist.'''

        target = self.__resolve_entity(entity)
        if target is None:
            return False
        
        turn_rates = self.__compute_turn_rates(target.position)

        # Modify yaw rate
        if Utils.equal_tol(turn_rates.yaw, 0, 0.001):
            self.__host.sendCommand('turn 0')
        else:
            self.__host.sendCommand('turn {}'.format(turn_rates.yaw))
    
        # Modify pitch rate
        if Utils.equal_tol(turn_rates.pitch, 0, 0.001):
            self.__host.sendCommand('pitch 0')
        else:
            self.__host.sendCommand('pitch {}'.format(turn_rates.pitch))

        # Use a slightly higher tolerance for reporting success
        return Utils.equal_tol(turn_rates.yaw, 0, 0.05) and Utils.equal_tol(turn_rates.pitch, 0, 0.05)
    

    def move_to(self, entity: Union[str, Mob, Item, Entity], keep_distance = 1) -> bool:
        '''Initiates movement of this agent to another entity, specified either by name or by reference. If multiple
        entities exist with the given name, the closest one will be targeted. Optionally specify a number of blocks the
        agent should keep away from the target (defaults to 1, since two entities cannot occupy the same block). This
        can be useful in cases where the agent plans to attack or give an item to the target.
        
        Because this transition does not occur instantaneously, this method is inteded to be called repeatedly as part
        of the simulation loop.
        
        Returns true if the agent is currently at the entity (with a tolerance of 2 blocks, given that two entities cannot
        always occupy the same block). Returns false otherwise.'''

        target = self.__resolve_entity(entity)
        if target is None:
            return False
        
        move_rates = self.__compute_move_rates(target.position, keep_distance)
        is_at = True

        # Modify left/right movement rate
        if Utils.equal_tol(move_rates.x, 0, 0.001):
            self.__host.sendCommand('strafe 0')
        else:
            self.__host.sendCommand('strafe {}'.format(move_rates.x))
            is_at = False

        # Modify forward/backward movement rate
        if Utils.equal_tol(move_rates.z, 0, 0.001):
            self.__host.sendCommand('move 0')
        else:
            self.__host.sendCommand('move {}'.format(move_rates.z))
            is_at = False

        return is_at
    

    def attack(self, entity: Union[str, Mob, Entity]) -> bool:
        '''Initiates an attack against another entity, specified either by name or by reference. If multiple entities
        exist with the given name, the closest one will be targeted. The attack will be performed using the currently-equipped
        item.
        
        If the agent is not currently looking or located at the target, this method will default to performing those actions
        first.
        
        Returns true if the attack was performed successfully. Returns false otherwise.'''

        target = self.__resolve_entity(entity)
        if target is None:
            return False
        
        # Ensure we are first looking and located at the entity
        looking_at = self.look_at(entity)
        located_at = self.move_to(entity, Agent.ATTACK_KEEP_DISTANCE)
        if not looking_at or not located_at:
            return False
        
        # Perform the attack
        self.__host.sendCommand('attack 1')
        self.__host.sendCommand('attack 0')
        return True
        

    def give_item(self, item: Item, entity: Union[str, Mob, Entity]) -> bool:
        '''Gives an item to another entity, specified either by name or by reference. If multiple entities exist with the given
        name, the closest one will be targeted.
        
        If the agent is not currently looking or located at the target, or does not have the item equipped, this method will
        default to performing those actions first.
        
        Returns true if the item(s) were exchanged successfully. Returns false otherwise.'''

        target = self.__resolve_entity(entity)
        if target is None:
            return False
        
        # Ensure we are first looking and located at the entity
        looking_at = self.look_at(entity)
        located_at = self.move_to(entity, Agent.GIVE_KEEP_DISTANCE)
        if not looking_at or not located_at:
            return False

        # Ensure the item is equipped        
        if not self.equip(item):
            return False
        
        self.__recent_trade_positions[target.position] = Agent.TRADE_IGNORE_TIME
        self.__host.sendCommand('discardCurrentItem')
        return True


    def _sync(self):
        '''Syncs the data cached on this agent with the latest available data from the Malmo Minecraft server. Returns
        true if new data has been loaded. Returns false otherwise.
        
        This method is not intended to be called directly by users of this library.'''

        # Decrement timers for recent trade positions
        self.__recent_trade_positions = {key:(val - 1) for key, val in
                self.__recent_trade_positions.items() if val > 1}

        # Update agent state
        if self.__host.peekWorldState().number_of_observations_since_last_state > 0:
            self.state = AgentState(self)
            return True

        return False
    

    def _get_recent_trade_positions(self):
        '''Returns the set of positions where this agent has recently traded items.
        
        This method is not intended to be called directly by users of this library.'''

        return set(self.__recent_trade_positions.keys())


    def __resolve_entity(self, entity: Union[str, Mob, Item, Entity]):
        '''If given the name of an entity, this method will return the closest entity to the agent containing that name (or None if
        no entity with that name could be located). If given an entity reference, this method will return that reference as-is.'''
        
        target = entity
        if isinstance(target, Entity):
            return target
        
        return self.state.get_nearby_entity(target)

    
    def __compute_turn_rates(self, target_position: Vector):
        '''Calculates proposed yaw and pitch angle rotations for the camera, in order to face the given position.'''

        # Compute signed angle differences
        angle_diffs = self.__compute_angle_diffs(target_position)
        yaw_turn_direction = 1 if angle_diffs.yaw >= 0 else -1
        pitch_turn_direction = 1 if angle_diffs.pitch >= 0 else -1

        # Compute rotation speeds
        yaw_rate = min(Utils.linear_map(abs(angle_diffs.yaw), 0, 180, 0, 2.25), 1) * yaw_turn_direction
        pitch_rate = min(Utils.linear_map(abs(angle_diffs.pitch), 0, 180, 0, 2.25), 1) * pitch_turn_direction

        return Rotation(yaw_rate, pitch_rate)


    def __compute_move_rates(self, target_position: Vector, tolerance = 2):
        '''Calculates proposed strafing (left/right) and movement (forward/backward) speeds in order to move
        to the given position. Optionally specify a tolerance in number of blocks (defaults to 2, since two entities
        cannot occupy the same block).
        
        Returns the result as a vector, where the x component represents the strafing rate, and the z component
        represents the movement rate.'''

        # If we are already at the target position, return the zero vector for the rates
        target_distance = Utils.distance(self.state.get_position(), target_position)
        if Utils.equal_tol(target_distance, 0, tolerance):
            return Vector(0, 0, 0)

        # Compute signed angle differences and use that to determine side-to-side and forward-backward movement
        angle_diffs = self.__compute_angle_diffs(target_position)
        strafe_rate = math.sin(math.radians(angle_diffs.yaw))
        move_rate = math.cos(math.radians(angle_diffs.yaw))
        return Vector(strafe_rate, 0, move_rate)


    def __compute_angle_diffs(self, target_position: Vector):
        '''Computes the signed angle differences between the agent's line-of-sight and a target position (in degrees).
        
        Returns the resulting two angles, where yaw will be in the range (-180, 180), and pitch will be in the range (-90, 90).'''
       
        # Get vector from agent to target
        agent_position = self.state.get_position()
        v = Utils.vector_to(agent_position, target_position)
        v = Utils.normalize(v)
        if Utils.is_zero_vector(v, 1.0e-6):
            return Rotation(0, 0)

        # Target pitch (-90, 90)
        target_pitch = math.atan(-v.y / math.sqrt(v.z * v.z + v.x * v.x))
        target_pitch = math.degrees(target_pitch)

        # Target yaw (0, 360)
        target_yaw = math.atan2(-v.x, v.z)
        target_yaw = math.degrees((target_yaw + Utils.TWO_PI) % Utils.TWO_PI)

        # Get agent and target angles
        agent_pov = self.state.get_pov()

        # Pitch turning direction
        pitch_diff = abs(target_pitch - agent_pov.pitch)
        pitch_diff *= (1 if target_pitch > agent_pov.pitch else -1)

        # Yaw turning direction. We want to rotate in whatever direction results in the least amount of turning.
        yaw_diff = abs(agent_pov.yaw - target_yaw)
        yaw_turn_direction = 1 if target_yaw > agent_pov.yaw else -1
        yaw_diff_2 = 360 - yaw_diff
        if yaw_diff_2 < yaw_diff:
            yaw_diff = yaw_diff_2
            yaw_turn_direction = -yaw_turn_direction
        yaw_diff = yaw_diff * yaw_turn_direction

        return Rotation(yaw_diff, pitch_diff)



# Additional imports to avoid circular dependencies
from malmoext.agent_state import AgentState