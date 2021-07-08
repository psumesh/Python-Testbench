
TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)
VERILOG_SOURCES   = $(PWD)/../rtl/*.v
TOPLEVEL         := adder_wrapper
MODULE           := simpletest


export PYTHONPATH := $(PWD)/model:$(PYTHONPATH)

include $(shell cocotb-config --makefiles)/Makefile.sim
