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
a_second_matrix = rand(10,10);

a_cell_array = cell(4,1);
for idx_cells = 1:4
  a_cell_array{idx_cells} = rand(2, 2);
end %for
clear idx_cells
a_second_cell_array = cell(1,4);
for idx_cells = 1:4
  a_second_cell_array{idx_cells} = rand(2, 2);
end %for
clear idx_cells

a_struct = struct('a_field',random_string(2),'a_second_field',randi(2,2,2));
a_second_struct = struct('a_field',random_string(2),'a_second_field',rand(2,2));

%a_string_matrix = [random_string(10); random_string(10)];
an_integer_matrix = randi(10,2,2);

a_heading_cell_array = cell(6,1);
a_heading_cell_array{1} = a_string;
a_heading_cell_array{2} = an_integer;
a_heading_cell_array{3} = a_float;
a_heading_cell_array{4} = a_matrix;
a_heading_cell_array{5} = a_cell_array;
a_heading_cell_array{6} = a_struct;

a_second_heading_cell_array = cell(1,6);
a_second_heading_cell_array{1} = a_second_string;
a_second_heading_cell_array{2} = a_second_integer;
a_second_heading_cell_array{3} = a_second_float;
a_second_heading_cell_array{4} = a_second_matrix;
a_second_heading_cell_array{5} = a_second_cell_array;
a_second_heading_cell_array{6} = a_second_struct;


a_heading_struct = struct();
a_heading_struct.string = a_string;
a_heading_struct.integer = an_integer;
a_heading_struct.float = a_float;
a_heading_struct.matrix = a_matrix;
a_heading_struct.cell = a_cell_array;
a_heading_struct.struct = a_struct;

a_second_heading_struct = struct();
a_second_heading_struct.string = a_second_string;
a_second_heading_struct.integer = a_second_integer;
a_second_heading_struct.float = a_second_float;
a_second_heading_struct.matrix = a_second_matrix;
a_second_heading_struct.cell = a_second_cell_array;
a_second_heading_struct.struct = a_second_struct;


save('v6.mat', '-v6')
save('v7.mat', '-v7')
save('v73.mat', '-v7.3')

test_data.for_xml = load('v73.mat');
xml_write('xmldata.xml', test_data);