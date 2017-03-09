#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pySpeeches/importer/PySpeechesDirectoryImproter.py
# Description : Class to import file recursively in a directory.
# Date : 20th of February 2017
#
# This file is part of pySpeeches.  pySpeeches is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Nils Schaetti, University of Neuchâtel <nils.schaetti@unine.ch>

# Import package
import os
import re
from .PySpeechesImporter import *
from .PySpeechesTextFileImporter import *


# Import a directory recursively
class PySpeechesDirectoryImporter(PySpeechesImporter):

    # Import text file
    def _import_text_file(self, filename):
        document = PySpeechesTextFileImporter(self._source)
        document.import_source(file_name=filename)
    # end _import_text_file

    # Import directory
    def _import_directory(self, dirname):
        # List the directory
        for filename in os.listdir(dirname):
            abs_file = dirname + "/" + filename
            if abs_file != "." and abs_file != ".." and os.path.isdir(abs_file):
                self._import_directory(abs_file)
            else:
                # Match regex
                if self._source.get_file_regex() != "":
                    if re.match(self._source.get_file_regex(), filename):
                        self._import_text_file(abs_file)
                    # end if
                else:
                    self._import_text_file(abs_file)
                # end if
            # end if
        # end for

    # end _import_directory

    # Import source
    def import_source(self, ):

        # Import endpoint
        self._import_directory(self._source.get_entry_point())

    # end import_source

# end PySpeechesDirectoryImporter
