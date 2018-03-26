% Copyright (c) 2018, Dirk Gütlin & Thomas Hartmann
%
% This file is part of the pymatreader Project, see: https://gitlab.com/obob/pymatreader
%
%    pymatreader is free software: you can redistribute it and/or modify
%    it under the terms of the GNU General Public License as published by
%    the Free Software Foundation, either version 3 of the License, or
%    (at your option) any later version.
%
%    pymatreader is distributed in the hope that it will be useful,
%    but WITHOUT ANY WARRANTY; without even the implied warranty of
%    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
%    GNU General Public License for more details.
%
%    You should have received a copy of the GNU General Public License
%    along with obob_subjectdb. If not, see <http://www.gnu.org/licenses/>.

% This script generates the necessary test files for the unittests

restoredefaultpath

addpath('xml_io_tools');

clear all global

a_string = random_string(10);
a_second_string = random_string(20);

an_integer = randi(255, 1);
a_second_integer = randi(255, 1);

a_float = rand(1);
a_second_float = rand(1);

a_matrix = rand(100, 100);

a_cell_array = {};
for idx_cells = 1:100
  a_cell_array{idx_cells} = rand(2, 5);
end %for
clear idx_cells

a_struct = {};
a_struct.string = random_string(20);
a_struct.int = randi(255, 1);
a_struct.float = rand(1);
a_struct.matrix = rand(100, 100);
a_struct.a_cell_array = {};
for idx_cells = 1:100
  a_struct.a_cell_array{idx_cells} = rand(2, 5);
end %for
clear idx_cells

a_struct.second_level.string = random_string(20);
a_struct.second_level.int = randi(255, 1);
a_struct.second_level.float = rand(1);
a_struct.second_level.matrix = rand(100, 100);
a_struct.second_level.a_cell_array = {};
for idx_cells = 1:100
  a_struct.second_level.a_cell_array{idx_cells} = rand(2, 5);
end %for
clear idx_cells

save('v6.mat', '-v6')
save('v7.mat', '-v7')
save('v73.mat', '-v7.3')

test_data.for_xml = load('v73.mat');
xml_write('xmldata.xml', test_data);