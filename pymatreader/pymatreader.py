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


from builtins import chr  # This is needed for python 2 and 3 compatibility

import h5py
import numpy
import scipy.io
import types

__all__ = 'read_mat'

"""
This is a small module intended to facilitate reading .mat files containing large data structures into python,
disregarding of the underlying .mat file version.
"""


def read_mat(filename, variable_names=None, ignore_fields=None):
    """This function reads .mat files of version <7.3 or 7.3 and returns the contained data structure
    as a dictionary of nested substructure similar to scipy.io.loadmat style.

    Parameters
    ----------
    filename: str
        Path and filename of the .mat file containing the data.
    variable_names: list of strings, optional
        Reads only the data contained in the specified dict key or variable name. Default is None.
    ignore_fields: list of strings, optional
        Ignores every dict key/variable name specified in the list within the entire structure. Only works for .mat files
        v 7.3. Default is [].

    Returns
    -------
    dict
        A structure of nested dictionaries, with variable names as keys and variable data as values.
    """

    if ignore_fields is None:
        ignore_fields = []
    try:
        hdf5_file = scipy.io.loadmat(filename, struct_as_record=False, squeeze_me=True, variable_names=variable_names)
        data = _check_for_scipy_mat_struct(hdf5_file)
        print("finished loading .mat file <v7.3")
    except NotImplementedError:
        ignore_fields.append('#refs#')
        with h5py.File(filename, 'r') as hdf5_file:
            data = _hdf5todict(hdf5_file, variable_names=variable_names, ignore_fields=ignore_fields)
        print("finished loading .mat file v7.3")
    return data



def _hdf5todict(hdf5_object, variable_names=None, ignore_fields=None):
    """
    Recursively converts a hdf5 object to a python dictionary, converting all types as well.

    Parameters
    ----------
    hdf5_object: Union[h5py.Group, h5py.Dataset]
        Object to convert. Can be a h5py File, Group or Dataset
    variable_names: iterable, optional
        Tuple or list of variables to include. If set to none, all variable are read.
    ignore_fields: iterable, optional
        Tuple or list of fields to ignore. If set to none, all fields will be read.

    Returns
    -------
    dict
        Python dictionary
    """
    if isinstance(hdf5_object, h5py.Group):
        all_keys = set(hdf5_object.keys())
        if ignore_fields:
            all_keys = all_keys - set(ignore_fields)

        if variable_names:
            all_keys = all_keys & set(variable_names)

        return_dict = dict()

        for key in all_keys:
            return_dict[key] = _hdf5todict(hdf5_object[key], variable_names=None, ignore_fields=ignore_fields)

        return return_dict
    elif isinstance(hdf5_object, h5py.Dataset):
        data = hdf5_object.value
        if isinstance(data, numpy.ndarray) and data.dtype == numpy.dtype('object'):
            data = [hdf5_object.file[cur_data] for cur_data in data.flatten()]
            data = numpy.squeeze(_hdf5todict(data)).T

        return _assign_types(data)
    elif isinstance(hdf5_object, (list, types.GeneratorType)):
        return [_hdf5todict(item) for item in hdf5_object]
    else:
        raise TypeError('Unknown type in hdf5 file')


def _assign_types(values):
    """private function, which assigns correct types to h5py extracted values from _browse_dataset()"""

    if type(values) == numpy.ndarray:
        values = numpy.squeeze(values).T
        if values.dtype in ("uint8", "uint16", "uint32"):
            if values.size > 1:
                assigned_values = u''.join(chr(c) for c in values)
            else:
                assigned_values = chr(values)
        else:
            assigned_values = values

        if isinstance(assigned_values, numpy.ndarray) and assigned_values.size == 1:
            assigned_values = assigned_values.item()

    elif type(values) == numpy.float64:
        assigned_values = float(values)
    else:
        assigned_values = values
    return assigned_values


def _check_for_scipy_mat_struct(data):
    """
    Private function to check all entries of data for occurrences of scipy.io.matlab.mio5_params.mat_struct and convert them.

    Parameters
    ==========
    data: any
        data to be checked

    Returns
    =========
    object
        checked and converted data
    """
    if isinstance(data, dict):
        for key in data:
            data[key] = _check_for_scipy_mat_struct(data[key])

    if isinstance(data, numpy.ndarray) and data.dtype == numpy.dtype('object') and not isinstance(data, scipy.io.matlab.mio5.MatlabFunction):
        as_list = data.tolist()
        try:
            for (element, list_element) in zip(numpy.nditer(data, flags=['refs_ok'], op_flags=['readwrite']), as_list):
                if not (isinstance(list_element, numpy.ndarray) and not list_element.dtype == numpy.dtype('object')):
                    element[...] = _check_for_scipy_mat_struct(list_element)
        except TypeError:
            pass

    if isinstance(data, scipy.io.matlab.mio5_params.mat_struct):
        data = _todict(data)
        data = _check_for_scipy_mat_struct(data)

    return data


def _todict(matobj):
    """private function to enhance scipy.io.loadmat. 
    A recursive function which constructs from matobjects nested dictionaries. Idea taken from:
    <stackoverflow.com/questions/7008608/scipy-io-loadmat-nested-structures-i-e-dictionaries>"""

    data_dict = {}
    for strg in matobj._fieldnames:
        elem = matobj.__dict__[strg]
        if isinstance(elem, scipy.io.matlab.mio5_params.mat_struct):
            data_dict[strg] = _todict(elem)
        else:
            data_dict[strg] = elem
    return data_dict
