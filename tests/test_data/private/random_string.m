function str = random_string(length)
% generates a random string of length length.

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

str = char(floor(94*rand(1, length)) + 32);
end

