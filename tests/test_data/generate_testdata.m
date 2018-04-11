% -*- coding: UTF-8 -*-
% Copyright (c) 2018, Dirk Gütlin & Thomas Hartmann
% All rights reserved.
%
% This file is part of the pymatreader Project, see: https://gitlab.com/obob/pymatreader
%
% Redistribution and use in source and binary forms, with or without
% modification, are permitted provided that the following conditions are met:
%
% * Redistributions of source code must retain the above copyright notice, this
%   list of conditions and the following disclaimer.
%
% * Redistributions in binary form must reproduce the above copyright notice,
%   this list of conditions and the following disclaimer in the documentation
%   and/or other materials provided with the distribution.
%
% THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
% AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
% IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
% DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
% FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
% DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
% SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
% CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
% OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
% OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
a_struct.a_cell_struct_array = {};
for idx_cells = 1:5
  a_struct.a_cell_struct_array{idx_cells}.int = randi(255, 1);
  a_struct.a_cell_struct_array{idx_cells}.float = rand(1);
  a_struct.a_cell_struct_array{idx_cells}.matrix = rand(100, 100);
  a_struct.a_cell_struct_array{idx_cells}.string = random_string(20);
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