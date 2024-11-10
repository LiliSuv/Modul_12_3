import unittest
import sss_1
import sss_2
runST=unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(sss_1.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(sss_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)