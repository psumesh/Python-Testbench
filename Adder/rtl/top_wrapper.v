module adder_wrapper(input      [3:0]number_1, 
                     input      [3:0]number_2,
                     input           reset_i,
                     output reg [4:0]result
                                 );
                                 
       adder dut_unit(number_1, 
                      number_2, 
                      reset_i, 
                      result);
                      
               initial begin
                   $dumpfile("adder_waveform.vcd");
                   $dumpvars(1, adder_wrapper);
               end
endmodule

