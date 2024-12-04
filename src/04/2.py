def check_cross_part(line):
  return line == "MAS" or line == "SAM"


def main(data):
  total = 0
  for line in range(1,len(data)-1):
    for column in range(1, len(data[line])-1):
      if data[line][column] == "A":
        cross_1 = f"{data[line-1][column-1]}A{data[line+1][column+1]}"
        cross_2 = f"{data[line-1][column+1]}A{data[line+1][column-1]}"
        if check_cross_part(cross_1) and check_cross_part(cross_2):
          total +=1
  return total
