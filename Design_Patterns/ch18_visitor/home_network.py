# Visitor pattern

# We will simulate a network including a thermostat, temperature regulator, front door lock, coffee machine, bedroom lights, kitchen lights,
# and a clock. Suppose each object can check the status of the device it is connected to. Lights return 1 for on and 0 for off, and -1 for
# an error. The thermostat returns the temperature it is reading, or None if it is offline. The front door lock returns 1 for locked, 0 for
# unlocked, and -1 for an error. The coffee machine has states for error (-1), off (0), on (1), brewing (2), waiting (3), and heating (4). 
# The temperature regulator has states for error (-1), off (0), on (1), cooling (2), and heating (3). The clock return a time, or None if it
# is disconnected.

import random
import unittest

class Light(object):
    def __init__(self, name): 
        self.name = name
        self.status = self.get_status()
    def get_status(self): 
        return random.choice(range(-1,2))
    def is_online(self):
        return self.get_status() != -1
    def boot_up(self):
        self.status = 0

class Thermostat(object):
    def __init__(self, name): 
        self.name = name
        self.status = self.get_status()
    def get_status(self):
        temp_range = [x for x in range (-10, 50)]
        temp_range.append(None)
        return random.choice(temp_range)
    def is_online(self):
        return self.get_status() is not None
    def boot_up(self):
        pass

class TemperatureRegulator(object):
    def __init__(self, name): 
        self.name = name
        self.status = self.get_status()
    def get_status(self):
        return random.choice(['heating', 'cooling', 'on', 'off', 'error'])
    def is_online(self):
        return self.get_status() != 'error'
    def boot_up(self):
        self.status = 'on'

class DoorLock(object):
    def __init__(self, name): 
        self.name = name
        self.status = self.get_status()
    def get_status(self): 
        return random.choice(range(-1,2))
    def is_online(self):
        return self.get_status() != -1
    def boot_up(self):
        pass

class CoffeeMachine(object):
    def __init__(self, name): 
        self.name = name
        self.status = self.get_status()
    def get_status(self): 
        return random.choice(range(-1,5))
    def is_online(self):
        return self.get_status() != -1
    def boot_up(self):
        self.status = 1

class Clock(object):
    def __init__(self, name): 
        self.name = name
        self.status = self.get_status()
    def get_status(self):
        return f'{random.randrange(24)}:{random.randrange(60)}'
    def is_online(self):
        return True
    def boot_up(self):
        self.status = '00:00'

class HomeAutomationBootTest(unittest.TestCase):
    def setUp(self):
        self.thermostat = Thermostat('General Thermostat')
        self.thermal_regulator = TemperatureRegulator('Thermal Regulator')
        self.front_door_lock = DoorLock('Front Door Lock')
        self.coffee_machine = CoffeeMachine('Caffeinator9000')
        self.bedroom_light = Light('Bedroom Light')
        self.system_clock = Clock('IoTHomeSystem Clock')
    
    def test_boot_thermostat_does_nothing_to_state(self):
        state_before = self.thermostat.status
        self.thermostat.boot_up()
        self.assertEqual(state_before, self.thermostat.status)
    
    def test_boot_thermal_regulator_turns_on(self):
        self.thermal_regulator.boot_up()
        self.assertEqual(self.thermal_regulator.status, 'on')

    def test_boot_front_door_lock_does_nothing_to_state(self):
        state_before = self.front_door_lock.status
        self.front_door_lock.boot_up()
        self.assertEqual(state_before, self.front_door_lock.status)
    
    def test_boot_coffee_machine_turns_on(self):
        self.coffee_machine.boot_up()
        self.assertEqual(self.coffee_machine.status, 1)
    
    def test_boot_light_turns_off(self):
        self.bedroom_light.boot_up()
        self.assertEqual(self.bedroom_light.status, 0)
    
    def test_boot_system_clck_resets(self):
        self.system_clock.boot_up()
        self.assertEqual(self.system_clock.status, '00:00')

def main():
    device_network = [Thermostat('General Thermostat'), 
                      TemperatureRegulator('Thermal Regulator'), 
                      DoorLock('Front Door Lock'), 
                      CoffeeMachine('Caffeinator9000'), 
                      Light('Bedroom Light'), 
                      Light('Kitchen Light'), 
                      Clock('IoTHomeSystem Clock')]
    for device in device_network:
        print(f'{device.name} is online: \t{device.is_online()}')

if __name__ == "__main__":
    main()
    # unittest.main()


# Reference: 
# Badenhurst, Wessel. "Chapter 18: Visitor Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 271-297,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_18.