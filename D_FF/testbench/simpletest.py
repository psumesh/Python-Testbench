import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from random import randint

class D_FF(object):

     def __init__(self, dut):
           self.dut     = dut
           self.reset_i = dut.reset_i
     
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
      
             
             
@cocotb.test()
async def simpletest(dut):
      
      D_var   = D_FF(dut)
      d_input = dut.d_in
      
      cocotb.fork(Clock(dut.clock_i, 10, units='ns').start())
      cocotb.fork(D_var.reset_function())
      
      for i in range(50):
          d_input <= randint(0, 1)
          await Timer(randint(10, 45), units = 'ns')
             
             
             
             
      

