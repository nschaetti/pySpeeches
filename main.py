#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : main.py
# Description : Main file for argument parsing.
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
import argparse
from pySpeeches.importer import *
from pySpeeches.dataset import *

########################################
# FUNCTIONS
########################################

########################################
# MAIN
########################################

# Main function
if __name__ == "__main__":

    # Argument parser
    parser = argparse.ArgumentParser(description="Political speeches downloader.")

    # Arguments
    parser.add_argument("--config", type=str, help="JSON config file.", default="config.json")
    parser.add_argument("--file",  type=str, help="Output Pickle file to create or update.", required=True)
    parser.add_argument("--action", type=str, help="Action to perform (update, list_doc, list_author_doc, list_author, "
                                                   "change_date).")
    parser.add_argument("--date", type=str, help="Date value (dd/mm/yyyy).", default="")
    parser.add_argument("--doc_id", type=int, help="Target document.", default=-1)
    parser.add_argument("--video", type=str, help="Video directory.", default=".")
    parser.add_argument("--audio", type=str, help="Audio.", default=".")

    # Parse
    args = parser.parse_args()

    # Load configuration file
    config = PySpeechesConfig.Instance()
    config.load(args.config)

    # Create output file if necessary
    if not os.path.exists("./" + args.file):
        corpus = PySpeechesCorpus(name=args.file)
    else:
        print("Loading %s" % args.file)
        corpus = PySpeechesCorpus.load(args.file)
    # end if

    # Set config
    config.set_corpus(corpus)
    config.set_video_directory(args.video)
    config.set_audio_directory(args.audio)

    # Action
    # UPDATE
    if args.action == "update":
        # For each source
        for source in config.get_sources():
            # Source type
            importer = None
            if source.get_type() == "directory":
                importer = PySpeechesDirectoryImporter(source, PySpeechesTextFileImporter)
            elif source.get_type() == "PySpeechesMillerCenterImporter":
                importer = PySpeechesMillerCenterImporter(source)
            # end if

            # Import
            importer.import_source()
        # end for
    # LIST DOCUMENTS
    elif args.action == "list_doc":
        print("> Documents(%s) : " % (corpus.get_document_count()))
        documents = corpus.get_documents()
        for document in documents:
            print(document.get_doc_id(), document.get_title(), document.get_author().get_name(),
                  document.get_date().strftime("%A %d. %B %Y"), document.get_language())
        # end for
    # LIST AUTHOR DOCUMENTS
    elif args.action == "list_author_doc":
        print(">Obama : ")
        obama = corpus.get_author("Barack Obama")
        documents = obama.get_documents()
        for document in documents:
            print(document.get_doc_id(), document.get_title(), document.get_author().get_name(),
                  document.get_date().strftime("%A %d. %B %Y"), document.get_language())
    # LIST AUTHORS
    elif args.action == "list_author":
        print("> Authors(%s) : " % (corpus.get_author_count()))
        authors = corpus.get_authors()
        for author in authors:
            print(author.get_name())
    # CHANGE DATE
    elif args.ac                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        tion == "change_date":
        if args.doc_id != -1 and args.date != "":
            corpus.set_document_date(args.doc_id, datetime.datetime.strptime(args.date, "%d/%m/%Y"))
        else:
            print("Doc ID and date must be set!")
    # end if

    # Print dictionary
    """print("%d documents registered" % corpus.get_size())
    print("%d tokens registered" % corpus.get_n_tokens())
    for k, v in corpus.get_dictionary().get_sorted_list():
        print("%s = %s" % (k, v))
    # end for"""

    # Save
    print("Saving file %s" % args.file)
    corpus.save(args.file)

# endif


