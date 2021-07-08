#!/bin/bash

cd ../tests
#-----------------------------------------------
#----check the existing temp files--------------
if [ -d __pycache__ ]; then
    rm -r __pycache__
    echo "deleting __pycache__ directory"
fi

if [ -d sim_build ]; then
    rm -r sim_build
    echo "deleting existing sim_build directory"
fi

if [ -f dump_apb_slave.vcd ]; then
    rm -r dump_apb_slave.vcd
    echo "deleting dump_apb_slave.vcd file" 
fi

if [ -f results.xml ]; then
    rm -r results.xml
    echo "deleting results.xml file \n \n" 
fi
#-----------------------------------------------



