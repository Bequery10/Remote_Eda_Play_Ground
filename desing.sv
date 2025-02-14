module alu(
    input logic [31:0] a, b,
    input logic [2:0] f,
    output logic [31:0] y,
    output logic zero
    );

    logic [31:0] adder_result;
    logic [31:0] zero_extend;
    logic [31:0] mux2_out;
    logic [31:0] mux4_out;
    logic [31:0] and_result;
    logic [31:0] or_result;
    logic cout;

    logic f2_mux;
    logic [1:0] f4_mux;

    always_comb begin
        f2_mux = f[2];
        f4_mux = f[1:0];
    end

    always_comb begin
        case (f2_mux)
            1'b0: mux2_out = b;
            1'b1: mux2_out = ~b;
        endcase
    end

    BA_32bit uut (
        .sum(adder_result), 
        .cout(cout), 
        .a(a), 
        .b(mux2_out), 
        .cin(f2_mux)
    );
     
    always_comb begin
        for (int i = 0; i < 32; i++) begin
            and_result[i]  = a[i] & b[i];
            or_result[i]   = a[i] | b[i];
        end
        zero_extend = 32'b0;
        zero_extend[0] = ~cout & adder_result[31];
    end     

    always_comb begin
        case (f4_mux)
            2'b00: mux4_out = and_result;
            2'b01: mux4_out = or_result;
            2'b10: mux4_out = adder_result;
            2'b11: mux4_out = zero_extend; 
            default: mux4_out = 32'b0;
        endcase
    end

    assign y = mux4_out;
    assign zero = (y == 32'b0);
endmodule