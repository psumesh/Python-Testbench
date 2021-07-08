module adder(input      [3:0]number_1, 
             input      [3:0]number_2,
             input           reset_i,
             output reg [4:0]result
                                 );
                                 
          always @(*) begin
                 if(reset_i)
                     result = 0;
                 
                 else
                     result = number_1 + number_2;
          end


endmodule

