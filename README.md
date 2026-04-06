# COP4533_PA_3

**Programming Assignment 3: Highest Value Longest Common Sequence**

## Authors

Alexander Neil - 16230392

Andrew Faircloth - 87943837

## Getting Started

### Installation

Clone the repository

```
git clone https://github.com/andrewfaircloth/COP4533_PA_3
```

Navigate to the repository

```
cd ../COP4533_PA_3
```

## Subsequence

`src/subsequence.py`

description

```
python src/subsequence.py <input_file> <output_file>
```

Example:

```
python src/subsequence.py data/benchmark_inputs.in data/benchmark_inputs.out
```

## Input

### <input_file> Format

* First line: K, The number of characters in the alphabet
* Next K lines: A character in the alphabet and its value
* Second last line: A, the first string
* Last line: B, the second string

Example Input:

```
7
w 4
o 9
i 2
f 3
p 6
m 14
h 16
fwfofpfipiomwfimmwwpifwfh
iimhfpfwhpfwmihhhfmhiopim
```

## Output

### <output_file> Format


* First line: The maximum value of a common subsequence
* Second line: One optimal common subsequence that achieves this value

Example Output:

```
69
fmiwmopf
```

## Written Component

[Written Portion](Programming_Assignment_3_Written_Portion.pdf)