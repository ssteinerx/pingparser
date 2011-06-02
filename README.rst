pingparser
==========
pingparser parses the output of the system ping command.

Usage
~~~~~
You can pipe ping command output into pingparser.py on the command line, which
outputs the parsed result to stdout in a customizable output format (see
``./pingparser.py --help`` for details)::

  $ ping -c 5 www.google.com | ./pingparser.py +%h %s %r %m %M %a
  www.l.google.com 5 5 14.711 26.378 19.621

Or in Python you can call ``pingparser.parse(ping_output)``, which returns
a dictionary containing the parsed fields::

  >>> import pingparser
  >>> pingparser.parse('''
  ... PING www.l.google.com (74.125.225.84) 56(84) bytes of data.
  ... 64 bytes from 74.125.225.84: icmp_req=1 ttl=55 time=13.9 ms
  ... 64 bytes from 74.125.225.84: icmp_req=2 ttl=55 time=21.4 ms
  ...
  ... --- www.l.google.com ping statistics ---
  ... 2 packets transmitted, 2 received, 0% packet loss, time 5072ms
  ... rtt min/avg/max/mdev = 13.946/17.682/21.418/3.736 ms''')
  {'received': '2', 'jitter': '3.736', 'avgping': '17.682', 'minping': '13.946', 'host': 'www.l.google.com', 'maxping': '21.418', 'sent': '2'}


Installing
~~~~~~~~~~
Download the source and run::

  $ python setup.py install

Tests
~~~~~
To run the tests, first install tox_::

  $ pip install tox

then run `tox` from the project root directory::

  $ tox

.. _tox: http://pypi.python.org/pypi/tox
