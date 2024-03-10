#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """
    Test cases for HBNBCommand class (console).
    """

    def setUp(self):
        """
        Set up the HBNBCommand instance for testing.
        """
        self.console = HBNBCommand()

    def test_empty_line(self):
        """
        Test that an empty line + ENTER doesn't execute anything.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("\n")
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_quit_command(self):
        """
        Test the 'quit' command to exit the program.
        """
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_eof_command(self):
        """
        Test the 'EOF' command to exit the program.
        """
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_custom_prompt(self):
        """
        Test the custom prompt (hbnb).
        """
        self.assertEqual(self.console.prompt, "(hbnb) ")

    def test_help_command(self):
        """
        Test the 'help' command.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("help")
            output = mock_stdout.getvalue().strip()
            self.assertNotEqual(output, "", f"Expected non-empty output, Actual: '{output}'")

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.console

if __name__ == '__main__':
    unittest.main()

