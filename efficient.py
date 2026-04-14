from utils import ALPHA, DELTA, parse_args, read_input_file, write_output_file
from basic import basic_align

def efficient_align(m: str, n: str):
    """Dynamic programming + divide and conquer"""
    # TODO: Base case, split, and recurse

    # Base Case
    # Currently set base case as 100 characters but this can be changed once 
    # we implement the space and time to get the sweet spot
    if len(m) <= 100 or len(n) <= 100:
        s1, s2, score = basic_align(m, n)
        return s1, s2, score
    else:
        # Split string m
        half = len(m) // 2
        m_left, m_right = m[:half], m[half:]

        # Identify split point of n
        n_split_idx = find_split(m_left, m_right, n)

        # Recurse through substrings
        m_s_left, n_s_left, score_left = efficient_align(m_left, n[:n_split_idx])
        m_s_right, n_s_right, score_right = efficient_align(m_right, n[n_split_idx:])
        
        # Concatenate and return strings and scores
        res_m = m_s_left + m_s_right
        res_n = n_s_left + n_s_right
        res_score = score_left + score_right
        return res_m, res_n, res_score


def find_split(m_left: str, m_right: str, n: str):
    # TODO: Runs calculate_score for m_left v n and m_right_reverse v n_reverse
    # Adds results columns together, returning index for min sum

    opt_left = calculate_score(m_left, n)
    opt_right = calculate_score(m_right[::-1], n[::-1])
    opt = [opt_left[k] + opt_right[len(n) - k] for k in range(len(n) + 1)]

    return opt.index(min(opt))


def calculate_score(m: str, n: str):
    # TODO: Running the DP, returning 1D array
    M, N = len(m), len(n)
    
    prev = [j * DELTA for j in range(N + 1)]

    for i in range(1, M+1):
        curr = [0] * (N+1)
        curr[0] = i * DELTA
        for j in range(1, N+1):
            curr[j] = min(prev[j-1] + ALPHA[m[i-1]][n[j-1]], 
                          prev[j] + DELTA, 
                          curr[j-1] + DELTA)
        prev = curr
    
    return prev

def main():
    input_path, output_path = parse_args()

    # 1) Read in input data
    s1, s2 = read_input_file(input_path)

    # 2) Run alignment on input data
    a1, a2, score = efficient_align(s1, s2)
    print(f"The aligned version of input s1 is: {a1}")
    print(f"The aligned version of input s2 is: {a2}")
    print(f"The total minimum alignment cost is: {score}")

    # 3) Write to output file
    # write_output_file(output_path)

if __name__ == "__main__":
    main()