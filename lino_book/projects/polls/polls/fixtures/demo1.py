from lino_book.projects.polls.polls.models import Question, Choice


def objects():
    p = Question(question_text="What is your preferred colour?")
    yield p
    yield Choice(choice_text="Blue", question=p)
    yield Choice(choice_text="Red", question=p)
    yield Choice(choice_text="Yellow", question=p)
    yield Choice(choice_text="other", question=p)

    p = Question(question_text="Do you like Django?")
    yield p
    yield Choice(choice_text="Yes", question=p)
    yield Choice(choice_text="No", question=p)
    yield Choice(choice_text="Not yet decided", question=p)

    p = Question(question_text="Do you like ExtJS?")
    yield p
    yield Choice(choice_text="Yes", question=p)
    yield Choice(choice_text="No", question=p)
    yield Choice(choice_text="Not yet decided", question=p)
