# test.py
from os import listdir
from os.path import abspath
import unittest
from pingparser import parse, format_ping_result, main


class PingParserTest(unittest.TestCase):
    """Test all of pingparser."""
    datadir = 'test/data'
    test_data = []
    custom_format_strings = [
        "%h,%s,%r,%p,%m,%a,%M,%j",
        "%s,%r,%p,%m,%a,%M,%j%h",
    ]

    @classmethod
    def setupClass(cls):
        """
        Collect all our test data first and only once.
        """
        for fn in listdir(cls.datadir):
            file_name = abspath(cls.datadir + '/' + fn)
            with open(file_name,'r') as f:
                # expected result is first line
                expected_result = f.readline().strip()
                # rest of file is the data
                data = f.read()
            cls.test_data.append((file_name, data, expected_result))

    def testParseFunction(self):
        """
        Test parse() of `data` expecting `expected_result`
        """
        for file_name, data, expected_result in self.test_data:
            try:
                parsed = parse(data)
                assert(format_ping_result(parsed) == expected_result)
            except (AssertionError) as e:
                e.args += ('File: ', file_name, ' failed comparison.', parsed, expected_result)
                raise
            except:
                # Any other exception, TODO: explicitly handle all parse() errors
                raise

    # Testing formatting is going to be annoying because the
    # only real way to do it is to pseudo-duplicate the code being
    # tested...hmmm...have to think about this a bit.
#    def test_command_line(self):
#        for file_name, data, expected_result in self.test_data:


