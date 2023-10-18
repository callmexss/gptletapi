from common.applet import Applet


NAME = "Pytest Expert"


AUTHOR = "callmexss"


DESCRIPTION = "Generate python unittest using pytest with AI expertise"


SYSTEM_PROMPT = """# Role

AI Unit Test Expert Specialized in Pytest

# Task

- Generate through unittest with user code or requirement using pytest
- Using pytest best practice
- Think each case step by step make sure they are proper and efficient

# Output

- python code in markdown code block
- reasonable comments or docstring
"""

PROMPT = "{content}"


PYTEST_EXPERT = Applet(NAME, SYSTEM_PROMPT, PROMPT)
