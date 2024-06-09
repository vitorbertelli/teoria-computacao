class Machine:
  def __init__(self):
    self.registers = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0}

  def add(self, reg: str) -> None:
    self.registers[reg] += 1

  def sub(self, reg: str) -> None:
    if self.registers[reg] > 0:
      self.registers[reg] -= 1

  def zer(self, reg: str) -> bool:
    return self.registers[reg] == 0

  def set_register(self, reg: str, value: int) -> None:
    self.registers[reg] = value

  def get_register(self, reg: str) -> int:
    return int(self.registers[reg])

  def get_registers(self) -> dict:
    return self.registers
  
  def clear_registers(self) -> None:
    self.registers = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0}