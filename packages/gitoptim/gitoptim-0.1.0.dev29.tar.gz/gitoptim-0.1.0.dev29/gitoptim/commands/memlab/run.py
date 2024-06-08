import glob
import os
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from typing import Annotated, List

import typer

from gitoptim.utils.cli import console, error_console

TESTS_PATH_HELP = "Path to the folder that contains memlab tests"

def run_test(test_file) -> str:
    with tempfile.TemporaryDirectory() as tmp_dir:
        run_command = f"memlab run --scenario {test_file} --work-dir {tmp_dir}"
        result = subprocess.run(run_command, shell=True, capture_output=True, text=True, check=False)
    return {test_file: result.stdout}

def run_tests(tests_path: str) -> List[str]:
    test_files = glob.glob(os.path.join(tests_path, '*.js'))
    test_results = {}

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_test, test_file) for test_file in test_files]
        for future in futures:
            test_results.update(future.result())

    return test_results

def analyse_results(tests_results: List[str]) -> None:
    for test_file, test_result in tests_results.items():
        test_name = test_file.split("/")[-1]
        if "No leaks found" not in test_result:
            error_console.print(f"Test {test_name} leaks memory")

def command(tests_path: Annotated[str, typer.Argument(..., help=TESTS_PATH_HELP)]):
    """
    Run memlab tests and analyse the results.
    In case of memory leaks, it will print the names of the tests that have a memory leak.
    """
    console.print("Running memlab tests")
    tests_results = run_tests(tests_path)

    console.print("Analysing memlab tests")
    analyse_results(tests_results)
