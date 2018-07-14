import unittest
import run

class TestStringMethods(unittest.TestCase):
    #samle tests  https://docs.python.org/3/library/unittest.html
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    #Tests for geenarsing game code:
    def test_loadUsers(self):
        """
        #test to check that the users can be loaded from the
        #json file
        """
        users = run.loadUsers()
        self.assertEqual(len(users),3)

    def test_loadRiddles(self):
        """
        #test to check that the users can be loaded from the
        #json file
        """
        riddles = run.loadRiddles()
        self.assertEqual(len(riddles),14)

if __name__ == '__main__':
    unittest.main()