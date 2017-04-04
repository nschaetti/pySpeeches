#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pySpeeches/importer/PySpeechesConfig.py
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
from pySpeeches.patterns.Singleton import *
from PySpeechesSource import PySpeechesSource
import json
import os
import logging


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
        self._video_dir = "."
        self._audio_dir = "."
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.WARNING)
    # end __init__

    # Change log level
    def set_log_level(self, log_level):
        """

        :param log_level:
        :return:
        """
        self._logger.setLevel(log_level)
    # end set_log_level

    # Change log format
    def set_log_format(self, log_format):
        """

        :param log_format:
        :return:
        """
        formatter = logging.Formatter(log_format)
        self._logger.setFormatter(formatter)
    # end set_log_format

    # Log info
    def info(self, log):
        """

        :param log:
        :return:
        """
        self._logger.info(log)
    # end log

    # Log warning
    def warning(self, log):
        """

        :param log:
        :return:
        """
        self._logger.warning(log)
    # end log

    # Log debug
    def debug(self, log):
        """

        :param log:
        :return:
        """
        self._logger.debug(log)
    # end

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
                description = "" if 'description' not in source else source['description']
                entry_point = source['entry_point']
                title_selector = "" if 'title_selector' not in source else source['title_selector']
                date_selector = "" if 'date_selector' not in source else source['date_selector']
                date_format = "" if 'date_format' not in source else source['date_format']
                text_selector = "" if 'text_selector' not in source else source['text_selector']
                url_selector = "" if 'url_selector' not in source else source['url_selector']
                speaker_selector = "" if 'speaker_selector' not in source else source['speaker_selector']
                language_selector = "" if 'language_selector' not in source else source['language_selector']
                file_regex = "" if 'file_regex' not in source else source['file_regex']
                speaker = "" if 'speaker' not in source else source['speaker']
                language = "" if 'language' not in source else source['language']
                text_cleaner = "" if 'text_cleaner' not in source else source['text_cleaner']
                dict_size = 1000000 if 'dict_size' not in source else source['dict_size']
                check_doublon = True if 'check_doublon' not in source else source['check_doublon']

                # New source
                sources += [PySpeechesSource(s_type=s_type, name=name, description=description, entry_point=entry_point,
                                             title_selector=title_selector, date_selector=date_selector,
                                             date_format=date_format, text_selector=text_selector,
                                             url_selector=url_selector, speaker_selector=speaker_selector,
                                             language_selector=language_selector, file_regex=file_regex,
                                             speaker=speaker, language=language, text_cleaner=text_cleaner,
                                             check_doublon=check_doublon)]
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

    # Set video directory
    def set_video_directory(self, video_dir):
        """

        :param video_dir:
        :return:
        """
        if not os.path.exists(video_dir):
            os.mkdir(video_dir)
        # end if
        self._video_dir = video_dir
    # end set_video_directory

    # Get video directory
    def get_video_directory(self):
        return self._video_dir
    # end get_video_directory

    # Set audio directory
    def set_audio_directory(self, audio_dir):
        """

        :param audio_dir:
        :return:
        """
        if not os.path.exists(audio_dir):
            os.mkdir(audio_dir)
        # end if
        self._audio_dir = audio_dir
    # end set_audio_directory

    # Get audio directory
    def get_audio_directory(self):
        return self._audio_dir
    # end get_audio_directory

# end PySpeechesConfig
