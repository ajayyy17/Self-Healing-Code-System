import subprocess
import re
import inspect
import utils
from prompt_builder import build_repair_prompt
from llm_engine import call_llm


def run_tests():
    result = subprocess.run(
        ["pytest", "project/tests", "-q", "--tb=short"],
        capture_output=True,
        text=True
    )
    return result.stdout, result.returncode


def extract_failed_tests(pytest_output):
    pattern = r"FAILED (.*)::(test_\w+)"
    matches = re.findall(pattern, pytest_output)

    failed_tests = []
    for file_path, test_name in matches:
        failed_tests.append({
            "file": file_path,
            "test_name": test_name
        })

    return failed_tests


def get_test_source(file_path, test_name):
    with open(file_path, "r") as f:
        lines = f.readlines()

    capture = False
    test_lines = []

    for line in lines:

        if line.strip().startswith(f"def {test_name}"):
            capture = True

        elif capture and line.strip().startswith("def "):
            break

        if capture:
            test_lines.append(line)

    return "".join(test_lines)


def get_function_source():
    return inspect.getsource(utils.asthma_prediction)


def main():

    pytest_output, return_code = run_tests()

    if return_code == 0:
        print("All tests passed")
        return

    print("Tests failed")

    # extract failing tests
    failed_tests = extract_failed_tests(pytest_output)

    print("\nFailed Tests Detected:")
    print(failed_tests)

    print("\nError Trace:")
    print(pytest_output)

    # extract buggy function
    function_code = get_function_source()

    print("\nBuggy Function:")
    print(function_code)

    # collect failing test code
    test_code_block = ""

    for test in failed_tests:

        src = get_test_source(test["file"], test["test_name"])

        print(f"\nTest Source: {test['test_name']}")
        print(src)

        test_code_block += "\n" + src

    # build prompt for LLM
    prompt = build_repair_prompt(
        pytest_output,
        test_code_block,
        function_code
    )

    print("\nSending prompt to LLM...\n")

    llm_response = call_llm(prompt)

    print("\n===== LLM RESPONSE =====\n")
    print(llm_response)


if __name__ == "__main__":
    main()