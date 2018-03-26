# Copyright (c) 2018, Dirk Gütlin & Thomas Hartmann
#
# This file is part of the pymatreader Project, see: https://gitlab.com/obob/pymatreader
#
#    pymatreader is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pymatreader is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with obob_subjectdb. If not, see <http://www.gnu.org/licenses/>.

from pymatreader import read_mat
import os.path
from .test_helpers import assertDeepAlmostEqual, sanitize_dict

from unittest import TestCase
TestCase.maxDiff = None

test_data_folder = 'tests/test_data'
testdata_v6_fname = 'v6.mat'
testdata_v7_fname = 'v7.mat'
testdata_v73_fname = 'v73.mat'

def test_v6v7():
    v6_data = sanitize_dict(read_mat(os.path.join(test_data_folder, testdata_v6_fname)))
    v7_data = sanitize_dict(read_mat(os.path.join(test_data_folder, testdata_v7_fname)))

    assertDeepAlmostEqual(v6_data, v7_data)

def test_v6v73():
    v6_data = sanitize_dict(read_mat(os.path.join(test_data_folder, testdata_v6_fname)))
    v73_data = sanitize_dict(read_mat(os.path.join(test_data_folder, testdata_v73_fname)))

    assertDeepAlmostEqual(v6_data, v73_data)

def test_v7v73():
    v7_data = sanitize_dict(read_mat(os.path.join(test_data_folder, testdata_v7_fname)))
    v73_data = sanitize_dict(read_mat(os.path.join(test_data_folder, testdata_v73_fname)))

    assertDeepAlmostEqual(v7_data, v73_data)