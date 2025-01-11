import os
import subprocess
import time

def submit_solution(problem_id, file_path):
    problem_dir = f"problems/{problem_id}"
    if not os.path.exists(problem_dir):
        print(f"Problem {problem_id} not found. Run `oj scrape` first.")
        return

    input_file = f"{problem_dir}/input.txt"
    output_file = f"{problem_dir}/output.txt"

    # Compile C++ file
    exec_file = file_path.replace(".cpp", "")
    compile_command = f"g++ {file_path} -o {exec_file} -O2 -std=c++17"
    compile_result = subprocess.run(compile_command, shell=True, stderr=subprocess.PIPE)

    if compile_result.returncode != 0:
        print("Compilation Error ❌")
        print(compile_result.stderr.decode())
        return

    # Read input cases
    with open(input_file, "r") as fin:
        input_data = fin.read()

    # Execute compiled C++ binary
    start_time = time.time()
    process = subprocess.Popen(
        [f"./{exec_file}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    output, error = process.communicate(input=input_data)
    execution_time = time.time() - start_time

    if process.returncode != 0:
        print("Runtime Error ❌")
        print(error)
        return

    # Compare output
    with open(output_file, "r") as fout:
        expected_output = fout.read().strip()

    if output.strip() == expected_output:
        print(f"Accepted ✅ (Execution Time: {execution_time:.3f}s)")
    else:
        print("Wrong Answer ❌")
        print("\nExpected Output:\n" + expected_output)
        print("\nYour Output:\n" + output)

    # Clean up executable
    os.remove(exec_file)

