from machine import Machine
from glob import glob
import sys

def list_files_in_directory(directory: str) -> list:
  files = glob(f"{directory}/*")
  return files

def read_file(file_path: str) -> list:
  with open(file_path, "r") as file:
    content = file.read()
  return content

def execute_program(machine: Machine, instructions: list) -> None:
  assignments = instructions[0].split(",")
  for assignment in assignments:
    register, value = assignment.split("=")
    machine.set_register(register.strip(), int(value.strip()))
  line = 1
  while line < len(instructions):

    print(f"{machine.get_registers()}, {line}")

    instruction = instructions[line]
    parts = instruction.split(":")
    instruction_parts = parts[1].strip().split()
    operation = instruction_parts[0]
    # register = instruction_parts[1]

    match operation:
      case "ZER":
        if machine.zer(instruction_parts[1]):
          line = int(instruction_parts[2])
        else:
          line = int(instruction_parts[3])
      case "ADD": 
        machine.add(instruction_parts[1])
        line = int(instruction_parts[2])
      case "SUB":
        machine.sub(instruction_parts[1])
        line = int(instruction_parts[2])
      case "MOV":
        # mov(machine, instruction_parts[1], instruction_parts[2])
        machine.set_register(instruction_parts[1], int(machine.get_register(instruction_parts[2])))
        line = int(instruction_parts[3])
      case "LESS":
        value1 = machine.get_register(instruction_parts[1])
        value2 = machine.get_register(instruction_parts[2])
        if less_than(value1, value2):
          line = int(instruction_parts[3])
        else:
          line = int(instruction_parts[4])
      case "REG_SUB":
        reg_sub(machine, instruction_parts[1], instruction_parts[2])
        line = int(instruction_parts[3])
      case "MOD":
        value1 = machine.get_register(instruction_parts[1])
        value2 = machine.get_register(instruction_parts[2])
        if mod(value1, value2):
          line = int(instruction_parts[3])
        else:
          line = int(instruction_parts[4])
      case _:
        raise Exception(f"Client-Side Error: Operação ({operation}) não conhecida.")

  print("FIM!\n\n")
  # machine.clear_registers()

# def mov(machine: Machine, register1: str, register2: str) -> None:
  # mov_file = read_file("macros/mov.txt")
  # instructions = mov_file.split("\n")
  # excute_machine = Machine()
  # excute_machine.set_register("B", int(machine.get_register(register2)))
  # execute_program(excute_machine, instructions)
  # machine.set_register(register1, int(excute_machine.get_register("B")))



def less_than(register_value1: int, register_value2: int) -> bool:
  less_than_file = read_file("macros/menor.txt")
  instructions = less_than_file.split("\n")
  excute_machine = Machine()
  excute_machine.set_register("A", register_value1)
  excute_machine.set_register("B", register_value2)
  execute_program(excute_machine, instructions)
  return excute_machine.get_register("E") == 1

def reg_sub(machine: Machine, register1: str, register2: str) -> None:
  reg_sub_file = read_file("macros/reg_sub.txt")
  instructions = reg_sub_file.split("\n")
  excute_machine = Machine()
  excute_machine.set_register("A", int(machine.get_register(register1)))
  excute_machine.set_register("B", int(machine.get_register(register2)))
  execute_program(excute_machine, instructions)
  machine.set_register(register1, int(excute_machine.get_register("A")))

def mod(register_value1: int, register_value2: int) -> bool:
  less_than_file = read_file("macros/mod.txt")
  instructions = less_than_file.split("\n")
  excute_machine = Machine()
  excute_machine.set_register("A", register_value1)
  excute_machine.set_register("B", register_value2)
  execute_program(excute_machine, instructions)
  return excute_machine.get_register("D") == 1

# def less_than(machine: Machine, register1: str, register2: str, registerResult: str):
#   less_than_file = read_file("macros/menor.txt")
#   instructions = less_than_file.split("\n")
#   excute_machine = Machine()
#   excute_machine.set_register("A", int(machine.get_register(register1)))
#   excute_machine.set_register("B", int(machine.get_register(register2)))
#   execute_program(excute_machine, instructions)
#   machine.set_register(registerResult, int(excute_machine.get_register("E")))

# def main(machine: Machine) -> None:
#   files_path = list_files_in_directory("instrucoes")
#   for path in files_path:
#     file = read_file(path)

#     print(path.split("\\")[1])
#     instructions = file.split("\n")
#     execute_program(machine, instructions)

if __name__ == "__main__":
  machine = Machine()
  # main(machine)
  # machine.set_register("A", 5)
  # print(machine.get_registers())
  # macro_mov(machine, "B", "A")
  # print(machine.get_registers())

  # file = read_file("instrucoes/menor.txt")
  # instructions = file.split("\n")
  # machine = Machine()
  # execute_program(machine, instructions)
  # print(machine.get_registers())

  # machine.set_register("A", 9)
  # machine.set_register("B", 3)
  # print(machine.get_registers())
  # # reg_sub(machine, "A", "B")
  # # print(machine.get_registers())
  # if less_than(machine.get_register("A"), machine.get_register("B")):
  #  print("MENOR")
  # else: 
  #   print("NAO É MENOR")
  # print(machine.get_registers())

  # file = read_file("instrucoes/mod.txt")
  # instructions = file.split("\n")
  # machine = Machine()
  # execute_program(machine, instructions)
  # print(machine.get_registers())

  # machine.set_register("A", 9)
  # machine.set_register("B", 3)
  # print(machine.get_registers())
  # if mod(machine.get_register("A"), machine.get_register("B")):
  #  print("mod")
  # else: 
  #   print("NAO É mod")
  # print(machine.get_registers())

  file = read_file("instrucoes/primo.txt")
  instructions = file.split("\n")
  machine = Machine()
  execute_program(machine, instructions)
  print(machine.get_registers())
