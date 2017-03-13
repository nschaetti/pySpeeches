#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pySpeeches/importer/PySpeechesSource.py
# Description : Object to read config file and get sources.
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


# A speech source
class PySpeechesSource:

    # Constructor
    def __init__(self, s_type, name, description, entry_point, links_selector=[], title_selector="", date_selector="",
                 date_format="%Y-%M-%dT%h:%m:%s", text_selector="", url_selector="", speaker_selector="",
                 language_selector="", file_regex=[], speaker="", language="", text_cleaner="", check_doublon=True):
        """

        :param type:
        :param name:
        :param description:
        :param entry_point:
        :param links_selector:
        :param title_selector:
        :param date_selector:
        :param date_format:
        :param text_selector:
        :param url_selector:
        :param speaker_selector:
        :param language_selector:
        :param file_import:
        """

        # Properties
        self._type = s_type
        self._name = name
        self._description = description
        self._entry_point = entry_point
        self._links_selector = links_selector
        self._title_selector = title_selector
        self._date_selector = date_selector
        self._date_format = date_format
        self._text_selector = text_selector
        self._url_selector = url_selector
        self._speaker_selector = speaker_selector
        self._language_selector = language_selector
        self._file_regex = file_regex
        self._speaker = speaker
        self._language = language
        self._text_cleaner = text_cleaner
        self._check_doublon = check_doublon
    # end __init__

    # Get source's type
    def get_type(self):
        """

        :return:
        """
        return self._type
    # end get_type

    # Get source's name
    def get_name(self):
        """

        :return:
        """
        return self._name
    # end get_name

    # Get source's description
    def get_description(self):
        """

        :return:
        """
        return self._description
    # end get_description

    # Get source's entrypoint
    def get_entry_point(self):
        """

        :return:
        """
        return self._entry_point
    # end get_entry_point

    # Get source's links
    def get_links_selector(self):
        """

        :return:
        """
        return self._links_selector
    # end get_links

    # Get source's title
    def get_title_selector(self):
        """

        :return:
        """
        return self._title_selector
    # end get_title

    # Get source's date
    def get_date_selector(self):
        """

        :return:
        """
        return self._date_selector
    # end get_date

    # Get source's date format
    def get_date_format(self):
        """

        :return:
        """
        return self._date_format
    # end get_date_format

    # Get source's text selector
    def get_text_selector(self):
        """

        :return:
        """
        return self._text_selector
    # end get_text_selector

    # Get source's URL selector
    def get_url_selector(self):
        """

        :return:
        """
        return self._url_selector
    # end get_url_selector

    # Get source's speaker selector
    def get_speaker_selector(self):
        """

        :return:
        """
        return self._speaker_selector
    # end get_speaker_selector

    # Get source's language selector
    def get_language_selector(self):
        """

        :return:
        """
        return self._language_selector
    # end get_language_selector

    # Get file's regex
    def get_file_regex(self):
        """

        :return:
        """
        return self._file_regex
    # end get_file_regex

    # Get source's speaker
    def get_speaker(self):
        """

        :return:
        """
        return self._speaker
    # end get_speaker

    # Get source's language
    def get_language(self):
        """

        :return:
        """
        return self._language
    # end get_language

    # Get source's text cleaner
    def get_text_cleaner(self):
        """

        :return:
        """
        return self._text_cleaner
    # end get_text_cleaner

    # Get check double
    def get_check_doublon(self):
        """

        :return:
        """
        return self._check_doublon
    # end get_check_doublon

# end PySpeechesSource
