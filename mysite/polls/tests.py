import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from .models import Question

def create_questions(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """was_published_recently should return false for questions published in the future."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertFalse(future_question.was_published_recently())

    def test_was_published_recently_with_old_question(self):
        """was_published_recently should return false for questions published a long time ago."""
        time = timezone.now() - datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertFalse(future_question.was_published_recently())

    def test_was_published_recently_with_recent_question(self):
        """was_published_recently should return true for questions published recently."""
        time = timezone.now() - datetime.timedelta(hours=1)
        future_question = Question(pub_date=time)
        self.assertTrue(future_question.was_published_recently())
