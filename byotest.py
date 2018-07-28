import unittest
import run

class TestStringMethods(unittest.TestCase):
    
    #Tests for genarsing game modules:

    #1
    #def test_write_to_file():



    #2
    def test_loadUsers(self):
        """
        test to check that the plyers can be loaded from the
        users file which stores player names and wrong answers.
        """
        users = run.loadUsers()
        self.assertEqual(len(users), 3)


    #3
    def test_storePlayerName(self):
        users = run.storePlayerName()
        self.assertGreater(len(users), 0)   


    #4
    def test_loadRiddles(self):
        """
        test to check that the users can be loaded from the
        json file
        """
        riddles = run.loadRiddles()
        self.assertEqual(len(riddles), 14)


    #5
    def test_validateAnswer(self):
        """
        test to vslidate the user's answer against our own
        from our json file.
        """
        riddles = run.loadRiddles()
        self.assertEqual(run.validateAnswer(riddles[0], "clock"), True)
        self.assertEqual(run.validateAnswer(riddles[0], "house"), False)

    
   
    def test_count_eq(self):
        """Will succeed"""
        self.assertCountEqual(self.result, self.expected)




    def test_list_eq(self):
        """Will fail"""
        self.assertListEqual(self.result, self.expected)




    



if __name__ == '__main__':
    unittest.main()