module dff_wrapper(input      clock_i, 
                   input      reset_i,
                   input      d_in,
                   output     q_o);
                                 
               DFF_design unit1(clock_i, 
                                reset_i,
                                d_in,
                                q_o );
               initial begin
                   $dumpfile("dff_waveform.vcd");
                   $dumpvars(1, dff_wrapper);
               end
endmodule

