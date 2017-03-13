#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pySpeeches/importer/PySpeechesXMLFileImproter.py
# Description : Class to import XML files.
# Date : 9th march 2017
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
from lxml import etree
from datetime import date
import os
from .PySpeechesImporter import *
from pySpeeches.dataset.PySpeechesDocument import *
from pySpeeches.importer.PySpeechesConfig import *


# Import a directory recursively
class PySpeechesXMLFileImporter(PySpeechesImporter):

    # Get tokens
    def _get_tokens(self, text):
        # Cleaner
        text_cleaner = self._text_cleaner
        text = text_cleaner.clean_text(text)
        tokens = text.split(u' ')
        return tokens
    # end _get_tokens

    # Import source
    def import_source(self, file_name):
        """
        Import an XML filename
        :param file_name: File name to import.
        :return: The document or a list of document.
        """

        # Corpus
        config = PySpeechesConfig.Instance()
        corpus = config.get_corpus()

        # Parse XML file
        print("Parsing XML file %s" % file_name)
        tree = etree.parse(file_name)

        # Author's name
        author_id = os.path.splitext(os.path.basename(file_name))[0]

        # For each documents
        index = 0
        for doc in tree.getroot()[0]:

            # Get title, date, etc
            title = author_id + str(index)
            d_date = date.today()
            tokens = self._get_tokens(doc.text)
            doc_id = corpus.get_max_doc_id() + 1

            # Create author
            author = corpus.add_author(author_id)

            # New document
            document = PySpeechesDocument(title=title, author=author, date=d_date, url="", language="",
                                          tokens=tokens, doc_id=doc_id)

            # Add document
            corpus.add_document(document, check_doublon=self._source.get_check_doublon())

            # Next index
            index += 1
        # end doc
    # end import_source

# end PySpeechesXMLFileImporter