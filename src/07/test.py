
def get_next_val(vals: list, next_val: int) -> list:
  new_vals = []
  for val in vals:
    new_vals.append(val + next_val)
    new_vals.append(val * next_val)
  
  return new_vals


def main(data: list):
  total = 0
  for line in data:
    # print()
    split_vals = line.split(":")
    cal_val = int(split_vals[0])
    test_vals = split_vals[1].split()
    n = [int(test_vals[0])]
    for val in range(1, len(test_vals)):
      n = get_next_val[n, int(test_vals[val])]
    if cal_val in n:
      total += 1
      
  return total
