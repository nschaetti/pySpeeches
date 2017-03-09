#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : core/downloader/PySpeechesConfig.py
# Description : .
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
from core.patterns.Singleton import Singleton
from PySpeechesSource import PySpeechesSource
import json


# Read config file
@Singleton
class PySpeechesConfig:

    # Constructor
    def __init__(self):
        """
        Constructor
        """
        self._sources = []
        self._corpus = None
    # end __init__

    # Load a source file
    def load(self, filename):
        """
        Load the configuration file.
        :param filename: Configuration filename.
        :return: None
        """

        # Sources
        sources = []

        # Open JSON file
        with open(filename) as data_file:

            # Load JSON
            data = json.load(data_file)

            # For each source
            for source in data['sources']:

                # Get variables
                s_type = source['type']
                name = source['name']
                description = source['description']
                entry_point = source['entry_point']
                title_selector = source['title_selector']
                date_selector = source['date_selector']
                date_format = source['date_format']
                text_selector = source['text_selector']
                url_selector = source['url_selector']
                speaker_selector = source['speaker_selector']
                language_selector = source['language_selector']
                file_regex = "" if source['file_regex'] is None else source['file_regex']
                speaker = "" if source['speaker'] is None else source['speaker']
                language = "" if source['language'] is None else source['language']

                # New source
                sources += [PySpeechesSource(s_type=s_type, name=name, description=description, entry_point=entry_point,
                                             title_selector=title_selector, date_selector=date_selector,
                                             date_format=date_format, text_selector=text_selector,
                                             url_selector=url_selector, speaker_selector=speaker_selector,
                                             language_selector=language_selector, file_regex=file_regex,
                                             speaker=speaker, language=language)]
            # end for

        # end with

        # Set sources
        self._sources = sources

    # end load

    # Get sources
    def get_sources(self):
        """
        Get sources
        :return: An array of sources
        """
        return self._sources
    # end get_sources

    # Set corpus
    def set_corpus(self, corpus):
        self._corpus = corpus
    # end set_corpus

    # Get corpus
    def get_corpus(self):
        return self._corpus
    # end get_corpus

# end PySpeechesConfig
