module apb_slave_tb #(parameter addrWidth = 8,
                   parameter dataWidth = 32)
(
  input                        PCLK,
  input                        PRESENTn,
  input        [addrWidth-1:0] PADDR,
  input                        PWRITE,
  input                        PSELx,
  input                        PENABLE,
  input        [dataWidth-1:0] PWDATA,
  output reg   [dataWidth-1:0] prdata
);



apb_slave dut(
                 PCLK,
                 PRESENTn,
                 PADDR,
                 PWRITE,
                 PSELx,
                 PENABLE,
                 PWDATA,
                 prdata);


// to generate the vcd file 
initial begin
      $dumpfile("dump_apb_slave.vcd");
      $dumpvars(1, apb_slave_tb);
end

/*
//for cadence simulator
initial begin
  $shm_open("waves.shm"); 
  $shm_probe("AS");
end
// and to run irun -access +r testcase.sv -input shm.tcl

*/



endmodule
