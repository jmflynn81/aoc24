#!/Users/c91253b/.pyenv/versions/aoc/bin/python

import argparse
from src.common.common import aoc


def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-d', '--day', type=str, help='day of the challenge, IE 01 or 25', default="01")
  parser.add_argument('-p', '--part', type=str, help='which part of the day [ 1 | 2 ]', default="1")
  parser.add_argument('-t', '--test', action='store_true')

  args =  parser.parse_args()
  validate_args(args)
  return args


def validate_args(args):
  if not 1 <= int(args.day) <= 25:
    raise ValueError("Day must be between 01 and 25")
  if args.part not in ["1", "2"]:
    raise ValueError("Part must be 1 or 2")
  

def main():
    args = get_args()

    aoc_runner = aoc(args.day, args.part, args.test)

    result, success = aoc_runner.get_result()
    if args.test:
      print(f"Result: {result}, Success: {success}")
    else:
      print(f"Result: {result}")


if __name__ == "__main__":
    main()
