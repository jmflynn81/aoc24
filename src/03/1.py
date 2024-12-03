import re


def main(data):
  total = 0
  for line in data:
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
    total += sum(int(match[0])*int(match[1]) for match in matches)
  return total