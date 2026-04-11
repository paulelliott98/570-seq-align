from utils import ALPHA, DELTA, parse_args, read_input_file, write_output_file

def efficient_align(m: str, n: str):
    """Dynamic programming + divide and conquer"""
    raise NotImplementedError

def main():
    input_path, output_path = parse_args()

    # 1) Read in input data
    s1, s2 = read_input_file(input_path)

    # 2) Run alignment on input data
    a1, a2, score = efficient_align(s1, s2)
    print(a1)
    print(a2)
    print(score)

    # 3) Write to output file
    write_output_file(output_path)

if __name__ == "__main__":
    main()