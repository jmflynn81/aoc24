def create_list(data, index):
  return [
    int(x.split("   ")[index])
    for x in data
  ]

def main(data):
  l1 = create_list(data, 0)
  l2 = create_list(data, 1)

  l1.sort()
  l2.sort()

  total = 0
  for i in range(0,len(l1)):
    total += abs(l2[i]-l1[i])

  return total