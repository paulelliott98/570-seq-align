"""
Shared functions and constants used in basic.py and efficient.py
"""
import sys
import os

"""Alpha and Delta values"""
ALPHA = { 
    'A': { 'A': 0, 'C': 110, 'G': 48, 'T': 94 },
    'C': { 'A': 110, 'C': 0, 'G': 118, 'T': 48 },
    'G': { 'A': 48, 'C': 118, 'G': 0, 'T': 110 },
    'T': { 'A': 94, 'C': 48, 'G': 110, 'T': 0 }
}

DELTA = 30

def parse_args():
    """Parse input and output file paths from cmd line args"""
    try:
        input_path, output_path = sys.argv[1], sys.argv[2]
    except IndexError:
        print(f"Error: Missing arguments.")
        print(f"Usage: {sys.argv[0]} <input_path> <output_path>")
        sys.exit(1)

    return input_path, output_path

def read_input_file(input_path: str) -> tuple[str, str]:
    """Read in input file into str1 and str2"""
    str1, str2 = "", ""
    with open(input_path, 'r') as f:
        line = f.readline().strip() # first string line
        str1 = line
        line = f.readline().strip()
        while line.isdigit():
            ind = int(line)
            str1 = str1[:ind+1] + str1 + str1[ind+1:]
            line = f.readline().strip()

        str2 = line
        line = f.readline().strip()
        while line.isdigit():
            ind = int(line)
            str2 = str2[:ind+1] + str2 + str2[ind+1:]
            line = f.readline().strip()
    return str1, str2

def write_output_file(output_path: str, a1: str, a2: str, score: int, time_ms: float, memory_kb: float):
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    lines = [
        f"Aligned version of s1: {a1}",
        f"Aligned version of s2: {a2}",
        f"Score: {score}",
        f"Time(ms): {time_ms}",
        f"Memory(KB): {memory_kb}",
    ]
    with open(output_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')