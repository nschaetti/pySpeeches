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

# Import package
from .PySpeechesDict import PySpeechesDict
from .PySpeechesDocumentCollection import PySpeechesDocumentCollection
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# A document
class PySpeechesDocument(object):

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
        self._current_token = 0

        # Create directory
        #self._create_dictionary(tokens)
    # end __init__

    #################################
    # ITERATOR
    #################################

    # Iter
    def __iter__(self):
        return self
    # end __iter__

    # Next
    def next(self):
        if self._current_token >= self._n_tokens:
            self._current_token = 0
            raise StopIteration
        else:
            self._current_token += 1
            return self._tokens[self._current_token - 1]
        # end if
    # end next

    #################################
    # GET FUNCTIONS
    #################################

    # Get document's title
    def get_title(self):
        """
        Get document's title
        :return: The document's title.
        """
        return self._title
    # end get_title

    # Get document's author
    def get_author(self):
        """
        Get document's author
        :return: The document's author.
        """
        return self._author
    # end get_author

    # Get document's date
    def get_date(self):
        """
        Get document's date
        :return: The document's date.
        """
        return self._date
    # end get_date

    # Get document's URL
    def get_url(self):
        """
        Get document's URL
        :return: The document's URL.
        """
        return self._url
    # end get_url

    # Get document's language
    def get_language(self):
        """
        Get document's language
        :return: The document's language.
        """
        return self._language
    # end get_language

    # Get document's tokens
    def get_tokens(self):
        """
        Get document's tokens.
        :return: Document's tokens.
        """
        return self._tokens
    # end get_tokens

    # Get document's doc id
    def get_doc_id(self):
        """
        Get document's doc id.
        :return: Document's ID.
        """
        return self._doc_id
    # end get_doc_id

    # Get size
    def get_n_tokens(self):
        """
        Get the tokens count.
        :return: The tokens count.
        """
        return self._n_tokens
    # end get_size

    #################################
    # GET FUNCTIONS
    #################################

    # Set document's ID
    def set_doc_id(self, doc_id):
        """
        Set document's ID
        :param doc_id: Document's ID.
        """
        self._doc_id = doc_id
    # end set_doc_id

    # Set document's date
    def set_date(self, date):
        """
        Set document's date
        :param date: Document's date.
        """
        self._date = date
    # end set_date

    ##################################
    # MAP FUNCTIONS
    ##################################

    # Map reduce
    def map(self, map_reducer):
        """
        Map reduce
        :param map_reducer: The PySpeechesMapReducer object.
        :return: The data computed by the PySpeechesMapReducer object.
        """
        return map_reducer.map(self)
    # end map

# end PySpeechesDocument
