#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pySpeeches/downloader/PySpeechesMillerCenterImporter.py
# Description : Class to import speeches from the Miller Center web site.
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
import json
from PySpeechesImporter import PySpeechesImporter
from core.cleaning.PyMillerCenterCleaner import PyMillerCenterCleaner
from core.importer.PySpeechesConfig import PySpeechesConfig
from core.dataset.PySpeechesDocument import PySpeechesDocument
from core.downloader.PySpeechesMillerCenterDownloader import PySpeechesMillerCenterDownloader
from dateutil.parser import parse
from datetime import datetime


# Import a directory recursively
class PySpeechesMillerCenterImporter(PySpeechesImporter):

    # Parse date
    def _parse_date(self, str_date):

        # Replace and split
        str_date.str_replace(',', ' ')
        entries = str_date.split(' ')

        # Month
        month = 0
        if entries[0] == "January":
            month = 1
        elif entries[0] == "February":
            month = 2
        elif entries[0] == "March":
            month = 3
        elif entries[0] == "April":
            month = 4
        elif entries[0] == "May":
            month = 5
        elif entries[0] == "June":
            month = 6
        elif entries[0] == "July":
            month = 7
        elif entries[0] == "August":
            month = 8
        elif entries[0] == "September":
            month = 9
        elif entries[0] == "October":
            month = 10
        elif entries[0] == "November":
            month = 11
        elif entries[0] == "December":
            month = 12

        return datetime(int(entries[2]), month, int(entries[1]))
    # end _parse_date

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
        text = PyMillerCenterCleaner.clean_text(text)

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

    # Import the source
    def import_source(self):
        """

        :return:
        """

        # Get speech list
        speeches_list = PySpeechesMillerCenterDownloader.get_speeches_list(self._source.get_entry_point())

        # Corpus
        config = PySpeechesConfig.Instance()
        corpus = config.get_corpus()

        # Download each speech
        for speech in speeches_list:

            # Download speech
            download_speech = PySpeechesMillerCenterDownloader.download_speech(speech)

            # Get title, date, etc
            date = parse(download_speech['date'], dayfirst=False)
            tokens = self.get_tokens(download_speech['transcript'])
            doc_id = corpus.get_max_doc_id() + 1

            # Create author
            author = corpus.add_author(download_speech['president'])

            # New document
            document = PySpeechesDocument(title=download_speech['title'], author=author, date=date,
                                          url=speech['link'], language=self._source.get_language(),
                                          tokens=tokens, doc_id=doc_id, location=download_speech['location'],
                                          video=speech['video'], audio=speech['audio'])

            # Add document
            corpus.add_document(document)

            # Downloading video
            if speech['video']:
                PySpeechesMillerCenterDownloader.download_file(download_speech['video'], config.get_video_directory()
                                                               + "/" + str(doc_id))
            # end if

            # Downloading audio
            if speech['audio']:
                PySpeechesMillerCenterDownloader.download_file(download_speech['audio'], config.get_audio_directory()
                                                               + "/" + str(doc_id))
            # end if
        # end for

    # end import_source

# end PySpeechesMillerCenterDownloader
