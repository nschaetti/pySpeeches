#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pySpeeches/dataset/PySpeechesDocumentCollection.py
# Description : A collectio of documents.
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
from PySpeechesDict import PySpeechesDict
import cPickle as pickle


# Read config file
class PySpeechesDocumentCollection(object):

    # Constructor
    def __init__(self, name):
        """
        Contructor
        """
        # Properties
        self._name = name
        self._documents = []
        self._authors = []
        self._max_doc_id = 0
        self._dictionary = PySpeechesDict()
        self._size = 0
        self._n_tokens = 0
        self._dict_size_history = []
    # end __init__

    ###########################################
    # IO
    ###########################################

    # Save corpus
    def save(self, filename):
        """

        :param filename:
        :return:
        """
        # Open file
        f = open(filename, 'w')

        # Write object
        pickle.dump(self, f)

        # Close file
        f.close()
    # end save

    # Open Corpus
    @staticmethod
    def load(filename):
        """

        :param filename:
        :return:
        """
        with open(filename, 'r') as f:
            corpus = pickle.load(f)
        # end with
        return corpus
    # end load

    ###########################################
    # EXISTS FUNCTIONS
    ###########################################

    # Document in collection
    def _document_exists(self, doc):
        """

        :param document:
        :return:
        """
        for document in self._documents:
            if doc.get_title() == document.get_title() and doc.get_author() == document.get_author() and \
                            doc.get_date() == document.get_date():
                return True
            # end if
        # end for
        return False
    # end _document_exists

    ###########################################
    # ADD FUNCTIONS
    ###########################################

    # Add a document
    def add_document(self, document):
        """
        Add a document to the data set.
        :param document:
        :return:
        """
        # If not in collection
        if not self._document_exists(document):
            # Increase max doc id
            if document.get_doc_id() > self._max_doc_id:
                self._max_doc_id = document.get_doc_id()
            # end if

            # Add to the document collection
            self._documents += [document]
            self._size += 1
            self._n_tokens += document.get_n_tokens()

            # Sort the collection
            self.order_by_date()

            # Update dictionary
            self._dictionary += document.get_dictionary()
            self._dict_size_history += [self._dictionary.get_size()]
        # end if
    # end add_document

    ###########################################
    # GET FUNCTIONS
    ###########################################

    # Get documents
    def get_documents(self):
        """

        :return:
        """
        return self._documents
    # end get_documents

    # Get document count
    def get_document_count(self):
        """

        :return:
        """
        return len(self._documents)
    # end get_document_count

    # Get document by Doc ID
    def get_document_by_id(self, doc_id):
        """

        :return:
        """
        # For each document
        for document in self._documents:
            if document.get_doc_id(doc_id):
                return document
            # end if
        # end fore
        return None
    # end get_document_by_ID

    # Get dictionary
    def get_dictionary(self):
        """

        :return:
        """
        return self._dictionary
    # end dictionary

    # Get size
    def get_size(self):
        """

        :return:
        """
        return self._size
    # end size

    # Get tokens count
    def get_n_tokens(self):
        """

        :return:
        """
        return self._n_tokens
    # end get_n_tokens

    # Get max doc id
    def get_max_doc_id(self):
        """

        :return:
        """
        return self._max_doc_id
    # end get_max_doc_id

    # Get name
    def get_name(self):
        """

        :return:
        """
        return self._name
    # end get_name

    ###########################################
    # SET FUNCTIONS
    ###########################################

    # Set document's date
    def set_document_date(self, doc_id, date):
        """

        :param doc_id:
        :param date:
        :return:
        """
        # For each document
        for document in self._documents:
            if document.get_doc_id() == doc_id:
                document.set_date(date)
            # end if
        # end for

        # Sort
        self.order_by_date()
    # end set_document_date

    ###########################################
    # ORDER FUNCTIONS
    ###########################################

    # Order by date
    def order_by_date(self):
        """

        :return:
        """
        self._documents = sorted(self._documents, key=lambda doc: doc.get_date())
    # end order_by_date

# end PySpeechesDocumentCollection