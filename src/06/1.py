import re


def change_direction(current_direction):
  if current_direction[0] == -1:
    return [0, 1]
  if current_direction[1] == 1:
    return [1, 0]
  if current_direction[0] == 1:
    return [0, -1]
  if current_direction[1] == -1:
    return [-1, 0]
  

def get_next_location(current_location, direction):
  return [current_location[0] + direction[0], current_location[1] + direction[1]]


def convert_to_table(data):
  
  new_table = []
  for line in data:
    new_table.append(list(line))
  return new_table


def main(data):
  
  max_vertical = len(data)
  max_horizontal = len(data[0])
  direction = [-1, 0]

  for line in range(0, len(data)):
    if "^" in data[line]:
      location = [line, re.search("\^", data[line]).span()[0]]
  
  data = convert_to_table(data)
  total = 1
  try:
    while location[0] > 0 and location[0] <= max_vertical and location[1] > 0 and location[1] <= max_horizontal:
      if data[location[0]][location[1]] == ".":
        total += 1
        data[location[0]][location[1]] = "x"
      next_location = get_next_location(location, direction)
      while data[next_location[0]][next_location[1]] == "#":
        direction = change_direction(direction)
        next_location = get_next_location(location, direction)
      location = next_location
  except:
    pass
  return total