import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r_1 = runner.Runner(self)
        for i in range(10):
            r_1.walk()
        self.assertEqual(r_1.distance, 50)

    def test_run(self):
        r_2 = runner.Runner(self)
        for i in range(10):
            r_2.run()
        self.assertEqual(r_2.distance, 100)

    def test_challenge(self):
        r_1 = runner.Runner(self)
        r_2 = runner.Runner(self)
        for i in range(10):
            r_1.walk()
            r_2.run()
        self.assertNotEqual(r_1.distance, r_2.distance)


if __name__ == "__main__":
    unittest.main()




