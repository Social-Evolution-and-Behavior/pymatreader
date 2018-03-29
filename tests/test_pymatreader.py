# -*- coding: UTF-8 -*-
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

import os.path
from unittest import TestCase

from pymatreader import read_mat
from .helper_functions import assertDeepAlmostEqual, sanitize_dict, read_xml_data

TestCase.maxDiff = None

test_data_folder = 'tests/test_data'
testdata_v6_fname = 'v6.mat'
testdata_v7_fname = 'v7.mat'
testdata_v73_fname = 'v73.mat'
testdata_xml = 'xmldata.xml'
testdata_ft_v7_fname = 'ft_v7.mat'
testdata_ft_v73_fname = 'ft_v73.mat'


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


def test_xmlv7():
    v7_data = sanitize_dict(read_mat(os.path.join(test_data_folder, testdata_v7_fname)))
    xml_data = read_xml_data(os.path.join(test_data_folder, testdata_xml))

    assertDeepAlmostEqual(v7_data, xml_data)

def test_ft_v7v73():
    v7_data = sanitize_dict(read_mat(os.path.join(test_data_folder, testdata_ft_v7_fname), variable_names=('data_epoched', )))
    v73_data = sanitize_dict(read_mat(os.path.join(test_data_folder, testdata_ft_v73_fname), variable_names=('data_epoched', )))

    assertDeepAlmostEqual(v7_data, v73_data)
