#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : core/downloader/PySpeechesDirectoryImproter.py
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
import re
from dateutil.parser import parse
from PySpeechesImporter import PySpeechesImporter
from core.dataset.PySpeechesDocument import PySpeechesDocument
from core.dataset.PySpeechesCorpus import PySpeechesCorpus
from core.downloader.PySpeechesConfig import PySpeechesConfig
from core.cleaning.PyWhiteHouseCleaner import PyWhiteHouseCleaner
import logging


# Import a directory recursively
class PySpeechesTextFileImporter(PySpeechesImporter):

    # Get document title
    def _get_title(self, text):
        """

        :param text:
        :return:
        """
        title = ""
        m = re.findall(self._source.get_title_selector(), text, re.MULTILINE)
        for e in m:
            title = e
        return title
    # end _get_title

    # Get document date
    def _get_date(self, text):
        """

        :param text:
        :return:
        """
        date = ""
        m = re.findall(self._source.get_date_selector(), text, re.MULTILINE)
        for e in m:
            date = e
        return date
    # end _get_date

    # Get document URL
    def _get_url(self, text):
        """

        :param text:
        :return:
        """
        url = ""
        m = re.findall(self._source.get_url_selector(), text, re.MULTILINE)
        for e in m:
            url = e
        return url
    # end _get_url

    # Get document speaker
    def _get_speaker(self, text):
        """

        :param text:
        :return:
        """
        speaker = ""
        m = re.findall(self._source.get_speaker_selector(), text, re.MULTILINE)
        for e in m:
            speaker = e
        return speaker
    # end _get_speaker

    # Get document language
    def _get_language(self, text):
        """

        :param text:
        :return:
        """
        language = ""
        m = re.findall(self._source.get_language_selector(), text, re.MULTILINE)
        for e in m:
            language = e
        return language
    # end _get_language

    # Get document text
    def _get_text(self, raw_text):
        """

        :param raw_text:
        :return:
        """
        text = ""
        m = re.findall(self._source.get_text_selector(), raw_text, re.DOTALL)
        for e in m:
            text = e
        return text
    # end _get_text

    # Get tokens
    def get_tokens(self, text):
        """
        Get text's tokens.
        :param text:
        :return: Array of tokens
        """

        # Tokens
        tokens = []

        # Clean text.
        text = PyWhiteHouseCleaner.clean_text(text)

        # For each line
        for line in text.split('\n'):
            # For each token
            for token in line.split(' '):
                if len(token) > 0 and token != "":
                    tokens.append(token)
                # end if
            # end for
        # end for

        return tokens
    # end get_tokens

    # Import source
    def import_source(self, file_name):
        """

        :return:
        """

        # Corpus
        config = PySpeechesConfig.Instance()
        corpus = config.get_corpus()

        # Open file
        f = open(file_name, 'r')

        # Read the entire file
        brut_text = f.read()

        # Get title, date, etc
        title = self._get_title(brut_text)
        date = parse(self._get_date(brut_text), dayfirst=True)
        url = self._get_url(brut_text)
        speaker = self._get_speaker(brut_text) if self._source.get_speaker() == "" else self._source.get_speaker()
        language = self._get_language(brut_text) if self._source.get_language() == "" else self._source.get_language()
        text = self._get_text(brut_text)
        tokens = self.get_tokens(text)

        # Create author
        author = corpus.add_author(speaker)

        # New document
        document = PySpeechesDocument(title=title, author=author, date=date, url=url, language=language, tokens=tokens)

        # Add document
        corpus.add_document(document)

        # Close file
        f.close()

    # end import_source

# end