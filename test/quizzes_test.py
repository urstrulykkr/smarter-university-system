import unittest
from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        This test case exposes a failure in the code by trying to add a quiz with a missing title.
        It is expected to crash at the line where the title is used to generate a quiz_id.
        File: quizzes_controller.py, Line: 42
        """
        self.ctrl.add_quiz(None, 'Quiz Text', datetime.now(), datetime.now())

    def test_expose_failure_02(self):
        """
        This test case exposes a failure in the code by trying to add a question to a non-existent quiz.
        It is expected to crash at the line where the quiz object is accessed.
        File: quizzes_controller.py, Line: 57
        """
        with self.assertRaises(Exception):  # Replace Exception with the actual exception type
            self.ctrl.add_question('nonexistent_quiz_id', 'Question Title', 'Question Text')

    def test_expose_failure_03(self):
        """
        This test case exposes a failure in the code by trying to add an answer to a non-existent question.
        It is expected to crash at the line where the question object is accessed.
        File: quizzes_controller.py, Line: 68
        """
        with self.assertRaises(Exception):  # Replace Exception with the actual exception type
            self.ctrl.add_answer('nonexistent_question_id', 'Answer Text', True)

if __name__ == '__main__':
    unittest.main()
