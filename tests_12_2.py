
import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.h = runner_and_tournament.Runner("Hussein", 10)
        self.a = runner_and_tournament.Runner("Andrey", 9)
        self.n = runner_and_tournament.Runner("Nick", 3)

    def test_1(self):
        results = runner_and_tournament.Tournament(90, self.h, self.n).start()
        self.all_results[1] = results
        self.assertTrue(results.get(max(results)) == "Nick")

    def test_2(self):
        results = runner_and_tournament.Tournament(90, self.a, self.n).start()
        self.all_results[2] = results
        self.assertTrue(results.get(max(results)) == "Nick")

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

