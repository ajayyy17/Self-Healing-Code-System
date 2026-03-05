def build_repair_prompt(error_trace, failing_tests, function_code, examples=None):

    example_section = ""

    if examples:
        formatted_examples = []
        for i, ex in enumerate(examples, 1):
            formatted_examples.append(f"""
Example {i}

Buggy Function:
{ex["buggy_function"]}

Error:
{ex["error"]}

Correct Fix:
{ex["fix"]}
""")

        example_section = f"""
==================================================
REFERENCE REPAIR EXAMPLES

{''.join(formatted_examples)}

==================================================
"""

    prompt = f"""
You are an expert Python debugging agent.

Your role is to repair faulty Python functions that cause unit test failures.

The provided unit tests are correct and must NOT be modified.

Your objective is to analyze the error trace, understand the failing tests,
identify the root cause of the bug, and return a corrected implementation
of the function.

--------------------------------------------------

REPAIR CONSTRAINTS

1. Do NOT modify the tests.
2. Do NOT change the function name.
3. Do NOT change the function signature.
4. Only modify the implementation.
5. Return ONLY the corrected function.
6. Do NOT include explanations.
7. Do NOT include markdown formatting.
8. Output must start directly with the function definition.

--------------------------------------------------
{example_section}
--------------------------------------------------

ERROR TRACE
{error_trace}

--------------------------------------------------

FAILING TEST CASES
{failing_tests}

--------------------------------------------------

CURRENT BUGGY FUNCTION
{function_code}

--------------------------------------------------

Return ONLY the corrected Python function.
"""

    return prompt