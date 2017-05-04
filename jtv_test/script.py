"""
Script with simple functions in them
"""

import json
from service import Service

class MyClass(object):

    def __init__(self):
        self.s = Service()

    def f0(self):

        self.s.do_something('Hello World!')

    def f1(self):

        a = self.s.get_array()

        return a

    def f2(self, json_string):

        d = json.loads(json_string)
        m = self.s.multiply(d['rhs'], d['lhs'])

        return m
