# -*- coding: UTF-8 -*-
# Copyright (c) 2018, Dirk Gütlin & Thomas Hartmann
# All rights reserved.
#
# This file is part of the pymatreader Project, see: https://gitlab.com/obob/pymatreader
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import string

import numpy
import xmltodict
from nose.tools import assert_almost_equal, assert_equal
from six import string_types
import types


def assertDeepAlmostEqual(expected, actual, *args, **kwargs):
    # This code has been adapted from https://github.com/larsbutler/oq-engine/blob/master/tests/utils/helpers.py

    """
    Assert that two complex structures have almost equal contents.

    Compares lists, dicts and tuples recursively. Checks numeric values
    using test_case's :py:meth:`unittest.TestCase.assertAlmostEqual` and
    checks all other values with :py:meth:`unittest.TestCase.assertEqual`.
    Accepts additional positional and keyword arguments and pass those
    intact to assertAlmostEqual() (that's how you specify comparison
    precision).
    """
    is_root = not '__trace' in kwargs
    trace = kwargs.pop('__trace', 'ROOT')

    if isinstance(expected, numpy.ndarray) and expected.size == 0:
        expected = None

    if isinstance(actual, numpy.ndarray) and actual.size == 0:
        actual = None

    try:
        if isinstance(expected, (int, float, complex)):
            assert_almost_equal(expected, actual, *args, **kwargs)
        elif isinstance(expected, (list, tuple, numpy.ndarray, types.GeneratorType)):
            if isinstance(expected, types.GeneratorType):
                expected = list(expected)
                actual = list(actual)

            assert_equal(len(expected), len(actual))
            for index in range(len(expected)):
                v1, v2 = expected[index], actual[index]
                assertDeepAlmostEqual(v1, v2,
                                      __trace=repr(index), *args, **kwargs)
        elif isinstance(expected, dict):
            assert_equal(set(expected), set(actual))
            for key in expected:
                assertDeepAlmostEqual(expected[key], actual[key],
                                      __trace=repr(key), *args, **kwargs)
        else:
            assert_equal(expected, actual)
    except AssertionError as exc:
        exc.__dict__.setdefault('traces', []).append(trace)
        if is_root:
            trace = ' -> '.join(reversed(exc.traces))
            message = ''
            try:
                message = exc.message
            except AttributeError:
                pass
            exc = AssertionError("%s\nTRACE: %s" % (message, trace))
        raise exc


def sanitize_dict(d):
    d = {k: d[k] for k in d if not k.startswith('__')}

    return d


def read_xml_data(f_name):
    with open(f_name, 'rb') as xml_file:
        xml_data = xmltodict.parse(xml_file)

    new_data = _convert_strings2numbers_xml(xml_data)

    return new_data['test_data']['for_xml']


def _convert_strings2numbers_xml(xml_data):
    if isinstance(xml_data, dict):
        if len(xml_data.keys()) == 1 and list(xml_data.keys())[0] == 'item' and isinstance(xml_data['item'], list):
            xml_data = numpy.array(_convert_strings2numbers_xml(xml_data['item']))
        else:
            for cur_key in xml_data.keys():
                xml_data[cur_key] = _convert_strings2numbers_xml(xml_data[cur_key])
    elif isinstance(xml_data, list):
        new_list = []
        for cur_item in xml_data:
            new_list.append(_convert_strings2numbers_xml(cur_item))

        xml_data = new_list
    elif isinstance(xml_data, string_types) and _is_string_matrix(xml_data):
        try:
            xml_data = numpy.array(numpy.matrix(str(xml_data)))
            if xml_data.size == 1:
                xml_data = xml_data[0][0]
        except ValueError:
            pass

    return xml_data


def _is_string_matrix(value):
    ok = string.digits + '.,; []e-'
    return all(c in ok for c in value)
