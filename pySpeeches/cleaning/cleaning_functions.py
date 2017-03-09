#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# File : core/cleaning/__init__.py
# Description : Init file for cleaning functions.
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

from __future__ import unicode_literals
import re
import unicodedata

#
# List of contractions to replace in the texts.
#
LIST_OF_CONTRACTIONS = [
    ("I'm", "I am"), ("(there|they|we|what|who|you)'re", "\g<1> are"),
    ("(could|I|might|must|should|they|we|what|who|would|you)'ve", "\g<1> have"),
    ("(he|here|how|it|she|that|there|what|when|where|who)'s", "\g<1> is"),
    ("(are|could|did|do|does|had|has|have|is|might|must|need|ought|should|was|were|would)n't", "\g<1> not"),
    ("ain't", "is not"), ("can't", "cannot"), ("shan't", "shall not"), ("won't", "will not"),
    ("(he|how|I|it|nobody|she|that|there|they|we|what|when|where|who|why|you)'ll", "\g<1> will"),
    ("(he|how|I|it|nobody|she|that|there|they|we|what|when|where|who|why|you)'d", "\g<1> would"),
    ("a'ight", "all right"), ("'em", "them"), ("'er", "her"), ("ma'am", "madam"),
    ("'nother", "another"), ("let's", "let us"), ("o'clock", "of the clock"),
    ("rock'n'roll", "rock and roll"), ("'round", "around"), ("y'all", "you all")
]

#
# List of abbreviations with dots to replace.
#
LIST_OF_ABBREVIATIONS = [
    ('Mr.', 'Mr'), ('Ms.', 'Ms'), ('Mrs.', 'Mrs'), ('Ph.D.', 'PhD'),
    ('Ph.D', 'PhD'), ('Dr.', 'Dr'), ('Jr.', 'Jr'), ('Lt.', 'Lt'),
    ('St.', 'St'), ('a.m.', 'am'), ('p.m.', 'pm'),
    ('a.k.a.', 'aka'), ('a.k.a', 'aka'), ('Corp.', 'Corp'), ('e.g.', 'eg'),
    ('etc.', 'etc'), ('i.e.', 'ie'), ('i.e', 'ie'), ('vs.', 'vs')
]

#
# Regex for month abbreviations
#
ABBREVIATIONS_MONTH_PATTERN = '(Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.'

#
# Regex for months
#
MONTHS_PATTERN = '(january|february|march|april|may|june|july|august|september|october|november|december)'

#
# Regex for days
#
DAYS_PATTERN = '[adefhimnorstuw]{3,6}day'

#
# Before time patterns (for the White House website).
#
BEFORE_START_TIME_PATTERN = '^((?!\sEND\s).)*\n\d{1,2}:\d{2} [AP]\.M\. (\(([A-Z]+|(l|L)ocal)\)|[A-Z]+)'

#
# End time patterns (for the White House website).
#
AFTER_END_TIME_PATTERN = '\s((END\s|# ?#).*?$|END$)'

#
# Other start pattern 1
#
BEFORE_START_1_PATTERN = '^.*(' + \
    '\nremarks (by|of)|' + \
    'as prepared for delivery|' + \
    'below (is|are)|' + \
    '(\n| {5,})(' + DAYS_PATTERN + '[ ,]*)?' + MONTHS_PATTERN + ' *\d{1,2}(th)?[ ,]*20\d\d' + \
    ')[^\n]*\n+([^\n]{1,20}\n)?'

#
# Other start pattern 2
#
BEFORE_START_2_PATTERN = '^.*\nWashington[, ]+D\.?C\.?\n+([^\n]{1,20}\n)?'

#
# Title "interview" pattern
#
INTERVIEW_PATTERN = 'interview|question|answer|q ?& ?a'

#
# Regex patterns when multiple speakers
#
OBAMA_PATTERN = '(THE PRESIDENT|PRESIDENT OBAMA|POTUS):'
Q_PATTERN = '\nQ[ :]'

#
# Englobe also Obama and a simple question
#
OTHER_PATTERN = "(([A-Z.'\- ]|Mc)+:|\nQ )"

#
# Regex for URL
#
URL_PATTERN = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"


# Utility function
class PyCleaningTool:

    # Constructor
    def __init__(self):
        """
        Constructor
        """
        pass
    # end __init__

    # Text cleaning functions
    @staticmethod
    def remove_informations(text):
        """
        Remove the informations at before and after the speech.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        # Remove the first time pattern (e.g. 12:38 A.M. EST) and what precedes
        text = re.sub(BEFORE_START_TIME_PATTERN, '\n', text, flags=re.S)
        # Remove the final END... or ##...
        text = re.sub(AFTER_END_TIME_PATTERN, '\n', text, flags=re.S)
        # Remove start pattern 1 and what precedes
        text = re.sub(BEFORE_START_1_PATTERN, '\n', text, flags=re.S | re.I)
        # Remove start pattern 2 and what precedes
        text = re.sub(BEFORE_START_2_PATTERN, '\n', text, flags=re.S | re.I)
        return text
    # end remove_informations

    # Remove text between parenthesis brackets
    @staticmethod
    def remove_text_between_parenthesis_brackets(text):
        """
        Remove all the texts between parenthesis or brackets as they are not real speech.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        return re.sub('\(.*?\)|\[.*?\]|{.*?}', ' ', text, flags=re.S)
    # end remove_text_between_parenthesis_brackets

    # Replace special characters
    @staticmethod
    def replace_special_characters(text):
        """
        Replace special US characters found by common ones.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        return text.replace('–', '-').replace('—', '-').replace('‘', "'") \
            .replace('’', "'").replace('“', '"').replace('”', '"') \
            .replace('…', '...').replace('½', ' ').replace('¼', ' ') \
            .replace('¾', ' ').replace('¬', ' ').replace('&', 'and')
    # end replace_special_characters

    # Remove useless characters
    @staticmethod
    def remove_useless_characters(text):
        """
        Remove unuseful characters.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        return text.replace('-', ' ').replace('...', ' ').replace('*', ' ') \
            .replace('/', ' ').replace('+', ' ').replace('\\', ' ')
    # end remove_useless_characters

    # Remove no ending dot
    @staticmethod
    def remove_not_ending_dot(text):
        """
        Remove all the dots that don't mark end of sentences.
        :param text: Text to clean.
        :return: Cleaned text.
        """

        # Remove all the dots from the list of given abbreviations
        for ab1, ab2 in LIST_OF_ABBREVIATIONS:
            text = text.replace(ab1, ab2)
        text = re.sub(ABBREVIATIONS_MONTH_PATTERN + ' (\d)', '\g<1> \g<2>', text)

        # Remove dot from websites (.com, .gov, .org, .us, www.)
        text = text.replace('.com', 'com').replace('.gov', 'gov') \
            .replace('.org', 'org').replace('.us', 'us').replace('www.', 'www')

        # Remove dot from initiales such as U.S.A(.), Washington D.C(.), B.o.B.,
        # or John F. Kennedy
        # For 3 letters (U.S.A. or U.S.A)
        text = re.sub(
            '([A-Za-z])\.([A-Za-z])\.([A-Za-z])\.?', '\g<1>\g<2>\g<3>', text)
        # For 2 letters (U.S.)
        text = re.sub('([A-Za-z])\.([A-Za-z])\.', '\g<1>\g<2>', text)
        # With one or two initial some typos can match (e.g. "... done.All ...")
        # So need to match either "\s", "-" or "'" before first initial when
        # one dot only
        # For 1 and 2 letters (F. or U.S). We don't consider the "I"
        text = re.sub("([\s])([A-FJ-Za-z])\.", '\g<1>\g<2>', text)

        # Remove dots or comma from float numbers
        text = re.sub('(\d+)(\.|,)(\d+)', '\g<1>\g<3>', text)
        return text
    # end remove_not_ending_dot

    # Keep ASCII characters only
    @staticmethod
    def keep_ascii_characters_only(text):
        """
        Keep only ASCII characters, that mean's diacritics are removed from letters and remaining special characters are
        removed.
        :param text: Text to clean
        :return: Cleaned text.
        """
        return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').encode('utf-8')
    # end keep_ascii_characters_only

    # Inverse dot and quote
    @staticmethod
    def inverse_dot_and_quote(text):
        """
        Inverse all couples [.!?,;:]" as "[.!?], because [.!?,;:] need to be the last element of a (sub)sentence.
        :param text:
        :return:
        """
        return re.sub('([.!?,;:])("|\')', '\g<2>\g<1>', text)
    # end inverse_dot_and_quote

    # Remove single quote
    @staticmethod
    def remove_single_quote(text):
        """
        Remove the single quote when contractions and useless
        :param text:
        :return:
        """
        for cont, full in LIST_OF_CONTRACTIONS:
            text = re.sub(cont, full, text, flags=re.I)

        # Remove quote between numbers (e.g. 10'000)
        text = re.sub("(\d)'(\d)", '\g<1>\g<2>', text)

        # Remove quote before numbers (e.g. '90s) or words ('Bama)
        text = re.sub("(\W)'(\w)", '\g<1>\g<2>', text)

        # Remove quote and 's' letter from year (e.g. 70's), possessive
        # (e.g. Paul's) and add a space
        text = re.sub("(\w)'(s)(\W)", '\g<1> \'s \g<3>', text)

        # Remove quote from plural possessive (e.g. guys') or after numbers/nouns
        text = re.sub("(\w)'(\W)", '\g<1> \'s \g<2>', text)

        return text
    # end remove_single_quote

    # Replace sharp hashtag
    @staticmethod
    def replace_sharp_hashtag(text):
        """
        Replace the sharp before a number as "number" and the sharp before combinations of letter and digit by "hashtag.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        text = re.sub("(\W)#(\d+)", '\g<1> number \g<2>', text)
        text = re.sub("(\W)#(\w+)", '\g<1> hashtag \g<2>', text)
        return text
    # end replace_sharp_hashtag

    # Get next speaker
    @staticmethod
    def get_next_speaker(text):
        """
        Get the next speaker (between Obama, a question and a named person) and and the index of match in the given
        text. The return object is a dictionary {'name': speaker, 'start': start_index, 'end': end_index}.
        :param text: Text to clean.
        :return: Dictionary {'name': speaker, 'start': start_index, 'end': end_index}
        """
        dictionary = {'name': '', 'start': float('inf'), 'end': 0}
        # Get the indexes of match of the next speech made by Obama
        match_obama = re.search(
            '(' + OBAMA_PATTERN + '.*?)' +
            '(?=(' + OTHER_PATTERN + '|$))', text, flags=re.S)
        if match_obama:
            dictionary['name'] = 'obama'
            dictionary['start'] = match_obama.start()
            dictionary['end'] = match_obama.end()
        # Get the indexes of match of the next question
        match_q = re.search(
            '(' + Q_PATTERN + '.*?)' +
            '(?=(' + OTHER_PATTERN + '|$))', text, flags=re.S)
        if match_q and match_q.start() < dictionary['start']:
            dictionary['name'] = 'q'
            dictionary['start'] = match_q.start()
            dictionary['end'] = match_q.end()
        # Get the indexes of match of the next speaker
        match_other = re.search(
            '(' + OTHER_PATTERN + '.*?)' +
            '(?=(' + OTHER_PATTERN + '|$))', text, flags=re.S)
        if match_other and match_other.start() < dictionary['start']:
            dictionary['name'] = 'other'
            dictionary['start'] = match_other.start()
            dictionary['end'] = match_other.end()

        return dictionary
    # end get_next_speaker

    # Split oral from written
    @staticmethod
    def split_oral_from_written(title, text):
        """
        Given the text (and the title), split the text as an oral and a written speech.
        :param title: Text's title.
        :param text: Text to clean.
        :return: Dictionary of the form {'written': written_message, 'oral': oral_speech}.
        """
        # Initialize the two types of text (written message and oral speech)
        written_message = ''
        oral_speech = ''

        # First test if there is not mutiple speakers
        sp = PyCleaningTool.get_next_speaker(text)
        if not sp['name']:
            return {'written': text, 'oral': ''}
        if sp['start'] > 3:
            print('Name: %s, Start: %s, Text: %s' % (sp['name'], sp['start'], text[sp['start']:sp['start']+20]))
        # Secondly, extract all Obama's preview speeches, if he begins to speak
        # Note that the preview speeches of Obama is considered as written speech
        while sp['name'] == 'obama':
            # Add to written speech the obama's speech without his name
            written_message = written_message + \
                re.sub(OBAMA_PATTERN, '', text[sp['start']:sp['end']]) + '\n'
            # Remove from the text the speech added in written speech
            text = '\n' + text[sp['end']:]
            # Get next speaker
            sp = PyCleaningTool.get_next_speaker(text)

        # Then, check if the pattern interview is in the title
        if re.search(INTERVIEW_PATTERN, title, flags=re.I):
            # If yes, we are in presence of an interview
            int_bool = True
        else:
            # Otherwise, we are in presence of written speech
            int_bool = False

        # ok = ''
        # While we have some speakers
        while sp['name']:
            # Test if next speaker is Obama
            # print int_bool
            # print ok
            # print text[sp['start']:sp['end']]
            # if ok != 'ok':
            #     ok = raw_input("")
            if sp['name'] == 'obama':
                # If we are in presence of an interview or questions, we put all
                # Obama's text in oral_speech, otherwise in written_message
                if int_bool:
                    # Add to oral speech
                    oral_speech = oral_speech + \
                        re.sub(OBAMA_PATTERN, '', text[sp['start']:sp['end']]) + '\n'
                else:
                    # Add to written speech
                    written_message = written_message + \
                        re.sub(OBAMA_PATTERN, '', text[sp['start']:sp['end']]) + '\n'
                # Remove speech from text
                text = '\n' + text[sp['end']:]
            # Test if next speaker is a question or another person speaking
            else:
                # Remove speech from text
                text = '\n' + text[sp['end']:]
                # All speeches of Obama after the period of questions are
                # considered as oral, even if for e.g. another president
                # speaks before him
                if not int_bool and sp['name'] == 'q':
                    int_bool = True

            # Get next speaker
            sp = PyCleaningTool.get_next_speaker(text)

        # Return written_message, oral_speech
        # print(chr(27) + "[2J")
        return {'written': written_message, 'oral': oral_speech}
    # split_oral_from_written

    # Insert space between special word
    @staticmethod
    def insert_space_between_special_word(text):
        """
        Insert a space when a word contains some special characters (%, ").
        :param text: Text to clean.
        :return: Cleaned text.
        """
        text = re.sub('(\d)(%|\$)', '\g<1> \g<2>', text)
        text = re.sub('(%|\$)(\d)', '\g<1> \g<2>', text)
        text = re.sub('([^\s])("|&)', '\g<1> \g<2>', text)
        text = re.sub('("|&)([^\s])', '\g<1> \g<2>', text)
        return text
    # end insert_space_between_special_word

    # Insert a new line after the end of a sentence.
    @staticmethod
    def newline_after_end_of_sentence(text):
        """
        After each end of sentence (given by '.', '?' or '!') maybe followed by a double quote, add a newline.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        return re.sub('([.?!])', '\g<1>\n', text)
    # end newline_after_end_of_sentence

    # Replace many spaces by one space
    @staticmethod
    def many_spaces_to_one_space(text):
        """
        Reduce many successive spaces to one space.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        return re.sub('[ \t]+', ' ', text)
    # end many_spaces_to_one_space

    # Strip every lines from spaces
    @staticmethod
    def strip_every_lines_from_space(text):
        """
        Remove each space at the beginning or the end of a line.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        text = re.sub(' \n|\n ', '\n', text)
        text = text.strip()
        return text
    # end strip_every_lines_from_space

    # Strip lines
    @staticmethod
    def strip_lines(text):
        """
        Remove each space at the beginning or the end of a line.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        cleaned = ""
        lines = text.split('\n')
        for line in lines:
            cleaned += line.strip() + '\n'
        return cleaned
    # end strip_lines

    # Many new lines to one new line
    @staticmethod
    def many_newlines_to_one_newline(text):
        """
        Reduce many successive newlines to one newline.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        return re.sub('(\n){2,}', '\n', text)
    # end many_newlines_to_one_newline

    # Cancel new line if it is not the end of the sentence
    @staticmethod
    def cancel_newline_if_not_end_of_sentence(text):
        """
        Remove the newline and add space if we are not at the end of a sentence.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        return re.sub('([^.?!])\n', '\g<1> ', text)
    # end cancel_newline_if_not_end_of_sentence

    # Remove alone exclamation and interrogation dots
    @staticmethod
    def remove_dot_exclamation_interrogation_alone(text):
        """
        Remove '.', '?' or '!', if they are alone on one line.
        :param text: Text to clean.
        :return: Cleaned text.
        """
        return text.replace('\n.', '').replace('\n!', '').replace('\n?', '')
    # end remove_dot_exclamation_interrogation_alone

    # Space between each word
    @staticmethod
    def space_between_each_word(text):
        """
        Add a space between each word ("test", "cyber-attack", "I'm" or [.?!,:;] are considered as word)
        :param text: Text to clean.
        :return: Cleaned text.
        """
        text = re.sub("([\w\-']+)([.?!,:;])", '\g<1> \g<2>', text)
        text = re.sub("([.?!,:;])([\w\-']+)", '\g<1> \g<2>', text)
        return text
    # end space_between_each_word

    # Remove URLs
    @staticmethod
    def remove_urls(text):
        """
        Remove URLs
        :param text: Text to clean
        :return: Cleaned text.
        """
        text = re.sub(URL_PATTERN, "", text)
        return text
    # end remove_urls

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

# end PyCleaningTool

