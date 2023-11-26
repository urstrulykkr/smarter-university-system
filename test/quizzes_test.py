import unittest
from app.controllers.quizzes_controller import QuizzesController
from datetime import datetime


class QuizzesTest(unittest.TestCase):

    def setUp(self):
        self.ctrl = QuizzesController('quizzes_test.py')
        
    # This test case aims to expose a crash when adding a quiz with unsupported data type in title parameter.
    # Expected crash: quizzes_controller.py, line 63
    def test_expose_failure_01(self):
        self.ctrl.add_quiz(None, 'Quiz-Text', datetime.now(), datetime.now())

    # This test case aims to expose a crash when passing a value in add_question as parameter 
    # that cannot be converted to utf-8
    # Expected crash: quizzes_controller.py, line 78
    # Expected crash: utils.py, line 11
    def test_expose_failure_02(self):
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Title: Quiz 1", "This is quiz text", datetime(2023, 1, 7, 11, 30, 0), datetime(2023, 11, 10, 19, 30, 0))
        self.ctrl.add_question(quiz_id, "hello\uD800world", "This is question text")

    # This test case aims to expose a crash when passing a lambda as parameter which causes a failure as lambda is not serialisable which causes an exception
    # Exception crash: quizzess_controller.py, line 81
    # Exception crash: data_loader.py, line 21
    def test_expose_failure_03(self):
        quiz_id = self.ctrl.add_quiz("", 'Quiz-Text', datetime.now(), datetime.now())
        self.ctrl.add_question(quiz_id, lambda:"", 'Question-Text')
        
if __name__ == '__main__':
    unittest.main()



