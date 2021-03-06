# This file is a part of nylo
#
# Copyright (c) 2018 The nylo Authors (see AUTHORS)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from nylo.objects.struct.struct import Struct


class Stack(list):

    def __init__(self, elements=[Struct()]):
        list.__init__(self, elements)

    def __getitem__(self, value):
        if isinstance(value, (int, slice)):
            return list.__getitem__(self, value)
        return self[-1].getitem(value, self)

    def __contains__(self, value):
        return value in self[-1]

    def __enter__(*args):
        pass

    def __exit__(self, *args):
        self.pop()

    def __call__(self, value):
        newvalue = Struct(self[-1].value.copy())
        newvalue.update(value, self, evaluate=False)
        self.append(newvalue)
        return self
