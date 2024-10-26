import unittest
import tests_12_3


mod_12TS = unittest.TestSuite()
mod_12TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
mod_12TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(mod_12TS)