from machine import Machine
from glob import glob

def list_files_in_directory(directory: str) -> list:
  files = glob(f"{directory}/*")
  return files

def read_file(file_path: str) -> list:
  with open(file_path, "r") as file:
    content = file.read()
  return content

def execute_program(machine: Machine, instructions: list) -> None:
  """
  Implementação de um algoritmo para a leitura e execução de programas monolíticos, simulando o funcionamento de uma Máquina Normal.
  As instruções devem seguir o seguinte formato:
  A=1, B=0
  1: ZER A 4 2
  2: ADD B 3
  3: SUB A 1
  Neste exemplo, a primeira linha é a assinatura, onde os valores são pré-definidos nos registradores antes da execução do programa. As demais linhas são as instruções e devem estar numeradas.

  Parâmetros:
    - machine (Machine): Uma instância da classe Machine.
    - instructions (list): Uma lista com as instruções do programa. Cada elemento da lista dentro de instructions deve conter uma linha do programa, seguindo a lógica descrita acima.
  """

  assignments = instructions[0].split(",")
  for assignment in assignments:
    register, value = assignment.split("=")
    machine.set_register(register.strip(), int(value.strip()))

  line = 1
  print(f"REGISTRADORES DE ENTRADA: {machine.get_registers()}")
  print("OPERAÇÕES:")
  while line < len(instructions):

    print(f"  {machine.get_registers()}, {line}")

    instruction = instructions[line]
    parts = instruction.split(":")
    instruction_parts = parts[1].strip().split()
    operation = instruction_parts[0]

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
      case "LESS":
        value1 = machine.get_register(instruction_parts[1])
        value2 = machine.get_register(instruction_parts[2])
        if less_than(value1, value2):
          line = int(instruction_parts[3])
        else:
          line = int(instruction_parts[4])
      case "MOD":
        value1 = machine.get_register(instruction_parts[1])
        value2 = machine.get_register(instruction_parts[2])
        if mod(value1, value2):
          line = int(instruction_parts[3])
        else:
          line = int(instruction_parts[4])
      case _:
        raise Exception(f"Client-Side Error: Operação ({operation}) não conhecida.")

def less_than(register_value1: int, register_value2: int) -> bool:
  return register_value1 < register_value2

def mod(register_value1: int, register_value2: int) -> bool:
  return (register_value1 % register_value2) == 0

def main(machine: Machine, directory: str) -> None:
  files_path = list_files_in_directory(directory)
  for path in files_path:
    file = read_file(path)

    print(f"\nEXECUÇÃO ARQUIVO {path.split("\\")[1]}")
    instructions = file.split("\n")
    execute_program(machine, instructions)
    print(f"REGISTRADORES DA SAÍDA: {machine.get_registers()}")
    machine.clear_registers()

if __name__ == "__main__":
  machine = Machine()
  main(machine, "programs")
