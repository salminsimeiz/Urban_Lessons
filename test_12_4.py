import rt_with_exceptions
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode="a", filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            r_1 = rt_with_exceptions.Runner("Вася", -5)
            for i in range(10):
                r_1.walk()
            self.assertEqual(r_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            r_2 = rt_with_exceptions.Runner(False, 10)
            for i in range(10):
                r_2.run()
            self.assertEqual(r_2.distance, 200)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(not is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r_1 = rt_with_exceptions.Runner(self)
        r_2 = rt_with_exceptions.Runner(self)
        for i in range(10):
            r_1.walk()
            r_2.run()
        self.assertNotEqual(r_1.distance, r_2.distance)


class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.h = rt_with_exceptions.Runner("Hussein", 10)
        self.a = rt_with_exceptions.Runner("Andrey", 9)
        self.n = rt_with_exceptions.Runner("Nick", 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
        results = rt_with_exceptions.Tournament(90, self.h, self.n).start()
        self.all_results[1] = results
        self.assertTrue(results.get(max(results)) == "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
        results = rt_with_exceptions.Tournament(90, self.a, self.n).start()
        self.all_results[2] = results
        self.assertTrue(results.get(max(results)) == "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
        results = rt_with_exceptions.Tournament(90, self.h, self.a, self.n).start()
        self.all_results[3] = results
        self.assertTrue(results.get(max(results)) == "Nick")

    @classmethod
    def tearDownClass(cls):
        for items in cls.all_results.values():
            print(items)


if __name__ == "__main__":
    unittest.main()

