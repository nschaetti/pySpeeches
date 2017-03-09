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
from core.cleaning.cleaning_functions import PyCleaningTool
from core.cleaning.PyCleaner import PyCleaner


# An Author
class PyMillerCenterCleaner(PyCleaner):

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
        text = PyCleaningTool.replace_special_characters(text)                  # Remove special characters.
        text = PyCleaningTool.remove_useless_characters(text)                   # Remove useless characters.
        text = PyCleaningTool.remove_text_between_parenthesis_brackets(text)    # No text between parentheses.
        text = PyCleaningTool.remove_not_ending_dot(text)                       # Remove not ending dot.
        text = PyCleaningTool.keep_ascii_characters_only(text)                  # Keep only ASCII characters.
        text = PyCleaningTool.inverse_dot_and_quote(text)                       # Inverse dot and quote.
        text = PyCleaningTool.remove_single_quote(text)                         # Remove single dot when contraction is useless.
        text = PyCleaningTool.replace_sharp_hashtag(text)                       # Remove hashtags.
        text = PyCleaningTool.insert_space_between_special_word(text)           # Insert space between special words.
        text = PyCleaningTool.newline_after_end_of_sentence(text)               # A new line after the end of a sentence.
        text = PyCleaningTool.many_spaces_to_one_space(text)                    # No multiple spaces
        text = PyCleaningTool.strip_lines(text)                                 # No space at the beginning or at the end of a line.
        text = PyCleaningTool.many_newlines_to_one_newline(text)                # No multiple new lines.
        text = PyCleaningTool.cancel_newline_if_not_end_of_sentence(text)       # Remove new line if not at the end of a sentence.
        text = PyCleaningTool.remove_dot_exclamation_interrogation_alone(text)  # Remove excl and inter. dot if alone.
        text = PyCleaningTool.space_between_each_word(text)                     # We want a space between each words.
        return text
    # end clean_text

# end PyMillerCenterCleaner