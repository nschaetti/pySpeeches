#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pySpeeches/dataset/PySpeechesCorpus.py
# Description : A corpus of document.
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
from .PySpeechesAuthor import *
from pySpeeches.importer.PySpeechesConfig import PySpeechesConfig


# Read config file
class PySpeechesCorpus(PySpeechesDocumentCollection):

    # Constructor
    def __init__(self, name):
        """

        """
        super(PySpeechesCorpus, self).__init__(name=name)

        # Properties
        self._authors = []
    # end __init__

    ###########################################
    # EXISTS FUNCTIONS
    ###########################################

    # Check if author exists
    def author_exists(self, name):
        """

        :param name:
        :return:
        """
        # For each author
        for author in self._authors:
            if author.get_name() == name:
                return True
        # end for

        return False
    # end _author_exists

    ###########################################
    # ADD FUNCTIONS
    ###########################################

    # Add an author
    def add_author(self, name):
        """

        :param name:
        :return:
        """
        if not self.author_exists(name):
            author = PySpeechesAuthor(author_name=name)
            self._authors += [author]
            return author
        else:
            return self.get_author(name)
    # end add_author

    # Add a document
    def add_document(self, document, check_doublon=True):
        """
        Add a document to the data set.
        :param document:
        :return:
        """
        # Print info
        if not check_doublon or not self._document_exists(document):
            PySpeechesConfig.Instance().debug("Adding %s to document collection %s with author %s" % (document.get_title(), self._name, document.get_author().get_name()))
            PySpeechesConfig.Instance().debug("Nb. documents : %-6d, Nb. tokens : %-7d, Max. doc id : %-6d, "
                                             "Nb authors : %-3d" % (self.get_size(), self.get_n_tokens(),
                                                                    self.get_max_doc_id(),
                                                                    self.get_n_authors()))
        else:
            PySpeechesConfig.Instance().warning("Already in the corpus %s" % (document.get_title()))
        # end if

        # Call PySpeechesDocumentCollection
        PySpeechesDocumentCollection.add_document(self, document, check_doublon)

        # Add author
        author = document.get_author()
        author.add_document(document, check_doublon=check_doublon)
    # end add_document

    ###########################################
    # GET FUNCTIONS
    ###########################################

    # Get an author
    def get_author(self, name):
        """

        :param name:
        :return:
        """
        for author in self._authors:
            if author.get_name() == name:
                return author
            # end if
        # end for
        return None
    # end get_author

    # Get authors
    def get_authors(self):
        """

        :return:
        """
        return self._authors
    # end get_authors

    # Get authors count
    def get_n_authors(self):
        """

        :return:
        """
        return len(self._authors)
    # end get_author_count

# end PySpeechesCorpus
