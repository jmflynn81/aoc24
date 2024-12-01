# ADVENT OF CODE 2024

## Background

The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany them as they check the places they think he was most likely to visit.

As each location is checked, they will mark it on their list with a star. They figure the Chief Historian must be in one of the first fifty places they'll look, so in order to save Christmas, you need to help them get fifty stars on their list before Santa takes off on December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

## How to use

Under the [src] folder there are all the days leading up to Christmas (01 .. 25). The answers and code for each day should be placed in each folder. There should be 2 python files 2 inpout files and a test result file.

In the top level there is a `runcode.py` file. To run any of the days and parts, use the following syntax...

> python runcode.py [ -d | --day ] str [ -p | --part ] int [ -t | --test ]

For eaxmple to run the test for the 2nd part of the 4th day, run...

> python runcode.py -d 04 -p 2 -t

It will default to running day 01 part 1 (no test) if no arguments are provided.