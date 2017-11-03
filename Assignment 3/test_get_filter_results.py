import unittest
import twitterverse_functions as tf


class TestGetFilterResults(unittest.TestCase):
    ''' Example unittests for get_filter_results.
        td refers to a Twitterverse dictionary.
        ul refers to a list of string containing usernames.
        fs refers to a filter spcification dictionary.
    '''
    
    global td
    td = {'tomCruise': {'following': ['katieH', 'PerezHilton'], 'bio': \
                        'Official TomCruise.com crew tweets. We love you guys! \
                        \nVisit us at Facebook!', 'location': 'Los Angeles, \
                        CA', 'name': 'Tom Cruise', 'web': \
                        'http://www.tomcruise.com'}, \
          'PerezHilton': {'following': ['tomCruise', 'katieH', 'x'],\
                          'bio': 'Perez Hilton is the creator and writer of one\
                          of the most famous websites\nin the world. And he\
                          also loves music - a lot!', 'location': 'Hollywood, \
                          California', 'name': 'Perez Hilton', 'web': \
                          'http://www.PerezH...'},\
          'a': {'following': ['tomCruise'], 'bio': 'Love the outdoors, even\
                \nin the rain.', 'location': 'Abbottsford, British Columbia', \
                'name': 'Alex D', 'web': 'www.abbotsford.ca'}, \
          'c': {'following': [''], 'bio': '', 'location': 'Kansas', 'name': \
                'The Captain', 'web': 'kellogs.com'}, \
          'x': {'following': ['c'], 'bio': '', 'location': 'Xerox Parc', \
                'name': 'Xavier', 'web': 'www.xerox.com'}, \
          'katieH': {'following': [''], 'bio': '', 'location': '', 'name': \
                     'Katie Holmes', 'web': 'www.tomkat.com'} \
          }

    def test_get_filter_results_example_1(self):
        """ Test get_filter_results with {}, [], {} """
        
        td = {}
        ul = []
        fs = {}
        actual = tf.get_filter_results(td, ul, fs)
        expected = []
        self.assertEqual(actual, expected)

    def test_get_filter_results_example_2(self):
        """ Test get_filter_results with td, ['tomCruise', 'a'], {} """
        
        ul = ['tomCruise', 'a']
        fs = {}
        actual = tf.get_filter_results(td, ul, fs)
        expected = ['tomCruise', 'a']
        self.assertEqual(actual, expected)

    def test_get_filter_results_example_3(self):
        """ 
        Test get_filter_results with td, ['tomCruise', 'a', 'PerezHilton',
        'katieH'], {'location-includes' : 'ol'}
        """
        
        ul = ['tomCruise', 'a', 'PerezHilton', 'katieH']
        fs = {'location-includes' : 'ol'}
        actual = tf.get_filter_results(td, ul, fs)
        expected = ['a', 'PerezHilton']
        self.assertEqual(actual, expected)

    def test_get_filter_results_example_4(self):
        """
        Test get_filter_results with td, ['tomCruise', 'PerezHilton', 'a',
        'c', 'x', 'katieH'], {'following' : 'katieH'}
        """
        
        ul = ['tomCruise', 'PerezHilton', 'a', 'c', 'x', 'katieH']
        fs = {'following' : 'katieH'}
        actual = tf.get_filter_results(td, ul, fs)
        expected = ['tomCruise', 'PerezHilton']
        self.assertEqual(actual, expected)

    def test_get_filter_results_example_5(self):
        """
        Test get_filter_results with td, ['tomCruise', 'PerezHilton', 'a',
        'c', 'x', 'katieH'], {'name-includes' : 'a'}
        """
        
        ul = ['tomCruise', 'PerezHilton', 'a', 'c', 'x', 'katieH']
        fs = {'name-includes' : 'a'}
        actual = tf.get_filter_results(td, ul, fs)
        expected = ['a', 'c', 'x', 'katieH']
        self.assertEqual(actual, expected)

    def test_get_filter_results_example_6(self):
        """
        Test get_filter_results with td, ['tomCruise', 'a', 'c', 'x', 'katieH'],
        {'follower' : 'tomCruise'}
        """

        ul = ['tomCruise', 'a', 'c', 'x', 'katieH']
        fs = {'follower' : 'tomCruise'}
        actual = tf.get_filter_results(td, ul, fs)
        expected = ['katieH']
        self.assertEqual(actual, expected)

    def test_get_filter_results_example_7(self):
        """
        Test get_filter_results with td, ['tomCruise', 'a', 'c', 'x', 'katieH'],
        {'following' : 'KatyPerry'}
        """

        ul = ['tomCruise', 'a', 'c', 'x', 'katieH']
        fs = {'following' : 'KatyPerry'}
        actual = tf.get_filter_results(td, ul, fs)
        expected = []
        self.assertEqual(actual, expected)

    def test_get_filter_results_example_8(self):
        """
        Test get_filter_results with td, ['tomCruise', 'a', 'c', 'x', 'katieH'],
        {'follower' : 'KatyPerry'}
        """
        
        ul = ['tomCruise', 'a', 'c', 'x', 'katieH']
        fs = {'follower' : 'KatyPerry'}
        actual = tf.get_filter_results(td, ul, fs)
        expected = []
        self.assertEqual(actual, expected)

    def test_get_filter_results_example_9(self):
        """
        Test get_filter_results with td, ['tomCruise', 'a', 'c', 'x', 'katieH'],
        {'following' : 'tomCruise', 'name-includes' : 'e',
        'location-includes' : 'ol'}
        """

        ul = ['tomCruise', 'PerezHilton', 'a', 'c', 'x', 'katieH']
        fs = {'following' : 'tomCruise', 'name-includes' : 'e', \
              'location-includes' : 'ol'}
        actual = tf.get_filter_results(td, ul, fs)
        expected = ['PerezHilton','a']
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
