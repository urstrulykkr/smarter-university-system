import unittest
from app.controllers.quizzes_controller import QuizzesController
from datetime import datetime


class QuizzesTest(unittest.TestCase):

    def setUp(self):
        self.ctrl = QuizzesController('quizzes_test.py')
        
    # adding the quiz (accepts id as integer if we give null it'll break)
    def test_expose_failure_01(self):
        self.ctrl.add_quiz(None, 'Quiz-Text', datetime.now(), datetime.now())

    # 
    def test_expose_failure_02(self):
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Title: Quiz 1", "This is quiz text", datetime(2023, 1, 7, 11, 30, 0), datetime(2023, 11, 10, 19, 30, 0))
        question_id = self.ctrl.add_question(quiz_id, "hello\uD800world", "This is question text")
        # answer_id = self.ctrl.add_answer(question_id, "this is the answer", "This is Wr
        # ong type!")
        # self.assertEqual(len(answer_id),0,  "There must be zero quizzes.")

    #lambda parameter is not serialisable that's why it breaks
    # data_loader.py", line 21
    def test_expose_failure_03(self):
        # with self.assertRaises(Exception):
        quiz_id = self.ctrl.add_quiz("", 'Quiz-Text', datetime.now(), datetime.now())
        self.ctrl.add_question(quiz_id, lambda:"", 'Question-Text')


if __name__ == '__main__':
    unittest.main()



