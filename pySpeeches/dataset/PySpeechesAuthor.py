#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pySpeeches/dataset/PySpeechesAuthors.py
# Description : An author.
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
from .PySpeechesDocumentCollection import *


# An Author
class PySpeechesAuthor(PySpeechesDocumentCollection):

    # Constructor
    def __init__(self, author_name, properties=None):
        """
        Constructor
        :param name:
        """
        super(PySpeechesAuthor, self).__init__(name=author_name)
        # Properties
        self._author_name = unicode(author_name)
        if properties is None:
            self._properties = dict()
        else:
            self._properties = properties
    # end __init__

    ###############################
    # GET FUNCTIONS
    ###############################

    # Get author's name
    def get_author_name(self):
        """
        Get author's name.
        :return: Author's name
        """
        return self._author_name
    # end get_name

    # Get author property's value
    def get_property(self, key):
        """
        Get author property's value.
        :param key: Property's key.
        :return: Property's value.
        """
        return self._properties[key]
    # end get_property

    # Set author property's value
    def set_property(self, key, value):
        """
        Set author property's value.
        :param key: Property's key.
        :param value: Property's value.
        :return: Property's value.
        """
        self._properties[key] = value
    # end set_property

# end PySpeechesAuthor"""


