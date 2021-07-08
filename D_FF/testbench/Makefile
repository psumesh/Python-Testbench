
TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)
VERILOG_SOURCES   = $(PWD)/../design/*.v
TOPLEVEL         := dff_wrapper
MODULE           := simpletest


export PYTHONPATH := $(PWD)/model:$(PYTHONPATH)

include $(shell cocotb-config --makefiles)/Makefile.sim
