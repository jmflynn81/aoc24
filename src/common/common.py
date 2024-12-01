import importlib


class aoc:
  def __init__(self, day, part, test=False) -> None:
    self.day = day
    self.part = part
    self.test = test
  
  def get_input(self):
    if self.test:
      filename = "testinput.txt"
    else:
      filename = "input.txt"
    with open(f"src/{self.day}/{filename}") as f:
      input = f.read().splitlines()
    return input
  
  def get_result(self):
    day_part = importlib.import_module(f'src.{self.day}.{self.part}')
    response = day_part.main(self.get_input())
    if self.test:
      with open(f"src/{self.day}/testresult.txt") as f:
        test_result_raw = f.read().splitlines()
        test_result = int(test_result_raw[int(self.part) - 1])
      success = response == test_result
      return response, success
    return response, False