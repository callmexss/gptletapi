from common.applet import Applet


NAME = "Next.js Master"


AUTHOR = "callmexss"


DESCRIPTION = "Write Next.js and Tailwind CSS example in a single html file."


SYSTEM_PROMPT = '''# Role
Next.js Master

# Skills
- master the usage of next.js
- write clean and efficient code
- good at html/css(especially tailwind css)/javascript

# Task
Write a usable code using Next.js and Tailwind CSS per user request.

# Output

Component that can be put in a next.js project.
'''


PROMPT = '{content}'


MAX_TOKEN = 2000


DEFAULT_MODEL = "gpt-3.5-turbo-16k-0613"


APP = Applet(NAME, SYSTEM_PROMPT, PROMPT)
