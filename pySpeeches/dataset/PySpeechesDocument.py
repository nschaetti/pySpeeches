#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pySpeeches/dataset/PySpeechesDocument.py
# Description : A document.
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

import sys

reload(sys)
sys.setdefaultencoding('utf8')

# Import package
from .PySpeechesDict import PySpeechesDict


# A document
class PySpeechesDocument:

    # Constructor
    def __init__(self, title, author, date, url, language, tokens, doc_id=-1, location="", abstract="", video=False,
                 audio=False):
        """

        :param title:
        :param author:
        :param date:
        :param url:
        :param language:
        :param tokens:
        :param doc_id:
        """
        # Properties
        self._title = unicode(title)
        self._author = author
        self._date = date
        self._url = unicode(url)
        self._language = unicode(language)
        self._tokens = tokens
        self._doc_id = doc_id
        self._n_tokens = len(tokens)
        self._location = location
        self._abstract = abstract
        self._video = video
        self._audio = audio

        # Create directory
        self._create_dictionary(tokens)
    # end __init__

    #################################
    # DICTIONARY
    #################################

    # Create dictionary
    def _create_dictionary(self, tokens):

        # Dictionary
        self._dictionary = PySpeechesDict()

        # For each tokens
        for token in tokens:
            self._dictionary.increment_token_count(token)
        # end for
    # end _create_dictionary

    #################################
    # GET FUNCTIONS
    #################################

    # Get document's title
    def get_title(self):
        """

        :return:
        """
        return self._title
    # end get_title

    # Get document's author
    def get_author(self):
        """

        :return:
        """
        return self._author
    # end get_author

    # Get document's date
    def get_date(self):
        """

        :return:
        """
        return self._date
    # end get_date

    # Get document's URL
    def get_url(self):
        """

        :return:
        """
        return self._url
    # end get_url

    # Get document's language
    def get_language(self):
        """

        :return:
        """
        return self._language
    # end get_language

    # Get document's tokens
    def get_tokens(self):
        """

        :return:
        """
        return self._tokens
    # end get_tokens

    # Get document's doc id
    def get_doc_id(self):
        """

        :return:
        """
        return self._doc_id
    # end get_doc_id

    # Get the dictionary
    def get_dictionary(self):
        """
        Get the dictionary
        :return: The dictionary
        """
        return self._dictionary
    # end get_dictionary

    # Get size
    def get_n_tokens(self):
        """

        :return:
        """
        return self._n_tokens
    # end get_size

    #################################
    # GET FUNCTIONS
    #################################

    # Set document's ID
    def set_doc_id(self, doc_id):
        """

        :param doc_id:
        :return:
        """
        self._doc_id = doc_id
    # end set_doc_id

    # Set document's date
    def set_date(self, date):
        """

        :param date:
        :return:
        """
        self._date = date
    # end set_date

# end PySpeechesDocument
