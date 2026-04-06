# THIS FILE IS COPIED FROM https://github.com/andrewfaircloth/COP4533_PA_1
# THIS WILL BE MODIFIED TO FIT THE NEW PROBLEM STATEMENT


import time
import random
import os
from pathlib import Path
from subsequence import subsequence

def generate_random_data(n, filename="src/temp_data.in"):
    imputFile = Path(filename)
    imputFile.touch(exist_ok=True)


    with open(imputFile, "w") as f:
        f.write(f"{n}\n")
        # Generate random hospital preferences
        for _ in range(n):
            prefs = random.sample(range(1, n + 1), n)
            for pref in prefs:
                f.write(f"{pref} ")
            f.write("\n")
            # print(prefs)
        # Generate random student preferences
        for _ in range(n):
            prefs = random.sample(range(1, n + 1), n)
            for pref in prefs:
                f.write(f"{pref} ")
            f.write("\n")
            # print(prefs)
    return imputFile


def run_benchmarks():
    n_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    matcher_times = []
    verifier_times = []

    for n in n_list:
        dataFilename = generate_random_data(n)

        ## measure matcher time
        start = time.perf_counter()
        matcher_output = matcher(dataFilename, "src/temp_data.out")
        end = time.perf_counter()
        print(f"Matcher: n={n}, time={end-start:.6f}s")
        matcher_times.append(end - start)

        ## measure verifier time
        start = time.perf_counter()
        verifier_result = verifier(dataFilename, "src/temp_data.out")
        end = time.perf_counter()

        if verifier_result == -1:
            print(f"n={n}, VERIFIER FAILED")
            print("Stopping benchmarks.")
            print("Input data was:")
            with open(dataFilename, "r") as f:
                for line in f:
                    print(line.strip())
            print("Matcher output was:")
            for line in matcher_output:
                print(line)
            break

        print(f"Verifier: n={n}, time={end-start:.6f}s")
        verifier_times.append(end - start)

    return n_list, matcher_times, verifier_times

if __name__ == "__main__":
    n_list, matcher_times, verifier_times = run_benchmarks()
    print("\nBenchmark Results:")
    print("N\tMatcher Time (s)\tVerifier Time (s)")
    for n, m_time, v_time in zip(n_list, matcher_times, verifier_times):
        print(f"{n}\t{m_time:.6f}\t\t{v_time:.6f}")
    os.remove("src/temp_data.in")
    os.remove("src/temp_data.out")