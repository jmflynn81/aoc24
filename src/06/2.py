import re
from collections import Counter


def change_direction(current_direction, square, data):
  if current_direction[0] == -1:
    new_direction = [0, 1]
  if current_direction[1] == 1:
    new_direction = [1, 0]
  if current_direction[0] == 1:
    new_direction = [0, -1]
  if current_direction[1] == -1:
    new_direction = [-1, 0]
  if len(square) == 4:
    square.pop(0)
  if len(square) == 3:
    vertical = [up[0] for up in square]
    horizontal = [across[1] for across in square]
    vcount = dict(Counter(vertical))
    hcount = dict(Counter(horizontal))

    if 2 in vcount.values() and 2 in hcount.values():
      dummy_loc = []
      for k, v in vcount.items():
        if v == 1:
          dummy_loc.append(k)
      for k, v in hcount.items():
        if v == 1:
          dummy_loc.append(k)
      
      tmp_loc = square[-1]
      hit = False
      while tmp_loc != dummy_loc:
        next_loc = get_next_location(tmp_loc, new_direction)
        if data[next_loc[0]][next_loc[1]] == "#":
          hit = True
          tmp_loc = dummy_loc
        else:  
          tmp_loc = next_loc
      if not hit:
        print("Square found, ", square, dummy_loc)
        return new_direction, 1
      else:
        print("Bad square found, ", square, dummy_loc)
  return new_direction, 0
  

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
  square = []
  try:
    while location[0] > 0 and location[0] <= max_vertical and location[1] > 0 and location[1] <= max_horizontal:
      next_location = get_next_location(location, direction)
      if data[next_location[0]][next_location[1]] == "#":
        square.append(location)
        direction, val = change_direction(direction, square, data)
        total += val
        next_location = get_next_location(location, direction)
      location = next_location
  except:
    pass
  return total