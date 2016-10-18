from polls.models import Question, Choice

DATA = """
What is your preferred colour? | Blue | Red | Yellow | other
Do you like Django? | Yes | No | Not yet decided
Do you like ExtJS? | Yes | No | Not yet decided
Which was first? | Checken | Egg | Turkey
"""


def objects():
    for ln in DATA.splitlines():
        if ln:
            a = ln.split('|')
            q = Question(question_text=a[0].strip())
            yield q
            for choice in a[1:]:
                yield Choice(choice_text=choice.strip(), question=q)
