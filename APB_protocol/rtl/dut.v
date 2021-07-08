module apb_slave #(parameter addrWidth = 8,
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

reg [dataWidth-1:0] mem [256];

reg [1:0] apb_st;
parameter [1:0] SETUP = 0;
parameter [1:0] W_ENABLE = 1;
parameter [1:0] R_ENABLE = 2;

// SETUP -> ENABLE
always @(posedge PCLK) begin
  if (PRESENTn==1) begin
    apb_st <= 0;
    prdata <= 0;
  end

  else begin
    case (apb_st)
      SETUP : begin
        // clear the prdata
        prdata <= 0;

        // Move to ENABLE when the psel is asserted
        if (PSELx && !PENABLE) begin
          if (PWRITE) begin
            apb_st <= W_ENABLE;
          end

          else begin
            apb_st <= R_ENABLE;
          end
        end
      end

      W_ENABLE : begin
        // write PWDATA to memory
        if (PSELx && PENABLE && PWRITE) begin
          mem[PADDR] <= PWDATA;
        end

        // return to SETUP
        apb_st <= SETUP;
      end

      R_ENABLE : begin
        // read prdata from memory
        if (PSELx && PENABLE && !PWRITE) begin
          prdata <= mem[PADDR];
        end

        // return to SETUP
        apb_st <= SETUP;
      end
    endcase
  end
end 


endmodule
