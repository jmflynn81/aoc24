def get_new(vals, next_val):
  new_vals = []
  for val in vals:
    new_vals.append(val + next_val)
    new_vals.append(val * next_val)
    new_vals.append(int(str(val)+str(next_val)))
  
  return new_vals


def main(data):
  total = 0
  for line in data:
    # print()
    split_vals = line.split(":")
    cal_val = int(split_vals[0])
    test_vals = split_vals[1].split()
    n = [int(test_vals[0])]
    for i in range(1, len(test_vals)):
      n = get_new(n, int(test_vals[i]))
    if cal_val in n:
      total += cal_val

  return total
