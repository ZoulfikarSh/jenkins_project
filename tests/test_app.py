# tests/test_app.py
import io
import runpy
import unittest
from contextlib import redirect_stdout

from app import greet

EXPECTED = "Hello, World from Zoulfikar Shokor!"


class TestApp(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("World"), EXPECTED)

    def test_main_prints_greeting(self):
        output = io.StringIO()
        with redirect_stdout(output):
            runpy.run_module("app", run_name="__main__")
        self.assertEqual(output.getvalue().strip(), EXPECTED)


if __name__ == "__main__":
    unittest.main()
