import sys

def subsequence(A, B, value):
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + value.get(A[i-1], 0)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    max_val, subseq = reconstruct(A,B, value, dp)
    return max_val, subseq

def reconstruct(A, B, value, dp):
    result = []
    i, j = len(A), len(B)

    return dp[i][j], ''.join(result)

def read_input(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    K = int(lines[0])
    value = {}

    for i in range(1, K + 1):
        char, val = lines[i].split()
        value[char] = int(val)

    A = lines[K + 1]
    B = lines[K + 2]

    return A, B, value

def main():
    if len(sys.argv) != 3:
        print("Usage: python weighted_lcs.py <input_file> <output_file>")
        return

    filename = sys.argv[1]
    output_file = sys.argv[2]
    A, B, value = read_input(filename)

    max_val, subseq = subsequence(A, B, value)

    with open(output_file, 'w') as f:
        f.write(f"{max_val}\n")
        f.write(subseq + "\n")

if __name__ == "__main__":
    main()
