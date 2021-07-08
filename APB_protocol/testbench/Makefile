TOPLEVEL_LANG  ?= verilog

PWD             = $(shell pwd)
VERILOG_SOURCES = $(PWD)/../rtl/*.v
TOPLEVEL        = apb_slave_tb
MODULE          = regression_top

export PYTHONPATH := $(PWD)/model:$(PYTHONPATH)

include $(shell cocotb-config --makefiles)/Makefile.sim
