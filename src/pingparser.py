#!/usr/bin/env python
# coding: utf-8
"""
Parses the output of the system ping command.
"""

try:
    import simplejson as json
except ImportError:
    import json

import re
import sys

def parse(ping_output):
    """
    Parses the `ping_output` string into a dictionary containing the following
    fields:

        `host`: *string*; the target hostname that was pinged
        `sent`: *int*; the number of ping request packets sent
        `received`: *int*; the number of ping reply packets received
        `minping`: *float*; the minimum (fastest) round trip ping request/reply
                    time in milliseconds
        `avgping`: *float*; the average round trip ping time in milliseconds
        `maxping`: *float*; the maximum (slowest) round trip ping time in
                    milliseconds
        `jitter`: *float*; the standard deviation between round trip ping times
                    in milliseconds
    """
    matcher = re.compile(r'PING ([a-zA-Z0-9.\-]+) \(')
    match = matcher.search(ping_output)
    if not match:
        raise Exception('Invalid PING output')
    host = match.groups()[0]

    matcher = re.compile(r'(\d+) packets transmitted, (\d+) received')
    sent, received = matcher.search(ping_output).groups()

    matcher = re.compile(r'(\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)')
    minping, avgping, maxping, jitter = matcher.search(ping_output).groups()

    return {'host': host, 'sent': sent, 'received': received,
            'minping': minping, 'avgping': avgping, 'maxping': maxping,
            'jitter': jitter}


def main(argv=sys.argv):
    # detects whether input is piped in
    if not sys.stdin.isatty():
        ping_output = sys.stdin.read()

    result_dict = parse(ping_output)
    sys.stdout.write(json.dumps(result_dict))
    sys.exit(0)

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        pass
