import unittest
import run

class TestStringMethods(unittest.TestCase):
    
    #Tests for genarsing game modules:
    def test_checkUsers(self):
        """
        test to check if a user has alresady had thier name
        registerd in the game
        """
        users = run.loadUsers()
        self.assertEqual(run.validateName(users[0], "SomeName"), True)
        self.assertEqual(run.validateName(users[0], "DuplicateName"), False)

    def test_loadUsers(self):
        """
        test to check that the users can be loaded from the
        users file
        """
        users = run.loadUsers()
        self.assertEqual(len(users),3)

    def test_loadRiddles(self):
        """
        test to check that the users can be loaded from the
        json file
        """
        riddles = run.loadRiddles()
        self.assertEqual(len(riddles), 14)

    def test_answer(self):
        """
        test to vslidate the user's answer against our own
        from our json file.
        """
        riddles = run.loadRiddles()
        self.assertEqual(run.validateAnswer(riddles[0], "clock"), True)
        self.assertEqual(run.validateAnswer(riddles[0], "house"), False)
    



if __name__ == '__main__':
    unittest.main()