import math

def get_combo_operand(operand, register_a, register_b, register_c):
    if operand == 4:
        operand = register_a
    elif operand == 5:
        operand = register_b
    elif operand == 6:
        operand = register_c

    return operand

def adv(operand, register_a):
    return int(register_a / math.pow(2, operand))

def bxl(operand, register_b):
    return register_b ^ operand

def bst(operand, register_b):
    return operand % 8

def jnz(operand, register_a, instruction_pointer):
    if register_a == 0:
        return instruction_pointer + 2

    return operand

def bxc(operand, register_b, register_c):
    return register_b ^ register_c

def out(operand):
    return str(operand % 8)

def bdv(operand, register_a):
    return int(register_a / math.pow(2, operand))

def cdv(operand, register_a):
    return int(register_a / math.pow(2, operand))

def get_puzzle_input(filepath):
    register_a = 0
    register_b = 0
    register_c = 0

    with open(filepath) as file:
        lines = file.readlines()

    register_a = int(lines[0].replace("Register A: ", ""))
    register_b = int(lines[1].replace("Register B: ", ""))
    register_c = int(lines[2].replace("Register C: ", ""))

    program = list(map(int, lines[4].strip().replace("Program: ", "").split(",")))

    return register_a, register_b, register_c, program

def run_program(register_a, register_b, register_c, program):
    instruction_pointer = 0
    result = ""

    while instruction_pointer < len(program):
        operand = program[instruction_pointer + 1]
        combo_operand = get_combo_operand(operand, register_a, register_b, register_c)
        should_increment = True
        match program[instruction_pointer]:
            case 0:
                register_a = adv(combo_operand, register_a)
            case 1:
                register_b = bxl(operand, register_b)
            case 2:
                register_b = bst(combo_operand, register_b)
            case 3:
                instruction_pointer = jnz(operand, register_a, instruction_pointer)
                should_increment = False
            case 4:
                register_b = bxc(operand, register_b, register_c)
            case 5:
                result += out(combo_operand)
                result += ","
            case 6:
                register_b = bdv(combo_operand, register_a)
            case 7:
                register_c = cdv(combo_operand, register_a)

        if should_increment:
            instruction_pointer += 2

    # We remove the last comma with this list selection
    return result[:-1]


def part_one():
    register_a, register_b, register_c, program = get_puzzle_input("input.txt")
    result = run_program(register_a, register_b, register_c, program)
    print(f"[PART ONE] - The resulting string is: {result}")

def part_two():
    register_a, register_b, register_c, program = get_puzzle_input("input.txt")
    register_a = int(math.pow(2, 40))
    result = run_program(register_a, register_b, register_c, program)

    while result != "".join(list(map(str, program))) and register_a < int(math.pow(2, 48)):
        register_a += 1
        result = run_program(register_a, register_b, register_c, program)

    print(f"[PART TW0] - The minimum value for register a is : {register_a}")

if __name__ == "__main__":
    part_one()
    part_two()









