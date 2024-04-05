import unittest
from main import Student
from time import sleep


class Competition(unittest.TestCase):

    def setUp(self):
        self.student = Student('Vasilij')

    def tearDown(self):
        pass

    def test_run(self):
        self.student.distance = 900
        for _ in range(10):
            self.student.run()
        self.assertEqual(self.student.distance, 1000, 'Дистанции не равны. Дистанция человека != 1000')
        print(self.student, 'дистанцию прошёл успешно')

    def test_walk(self):
        self.student.distance = 450
        for _ in range(10):
            self.student.walk()
        self.assertEqual(self.student.distance, 500, 'Дистанции не равны. Дистанция человека != 500')
        print(self.student, 'дистанцию прошёл успешно')

    def test_complete_greater(self):
        self.student.distance = 100
        for _ in range(10):
            self.student.run()
        else:
            run_distance = self.student.distance
        self.student.distance = 100
        for _ in range(10):
            self.student.walk()
        else:
            walk_distance = self.student.distance
        self.assertGreater(run_distance, walk_distance,
                           'Бегущий человек должен преодолеть дистанцию больше, чем идущий человек.')
        print(self.student, 'обогнал соперника')

    def test_complete_less(self):
        self.student.distance = 100
        for _ in range(10):
            self.student.run()
        else:
            run_distance = self.student.distance
        self.student.distance = 100
        for _ in range(10):
            self.student.walk()
        else:
            walk_distance = self.student.distance
        self.assertLess(walk_distance, run_distance,
                        'Идущий человек должен преодолеть дистанцию меньше, чем бегущий человек.')
        print(self.student, 'никуда не спешит')


if __name__ == '__main__':
    unittest.main()
