# test.py
import os
from pingparser import parse, format_ping_result

# So at least one test succeeds
def test_happy():
    return True

def test_parse():
    for fn in os.listdir('test/data'):
        with open('test/data/'+fn,'r') as f:
            print("Test file: %s"%fn)
            # expected result is first line
            expected_result = f.readline().strip()
            # rest of file is the data
            data = f.read()
            try:
                parsed = parse(data)
                assert(format_ping_result(parsed) == expected_result)
            except (AssertionError) as e:
                e.args += ('File: %s'%fn, " failed.", parsed, expected_result)
                raise
