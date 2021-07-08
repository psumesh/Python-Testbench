
from psumesh_lib import *
            
@cocotb.test()
async def simpletest(dut):
      
    add   = adder_(dut)
      
    cocotb.fork(add.reset_function())
      
    for i in range(50):
          cocotb.fork(add.number_1_function())
          cocotb.fork(add.number_2_function())
          await Timer(randint(23, 50), units = 'ns')
      






