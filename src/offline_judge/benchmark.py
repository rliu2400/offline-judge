import time
from pathlib import Path

def run_benchmarks(algorithms, input_path):
    """
    algorithms: tuple of strings naming functions or executables
    input_path: file or directory of test inputs
    """
    inputs = []
    ip = Path(input_path)
    if ip.is_dir():
        inputs = sorted(ip.iterdir())
    else:
        inputs = [ip]

    for alg in algorithms:
        print(f"\n▶ Running {alg!r}")
        for inp in inputs:
            start = time.time()
            # You could import a Python function dynamically:
            #   func = __import__("your_module").__dict__[alg]
            #   func(inp)
            #
            # Or shell out to a compiled binary:
            #   subprocess.run([...])
            #
            # Here we just sleep to demo:
            time.sleep(0.1)
            elapsed = time.time() - start
            print(f"  • {inp.name}: {elapsed:.3f}s")

