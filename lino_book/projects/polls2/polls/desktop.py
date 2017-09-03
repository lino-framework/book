from lino.api import dd


class Questions(dd.Table):
    model = 'polls.Question'
    order_by = ['pub_date']

    detail_layout = """
    id question_text
    hidden pub_date
    description
    ChoicesByQuestion
    """

    insert_layout = """
    question_text
    hidden
    description
    """


class Choices(dd.Table):
    model = 'polls.Choice'


class ChoicesByQuestion(Choices):
    master_key = 'question'

