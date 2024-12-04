import re


def check_for_xmas(line):
  return len(re.findall("XMAS", line))


def get_reverse(data):
  new_table = []
  for line in data:
    new_table.append(line[::-1])
  return new_table


def get_vertical(data):
  width = len(data[0])
  new_table = []
  for column in range(0, width):
    new_table.append("")
    for line in range(0, len(data)):
      new_table[column] += data[line][column]
  return new_table


def get_diagonal(data):
  counter = 0
  table_size = len(data)
  new_table = []
  while(counter < 2 * table_size-1):
    new_table_tmp = []
    for i in range(table_size):
      for j in range(table_size):
        if i + j == counter:
          new_table_tmp.append(data[i][j])

    new_table_tmp.reverse()
    new_table.append("")
    for element in new_table_tmp:
      new_table[counter] += element
    counter += 1
  return new_table
   

def main(data):
  total = 0
  total += sum(check_for_xmas(line) for line in data)
  total += sum(check_for_xmas(line) for line in get_reverse(data))
  total += sum(check_for_xmas(line) for line in get_vertical(data))
  total += sum(check_for_xmas(line) for line in get_reverse(get_vertical(data)))
  total += sum(check_for_xmas(line) for line in get_diagonal(data))
  total += sum(check_for_xmas(line) for line in get_reverse(get_diagonal(data)))
  total += sum(check_for_xmas(line) for line in get_diagonal(get_reverse(data)))
  total += sum(check_for_xmas(line) for line in get_reverse(get_diagonal(get_reverse(data))))
  return total