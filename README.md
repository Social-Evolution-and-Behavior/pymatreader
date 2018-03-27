# pymatreader

A Python module to read Matlab files. This module works with both the old (< 7.3) and the new (>= 7.3) HDF5 based format. The output should be the same for both kinds of files.

## How to use
```python
from pymatreader import read_mat

data = read_mat(filename)
```

`data` is a python `dict` containing all variables of the mat file.

## License
This module is developed by Dirk Gütlin & Thomas Hartmann at the Universität Salzburg. You are free to use, copy, modify, distribute it under the terms of the GPL3.
