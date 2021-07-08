module DFF_design(input      clock_i, 
                  input      reset_i,
                  input      d_in,
                  output reg q_o
                                 );
                                 
          always @(posedge clock_i) begin
                 if(reset_i)
                     q_o <= 0;
                 
                 else
                     q_o <= d_in;
          end


endmodule

