"""

    test_openmp.py

    This file is part of ANNarchy.

    Copyright (C) 2020 Helge Uelo Dinkelbach <helge.dinkelbach@gmail.com>,
    Julien Vitay <julien.vitay@informatik.tu-chemnitz.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ANNarchy is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import unittest
from ANNarchy import setup

setup(num_threads=3)

from Common import *
from Interface import *
from Neuron import *
from Synapse import *


if __name__ == '__main__':
    unittest.main(verbosity=2)
