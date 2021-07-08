"""
testbench designed by Umesh Prasad
github : psumesh
"""


import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from random import randint
from cocotb_coverage.coverage import *

class adder_(object):

     def __init__(self, dut):
           self.dut      = dut
           self.reset_i  = dut.reset_i
           self.number_1 = dut.number_1
           self.number_2 = dut.number_2
     
     @cocotb.coroutine      
     async def reset_function(self):
             self.dut._log.info("Reset is de-asserted")
             self.reset_i <= 0
             await Timer(60, units = 'ns')
             
             self.dut._log.info("Reset if asserted")
             self.reset_i <= 1
             await Timer(45, units = 'ns')
             
             self.dut._log.info("Reset if de-asserted")
             self.reset_i <= 0
             
    
     @cocotb.coroutine
     async def number_1_function(self):
            self.number_1 <= randint(0, 15)  
     
     @cocotb.coroutine
     async def number_2_function(self):
            self.number_2 <= randint(0, 15)        

