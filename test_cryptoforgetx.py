# test_cryptoforgetx.py
"""
Tests for CryptoForgeTx module.
"""

import unittest
from cryptoforgetx import CryptoForgeTx

class TestCryptoForgeTx(unittest.TestCase):
    """Test cases for CryptoForgeTx class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoForgeTx()
        self.assertIsInstance(instance, CryptoForgeTx)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoForgeTx()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
