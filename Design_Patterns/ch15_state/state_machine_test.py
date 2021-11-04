# Testing our state_machine.py script
import unittest
from state_machine import *

class GenericStatePatternTest(unittest.TestCase):
    def setUp(self):
        self.state_machine = StateMachine()
    def tearDown(self):
        pass
    def test_state_machine_initialises_correctly(self):
        self.assertIsInstance(self.state_machine.state, ConcreteState1)
    def test_switch_from_state_1_to_state_2(self):
        self.state_machine.switch()
        self.assertIsInstance(self.state_machine.state, ConcreteState2)
    def test_Switch_from_state_2_to_state_1(self):
        self.state_machine.switch()
        self.state_machine.switch()
        self.assertIsInstance(self.state_machine.state, ConcreteState1)

if __name__ == "__main__":
    unittest.main()







# Reference: 
# Badenhurst, Wessel. "Chapter 15: State Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 239-248,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_15.