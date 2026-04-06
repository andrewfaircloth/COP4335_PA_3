import time
import random
import string
import os
from subsequence import read_input, subsequence


def create_input_file(path, alphabet, value_map, A, B):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(str(len(alphabet)) + "\n")
        for char in alphabet:
            f.write(char + " " + str(value_map[char]) + "\n")
        f.write(A + "\n")
        f.write(B + "\n")
    return


def generate_random_input_file(path, length, alphabet_size=7):
    alphabet = random.sample(string.ascii_lowercase, alphabet_size)
    value_map = {}
    for char in alphabet:
        value_map[char] = random.randint(1, 20)

    A = ""
    for _ in range(length):
        A += random.choice(alphabet)

    B = ""
    for _ in range(length):
        B += random.choice(alphabet)

    create_input_file(path, alphabet, value_map, A, B)

    return


def create_input_files(output_dir):
    os.makedirs(output_dir, exist_ok=True)

    lengths = [25, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800]
    input_paths = []

    for i in range(len(lengths)):
        filename = os.path.join(output_dir, "input_" + str(i + 1).zfill(2) + ".in")
        if not os.path.exists(filename):
            generate_random_input_file(filename, lengths[i], alphabet_size=7)
        input_paths.append(filename)

    return input_paths


def run_benchmarks(input_files):
    results = []

    for input_path in input_files:
        start_time = time.perf_counter()
        A, B, value = read_input(input_path)
        max_val, subsequence_result = subsequence(A, B, value)
        end_time = time.perf_counter()
        elapsed = end_time - start_time

        output_path = input_path.replace(".in", ".out")
        with open(output_path, "w") as f:
            f.write(str(max_val) + "\n")
            f.write(subsequence_result + "\n")

        results.append((len(A), len(B), elapsed))
        # print("|A|=" + str(len(A)) + ", |B|=" + str(len(B)) + ", time=" + "{:.6f}".format(elapsed) + "s")

    return results


def main():
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(script_dir)
    data_dir = os.path.join(parent_dir, "data", "benchmark_inputs")

    input_files = create_input_files(data_dir)

    print("Input files found")

    print("Running benchmark files")
    results = run_benchmarks(input_files)

    print("\nBenchmark summary:")
    print("|A|\t|B|\tTime(s)")
    for row in results:
        print(str(row[0]) + "\t" + str(row[1]) + "\t" + "{:.6f}".format(row[2]))


if __name__ == "__main__":
    main()
    