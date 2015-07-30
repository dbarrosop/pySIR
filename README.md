# pySIR

Python API to interact with the SIR agent.

# Installation

To install execute:

    pip install pySIR

# Documentation

pySIR implements in python the SIR API. It is just a one to one mapping to avoid dealing with the specifics of making the calls, getting the data or catching the errors. It is just a convenient way of consuming the API. It brings no extra functionality.

You can use this library like this:

    >>> from pySIR.pySIR import pySIR
    >>> sir = pySIR('http://localhost:8080')

    >>> result = sir.get_top_prefixes(start_time="2015-07-25T14:00", end_time="2015-07-25T15:00", limit_prefixes=10, net_masks="24", exclude_net_masks=1)

After every call you will get a ```Call``` object which has three attributes:

* **meta** - Some information regarding the call.

      >>> result.meta
      {u'length': 10, u'request_time': 4.2649, u'error': False}

* **result** - The actual result of the call.

      >>> result.result
      [{u'as_dst': 43650, u'sum_bytes': 96527904, u'key': u'194.132.196.0/22'}, {u'as_dst': 1299, u'sum_bytes': 50852480, u'key': u'0.0.0.0/0'}, {u'as_dst': 2856, u'sum_bytes': 42289633, u'key': u'86.128.0.0/10'}, {u'as_dst': 43650, u'sum_bytes': 27442840, u'key': u'194.132.197.72/29'}, {u'as_dst': 3320, u'sum_bytes': 23312608, u'key': u'79.192.0.0/10'}, {u'as_dst': 2856, u'sum_bytes': 22229909, u'key': u'86.128.0.0/11'}, {u'as_dst': 2856, u'sum_bytes': 19337668, u'key': u'86.128.0.0/12'}, {u'as_dst': 3320, u'sum_bytes': 19048046, u'key': u'84.128.0.0/10'}, {u'as_dst': 2856, u'sum_bytes': 18816388, u'key': u'109.144.0.0/12'}, {u'as_dst': 3320, u'sum_bytes': 18002994, u'key': u'91.0.0.0/10'}]

* **parameters** - The parameters used for the call.

      >>> result.parameters
      {u'exclude_net_masks': u'1', u'limit_prefixes': 10, u'start_time': u'2015-07-25T14:00', u'end_time': u'2015-07-25T15:00', u'net_masks': u'24'}

## Supported methods

As I mentioned before, this is a 1:1 mapping of the raw API. You can check the supported methods in the official documentation:

http://sdn-internet-router-sir.readthedocs.org/en/latest/api/api_v1.0.html

I recommend you to quickly check the code in the file ```pySIR/pySIR.py``` to quickly see the names of the methods supported. The code and the names are quite straightforward so the code should be easy to read.

## Passing variables

When passing variables to the methods just send them *named* using the same names they have in the original API. For example:

    sir.get_top_prefixes(start_time="2015-07-13T14:00", end_time="2015-07-13T15:00", limit_prefixes=10, net_masks="24", exclude_net_masks=1)
    sir.put_variables_by_category_and_name(development, whatever, content='231', extra_vars='{"asd": "qwe" , "zxc":"poi"}')

The same apply when you want to send data (for example when storing or updating a variable). For example:

    sir.post_variables(name='this_is_a_variable', content='231', category='development', extra_vars='{"asd": "qwe" , "zxc":"poi"}')
    sir.put_variables_by_category_and_name(development, whatever, content='231', extra_vars='')
