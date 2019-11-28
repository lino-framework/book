import datetime
from django.utils import timezone
from django.db import models

from lino.api import dd



class Question(dd.Model):
    question_text = models.CharField("Question text", max_length=200)
    pub_date = models.DateTimeField('Date published', default=dd.today)
    hidden = models.BooleanField(
        "Hidden",
        help_text="Whether this poll should not be shown in the main window.",
        default=False)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(dd.Model):
    question = dd.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("Choice text", max_length=200)
    votes = models.IntegerField("No. of votes", default=0)

    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

    def __str__(self):
        return self.choice_text

    @dd.action(help_text="Click here to vote this.")
    def vote(self, ar):
        def yes(ar):
            self.votes += 1
            self.save()
            return ar.success(
                "Thank you for voting %s" % self,
                "Voted!", refresh=True)
        if self.votes > 0:
            msg = "%s has already %d votes!" % (self, self.votes)
            msg += "\nDo you still want to vote for it?"
            return ar.confirm(yes, msg)
        return yes(ar)
