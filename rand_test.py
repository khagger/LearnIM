import unittest
import mfa_token

class TestRandLib(unittest.TestCase):
    
    def test_rand(self):
        
        self.assertEqual(len(mfa_token.random_token(6)), 6)
        
if __name__ == '__main__':
    unittest.main()