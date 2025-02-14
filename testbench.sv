module alu_tb;

    // Inputs
    reg [3:0] a;
    reg [3:0] b;
    reg [2:0] alu_ctrl;

    // Outputs
    wire [3:0] result;
    wire zero;

    // Instantiate the ALU
    alu uut (
        .a(a),
        .b(b),
        .alu_ctrl(alu_ctrl),
        .result(result),
        .zero(zero)
    );

    initial begin
        // Initialize Inputs
        a = 0;
        b = 0;
        alu_ctrl = 0;

        // Wait for global reset
        #100;

        // Test case 1: ADD
        a = 4'b0011; // 3
        b = 4'b0101; // 5
        alu_ctrl = 3'b010; // ADD
        #10;
        $display("ADD: a = %d, b = %d, result = %d, zero = %b", a, b, result, zero);

        // Test case 2: SUB
        a = 4'b0110; // 6
        b = 4'b0011; // 3
        alu_ctrl = 3'b110; // SUB
        #10;
        $display("SUB: a = %d, b = %d, result = %d, zero = %b", a, b, result, zero);

        // Test case 3: AND
        a = 4'b1010; // 10
        b = 4'b1100; // 12
        alu_ctrl = 3'b000; // AND
        #10;
        $display("AND: a = %d, b = %d, result = %d, zero = %b", a, b, result, zero);

        // Test case 4: OR
        a = 4'b1010; // 10
        b = 4'b0101; // 5
        alu_ctrl = 3'b001; // OR
        #10;
        $display("OR: a = %d, b = %d, result = %d, zero = %b", a, b, result, zero);

        // Test case 5: Zero flag
        a = 4'b0000; // 0
        b = 4'b0000; // 0
        alu_ctrl = 3'b010; // ADD
        #10;
        $display("Zero flag: a = %d, b = %d, result = %d, zero = %b", a, b, result, zero);

        $stop;
    end

endmodule