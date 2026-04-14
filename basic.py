from utils import ALPHA, DELTA, parse_args, read_input_file, write_output_file

def basic_align(m: str, n: str):
    """Dynamic programming solution (Needleman-Wunsch)"""
    M, N = len(m), len(n)

    # initialize M+1 by N+1 matrix
    opt = [[0] * (N+1) for _ in range(M+1)]

    # fill in column 0
    for i in range(M+1):
        opt[i][0] = i * DELTA

    # fill in row 0
    for j in range(N+1):
        opt[0][j] = j * DELTA

    # bottom-up pass to fill in dp table
    for i in range(1, M+1):
        for j in range(1, N+1):
            opt[i][j] = min(
                opt[i-1][j-1] + ALPHA[m[i-1]][n[j-1]],  # mismatch cost
                opt[i-1][j] + DELTA,                    # gap at index i of string m
                opt[i][j-1] + DELTA                     # gap at index j of string n
            )
    
    # top-down pass to get alignment strings
    s1, s2 = "", ""
    i, j = M, N
    while i > 0 and j > 0:
        cur = opt[i][j]
        if cur == opt[i-1][j-1] + ALPHA[m[i-1]][n[j-1]]: # add both letters (go diagonally left and up in table)
            s1 += m[i-1]
            s2 += n[j-1]
            i -= 1
            j -= 1
        elif cur == opt[i-1][j] + DELTA: # add letter m[i] and gap at j (go up in table)
            s1 += m[i-1]
            s2 += '_'
            i -= 1
        else: # add letter n[j] and gap at i (go left in table)
            s1 += '_'
            s2 += n[j-1]
            j -= 1

    # add gaps for any leftover characters
    while i > 0:
        s1 += m[i-1]
        s2 += '_'
        i -= 1

    while j > 0:
        s1 += '_'
        s2 += n[j-1]
        j -= 1

    s1, s2 = s1[::-1], s2[::-1]
    return s1, s2, opt[M][N]

def main():
    input_path, output_path = parse_args()

    # 1) Read in input data
    s1, s2 = read_input_file(input_path)

    # 2) Run alignment on input data
    a1, a2, score = basic_align(s1, s2)
    print(f"The aligned version of input s1 is: {a1}")
    print(f"The aligned version of input s2 is: {a2}")
    print(f"The total minimum alignment cost is: {score}")

    # 3) Write to output file
    # write_output_file(output_path)

if __name__ == "__main__":
    main()