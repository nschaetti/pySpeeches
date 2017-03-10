#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pySpeeches/dataset/PySpeechesDict.py
# Description : A dictionary.
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
import operator


# A document
class PySpeechesDict:

    # Constructor
    def __init__(self):
        self._dict = dict()
    # end

    #############################
    # ADD FUNCTIONS
    #############################

    # Increment token count
    def increment_token_count(self, token):
        """

        :param token:
        :return:
        """
        if token in self._dict.keys():
            self._dict[token] += 1
        else:
            if len(self._dict) < 10000:
                self._dict[token] = 1
            # end if
        # end if
    # end increment_token_count

    # Add increment token count
    def add_to_token_count(self, token, value):
        """

        :param token:
        :param value:
        :return:
        """
        if token in self._dict.keys():
            self._dict[token] += value
        else:
            if len(self._dict) < 10000:
                self._dict[token] = value
            # end if
    # end add_to_token_count

    #############################
    # OPERATORS
    #############################

    # Get token count
    def __getitem__(self, item):
        """

        :param item:
        :return:
        """
        return self._dict[item]
    # end __getitem_-

    # Set token count
    def __setitem__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """
        self._dict[key] = value
    # end __setitem__

    # Add dictionaries
    def __add__(self, dic):
        # For each tokens
        for token in dic.keys():
            value = dic[token]
            self.add_to_token_count(token, value)
            # end if
        # end for
        return self
    # end __add__

    #############################
    # GET FUNCTIONS
    #############################

    # Key
    def keys(self):
        return self._dict.keys()
    # end keys

    # Get dictionary
    def get_dictionary(self):
        """

        :return:
        """
        return self._dict
    # end dictionary

    # Get sorted list of token couts
    def get_sorted_list(self):
        """
        Get sorted list of token counts.
        :return:
        """
        return sorted(self._dict.items(), key=operator.itemgetter(1), reverse=True)
    # end get_sorted_dictionary

    # Get size
    def get_size(self):
        """

        :return:
        """
        return len(self._dict)
    # end get_size

    ################################
    # PRINT FUNCTION
    ################################

    # Print dictionary
    def print_dict(self):
        """

        :return:
        """
        for token in self._dict:
            print("%s : %d" % (token, self._dict[token]))
        #end for
    # end print_dict

# end PySpeechesDict
