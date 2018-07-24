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

import os.path
from unittest import TestCase

from pymatreader import read_mat
from .helper_functions import assertDeepAlmostEqual, sanitize_dict, read_xml_data
from nose.tools import raises

TestCase.maxDiff = None

test_data_folder = 'tests/test_data'
testdata_v6_fname = 'v6.mat'
testdata_v7_fname = 'v7.mat'
testdata_v73_fname = 'v73.mat'
testdata_xml = 'xmldata.xml'
testdata_ft_v7_fname = 'ft_v7.mat'
testdata_ft_v73_fname = 'ft_v73.mat'
testdata_eeglab_h5 = 'test_raw_h5.set'
invalid_fname = 'invalid.mat'


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

def test_raw_h5_eeglab():
    data = read_mat(os.path.join(test_data_folder, testdata_eeglab_h5))

@raises(IOError)
def test_file_does_not_exist():
    read_mat(os.path.join(test_data_folder, invalid_fname))
