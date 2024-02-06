import unittest
from datetime import timedelta
from student import Student
from unittest.mock import patch


class TestStudent(unittest.TestCase):
    """TestStudent"""
    @classmethod
    def setUpClass(cls):
        print('setUpClass')


    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')


    def tearDown(self):
        print('tearDown')


    def test_full_name(self):
        """test_full_name(self)"""
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')
    

    def test_email(self):
        """email testing"""
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')


    def test_alert_santa(self):
        """testing if student misbehaves"""
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)


    def test_apply_extension(self):
        """test_apply_extension"""
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, 
                         old_end_date + timedelta(days=5))


    def test_course_schedule_success(self):
        """test_course_schedule_success"""
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")


    def test_course_chedule_failed(self):
        """test_course_chedule_failed"""
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")


if __name__ == "__main__":
    unittest.main()