import unittest
import runner
import runner_and_tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        r_1 = runner.Runner(self)
        for i in range(10):
            r_1.walk()
        self.assertEqual(r_1.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        r_2 = runner.Runner(self)
        for i in range(10):
            r_2.run()
        self.assertEqual(r_2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r_1 = runner.Runner(self)
        r_2 = runner.Runner(self)
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
        self.h = runner_and_tournament.Runner("Hussein", 10)
        self.a = runner_and_tournament.Runner("Andrey", 9)
        self.n = runner_and_tournament.Runner("Nick", 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
        results = runner_and_tournament.Tournament(90, self.h, self.n).start()
        self.all_results[1] = results
        self.assertTrue(results.get(max(results)) == "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
        results = runner_and_tournament.Tournament(90, self.a, self.n).start()
        self.all_results[2] = results
        self.assertTrue(results.get(max(results)) == "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
        results = runner_and_tournament.Tournament(90, self.h, self.a, self.n).start()
        self.all_results[3] = results
        self.assertTrue(results.get(max(results)) == "Nick")

    @classmethod
    def tearDownClass(cls):
        for items in cls.all_results.values():
            print(items)

if __name__ == "__main__":
    unittest.main()

