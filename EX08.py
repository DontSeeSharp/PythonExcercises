"""Callcentre tester."""

import EX08_helper
import unittest


class Tests(unittest.TestCase):

    """
    Callcentre class testing class.

    This class contain methods that test Callcentre class.
    """

    def setup(self):
        """
        Create object with EX08_helper.

        This method creates a callcentre module with the help
        of the EX08_helper module and get_callcentre() method
        """
        call_centre_instance = EX08_helper.get_callcentre()
        return call_centre_instance

    def test_not_looping(self):
        """"Test if callcentre returns right noun."""
        instance = self.setup()
        noun_list = ["koer", "porgand", "madis", "kurk", "tomat", "koer"]
        for i in range(6):
            self.assertEqual(
                instance.create_sentence('noun'), noun_list[i])

    def test_caps_data(self):
        """Test if callcentre handles capslock."""
        instance = self.setup()
        self.assertEqual(
            instance.create_sentence('noun ABABAB'), 'koer ABABAB')

    def test_recursive(self):
        """Test if callcentre prints two sentences."""
        instance = self.setup()
        self.assertEqual(instance.create_sentence('twosentences'),
                         'koer sööb koera . porgand lööb porgandit .')

    def test_false_order(self):
        """Test if words appear in right order."""
        instance = self.setup()
        self.assertEqual(instance.create_sentence('beautifulsentence '
                                                  'beautifulsentence '
                                                  'beautifulsentence '
                                                  'beautifulsentence '
                                                  'beautifulsentence '
                                                  'beautifulsentence'),
                         'ilus koer sööb ilusat koera . '
                         'kole porgand lööb koledat porgandit . '
                         'pahane madis jagab pahast madist . '
                         'magus kurk tahab magusat kurki . '
                         'sinu tomat ei taha sinu tomatit . '
                         'ilus koer sööb ilusat koera .')

if __name__ == '__main__':
    unittest.main()
