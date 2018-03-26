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


import h5py
import numpy
import scipy.io

from builtins import chr # This is needed for python 2 and 3 compatibility

__all__ = 'read_mat'

"""
This is a small module intended to facilitate reading .mat files containing large data structures into python,
disregarding of the underlying .mat file version.
"""


def read_mat(filename, variable_names = None, ignore_fields=[]):
    
    """This function reads .mat files of version <7.3 or 7.3 and returns the contained data structure
    as a dictionary of nested substructure similar to scipy.io.loadmat style.

    Parameters
    ----------
    filename: str
        Path and filename of the .mat file containing the data.
    variable_names: str, optional
        Reads only the data contained in the specified dict key or variable name. Default is None.
    ignore_fields: list of strings, optional
        Ignores every dict key/variable name specified in the list within the entire structure. Only works for .mat files
        v 7.3. Default is [].

    Returns
    -------
    dict
        A structure of nested dictionaries, with variable names as keys and variable data as values.
    """

    try:
        hdf5_file = scipy.io.loadmat(filename, struct_as_record=False, squeeze_me=True, variable_names=variable_names)
        data = _check_keys(hdf5_file)
        print("finished loading .mat file <v7.3")
    except NotImplementedError:
        hdf5_file = h5py.File(filename, "r")
        data = _browse(hdf5_file, hdf5_file, variable_names=variable_names, ignore_fields=ignore_fields)
        hdf5_file.close()
        print("finished loading .mat file v7.3")
    return data




def _browse(struct, hdf5_file, variable_names = None, ignore_fields=[]):
    """private function which runs through h5py structure recursively, creating subdicts for every substructure.
    calls _browse_dataset() to extract values"""
    
    copy = {}
    for key, value in zip(struct, struct.values()):
        if key not in ignore_fields and (not variable_names or key in variable_names) and key != '#refs#':
            if type(value) == h5py._hl.group.Group:
                copy[key] = _browse(value, hdf5_file, ignore_fields=ignore_fields)
            else:
                copy[key] = _browse_dataset(value, hdf5_file)
    return copy


def _browse_dataset(struct, hdf5_file):
    """private function, which recursively browses through h5py Dataset to extract values. Calls _assign_types()
    to assign data types"""
    
    if type(struct) in (h5py._hl.dataset.Dataset,numpy.ndarray):
        if struct.size > 1:
            content = numpy.squeeze(struct).T
            for ind,val in enumerate(content):
                content[ind] = _browse_dataset(val,hdf5_file)
        elif type(struct) == h5py._hl.dataset.Dataset:
            content = _browse_dataset(struct.value,hdf5_file)
        elif type(struct) == numpy.ndarray:
            content = _browse_dataset(struct[0], hdf5_file)
    elif type(struct) == h5py.h5r.Reference:
        content = hdf5_file[struct].value.T
    else:
        content = struct
    return _assign_types(content)


def _assign_types(values):
    """private function, which assigns correct types to h5py extracted values from _browse_dataset()"""
    
    if type(values) == numpy.ndarray:
        values = numpy.squeeze(values)
        if values.dtype in ("uint8","uint16","uint32"):
            if values.size > 1:
                assigned_values = u''.join(chr(c) for c in values)
            else:
                assigned_values = chr(values)
        else:
            assigned_values = values
    elif type(values) == numpy.float64:
        assigned_values = float(values)
    else:
        assigned_values = values
    return assigned_values
    
    
def _check_keys(data_dict):
    """private function to enhance scipy.io.loadmat. Checks if entries in dictionary are mat-objects.
    If yes _todict is called to change them to nested dictionaries. Idea taken from:
    <stackoverflow.com/questions/7008608/scipy-io-loadmat-nested-structures-i-e-dictionaries>"""
    
    for key in data_dict:
        if isinstance(data_dict[key], scipy.io.matlab.mio5_params.mat_struct):
            data_dict[key] = _todict(data_dict[key])
    return data_dict


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
