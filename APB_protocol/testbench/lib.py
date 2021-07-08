#This file is created by Umesh Prasad
#email   : spumesh@outlook.com


import cocotb
from cocotb.triggers import Timer, RisingEdge, FallingEdge

from random import randint

from directory_setup import Temporary_file_setup


class APB_test(object):
    def __init__(self, dut, testcase_name = 'unknown testcase name'):       

        self.dut     = dut
        self.PCLK    = self.dut.PCLK
        self.PRESETn = self.dut.PRESENTn
        self.PSELx   = self.dut.PSELx
        self.PWRITE  = self.dut.PWRITE
        self.PENABLE = self.dut.PENABLE
        self.PADDR   = self.dut.PADDR
        self.PWDATA  = self.dut.PWDATA

        Temporary_file_setup()


    def clk_gen(self, periods, units):                    #global clock signal
        while True:
            self.PCLK <= 0
            yield Timer(periods/2, units)
            self.PCLK <= 1
            yield Timer(periods/2, units)

    async def reset_fn(self, rst = 1, units):                 #global reset singal
        self.PRESETn <= 1
        await Timer(30, units='ns')
        self.PRESETn <= 0
        await Timer(50, units = 'ns')
        await FallingEdge(self.PCLK)
        self.PRESETn <= rst

    @cocotb.coroutine
    async def global_signal_setup(self, periods = 100, rst = 1, units = 'ns'):
       cocotb.fork(self.clk_gen(periods, units))
       cocotb.fork(self.reset_fn(rst, units))




    @cocotb.coroutine
    async def Psel_sign(self, sel = 1):
        await RisingEdge(self.PCLK)
        self.PSELx <= 1
        await FallingEdge(self.PCLK) 
        self.PSELx <= 0
        await FallingEdge(self.PCLK)
        self.PSELx <= sel

    @cocotb.coroutine
    async def enable_sign(self, en = 1):
         self.PENABLE <= 1
         await RisingEdge(self.dut.PCLK)
         self.PENABLE <= 0
         await FallingEdge(self.PCLK)
         await Timer(10, units = 'ps')
         self.PENABLE <= en
         

    @cocotb.coroutine
    async def write_sign(self, wr = 0):
         self.PWRITE <= 0
         await RisingEdge(self.PCLK)
         self.PWRITE <= wr

    @cocotb.coroutine
    async def paddr(self, addr = 10):
         self.PADDR <= addr

    @cocotb.coroutine
    async def pwdata(self, wdata = 0xFFFFFFFF):
         self.PWDATA <= wdata

