#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pySpeeches/cleaning/PySpeechesWhiteHouseCleaner.py
# Description : Clean speeches from the white house website.
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
from .cleaning_functions import *
from .PySpeechesCleaner import *


# An Author
class PyWhiteHouseCleaner(PySpeechesCleaner):

    # Constructor
    def __init__(self):
        """
        Constructor.
        """
        pass
    # end __init__

    # Clean text
    @staticmethod
    def clean_text(text):
        """
        Clean text.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        text = PyWhiteHouseCleaner.apply_cleaning_functions_to_global_text(text)
        text = PyWhiteHouseCleaner.apply_cleaning_functions_to_splitted_text(text)
        return text
    # end clean_text

    # Apply cleaning functions to global text
    @staticmethod
    def apply_cleaning_functions_to_global_text(text):
        """
        Apply the first sequence of cleaning functions in a specific order for Obama's texts.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        text = PyCleaningTool.remove_informations(text)
        text = PyCleaningTool.remove_text_between_parenthesis_brackets(text)
        text = PyCleaningTool.replace_special_characters(text)
        text = PyCleaningTool.remove_useless_characters(text)
        text = PyCleaningTool.remove_not_ending_dot(text)
        text = PyCleaningTool.keep_ascii_characters_only(text)
        text = PyCleaningTool.inverse_dot_and_quote(text)
        text = PyCleaningTool.remove_single_quote(text)
        text = PyCleaningTool.replace_sharp_hashtag(text)
        return text
    # end apply_cleaning_functions_to_global_text

    # Apply cleaning functions to splitted text
    @staticmethod
    def apply_cleaning_functions_to_splitted_text(text):
        """
        Apply the second sequence of cleaning functions in a specific order for Obama's texts.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        text = PyCleaningTool.insert_space_between_special_word(text)
        text = PyCleaningTool.newline_after_end_of_sentence(text)
        text = PyCleaningTool.many_spaces_to_one_space(text)
        text = PyCleaningTool.strip_every_lines_from_space(text)
        text = PyCleaningTool.many_newlines_to_one_newline(text)
        text = PyCleaningTool.cancel_newline_if_not_end_of_sentence(text)
        text = PyCleaningTool.remove_dot_exclamation_interrogation_alone(text)
        text = PyCleaningTool.space_between_each_word(text)
        return text
    # end apply_cleaning_functions_to_splitted_text

    # Apply cleaning functions to other presidents text
    @staticmethod
    def apply_cleaning_functions_to_other_presidents_text(text):
        """
        Apply the sequence of cleaning functions in a specific order for other presidents' main texts.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        text = PyCleaningTool.remove_text_between_parenthesis_brackets(text)
        text = PyCleaningTool.replace_special_characters(text)
        text = PyCleaningTool.remove_useless_characters(text)
        text = PyCleaningTool.remove_not_ending_dot(text)
        text = PyCleaningTool.keep_ascii_characters_only(text)
        text = PyCleaningTool.inverse_dot_and_quote(text)
        text = PyCleaningTool.remove_single_quote(text)
        text = PyCleaningTool.insert_space_between_special_word(text)
        text = PyCleaningTool.newline_after_end_of_sentence(text)
        text = PyCleaningTool.many_spaces_to_one_space(text)
        text = PyCleaningTool.strip_every_lines_from_space(text)
        text = PyCleaningTool.many_newlines_to_one_newline(text)
        text = PyCleaningTool.cancel_newline_if_not_end_of_sentence(text)
        text = PyCleaningTool.remove_dot_exclamation_interrogation_alone(text)
        text = PyCleaningTool.space_between_each_word(text)
        return text
    # end apply_cleaning_functions_to_other_presidents_text

# end PyCleaner