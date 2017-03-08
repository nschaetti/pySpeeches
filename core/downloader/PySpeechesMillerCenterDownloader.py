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
import requests
import shutil
import json
from bs4 import BeautifulSoup
import os


# Import a directory recursively
class PySpeechesMillerCenterDownloader(object):

    def __init__(self):
        pass
    # end __init__

    @staticmethod
    def download_file(url, dest):
        """

        :param url:
        :param dest:
        :return:
        """
        if not os.path.exists(dest):
            print("Downloading file %s" % url)
            response = requests.get(url, stream=True)
            with open(dest, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            # end with
        # end if
    # end download_file

    @staticmethod
    def download_speech(speech):

        # Document
        document = dict()

        # Get speech list
        print("Downloading speech from %s" % speech['link'])
        web_page = BeautifulSoup(
            requests.get(speech['link']).text,
            'html.parser'
        )

        # Get transcript
        transcript_element = web_page.find_all('div', {'class': 'transcript-inner'})
        if len(transcript_element) == 0:
            transcript_element = web_page.find_all('div', {'class': 'view-transcript'})
        # end if
        #print(transcript_element)
        #print(len(transcript_element))

        # Transcript
        document['transcript'] = ""
        for p in transcript_element[0].find_all('p'):
            document['transcript'] += " " + p.text
        # end for

        # President's name
        document['president'] = web_page.find_all('p', {'class' : 'president-name'})[0].text

        # Date
        document['date'] = web_page.find_all('p', {'class': 'episode-date'})[0].text

        # Location
        location_element = web_page.find_all('span', {'class': 'speech-loc'})
        if len(location_element) > 0:
            document['location'] = web_page.find_all('span', {'class': 'speech-loc'})[0].text
        else:
            document['location'] = ""
        # end if

        # Abstract
        abstract_element = web_page.find_all('div', {'class': 'about-sidebar--intro'})
        if len(abstract_element) > 0:
            document['abstract'] = web_page.find_all('div', {'class': 'about-sidebar--intro'})[0].text
        else:
            document['abstract'] = ""
        # end if

        # Title
        title = web_page.find_all('h2', {'class': 'presidential-speeches--title'})[0].text
        document['title'] = title[title.index(':')+1:].strip()

        # Video source
        if speech['video']:
            document['video'] = web_page.find_all('div', {'class': 'video-container'})[0].find_all('source')[0]['src']
        # end if

        # Audio
        if speech['audio']:
            document['audio'] = web_page.find_all('a', {'class': 'download-trigger audio'})[0]['href']
        # end if

        return document
    # end download_speech

    @staticmethod
    def parse_speech_list(html_data):
        # List
        speeches_list = []

        # Get speech list
        web_page = BeautifulSoup(
            html_data,
            'html.parser'
        )

        # Each elements
        views_elements = web_page.find_all('div', {'class': 'views-row'})
        for div in views_elements:
            speech_info = dict()
            speech_info['title'] = div.find_all('a')[0].text
            speech_info['link'] = "https://millercenter.org" + div.find_all('a')[0]['href']
            speech_info['video'] = len(div.find_all('span', {'class': 'media-video'})) != 0
            speech_info['audio'] = len(div.find_all('span', {'class': 'media-audio'})) != 0
            speech_info['transcript'] = len(div.find_all('span', {'class': 'media-transcript'})) != 0
            speeches_list.append(speech_info)
        # end for

        return speeches_list
    # end parse_speech_list

    @staticmethod
    def get_speeches_list_ajax(president_id):
        """

        :param president_id:
        :return:
        """

        # HTTPS entry
        speeches_url = "https://millercenter.org/views/ajax?field_president_target_id[" + str(president_id) + "]=" + \
                       str(president_id) + "&_wrapper_format=drupal_ajax"

        # List
        speeches_list = []

        # For each page
        cont = True
        page = 1
        while cont:
            # Form-Data
            form_data = dict()
            form_data['0'] = "43"
            form_data['view_name'] = "presidential_speech"
            form_data['view_display_id'] = "presidential_speech_view_block"
            form_data['view_args'] = ""
            form_data['view_path'] = "%2Fthe-presidency%2Fpresidential-speeches"
            form_data['view_base_path'] = ""
            form_data['view_dom_id'] = "b771133734aa1b2d78f009e795562d37ce7e0c809946f48b0ab48eb738c7d0eb"
            form_data['pager_element'] = "0"
            form_data['field_president_target_id%5B43%5D'] = "43"
            form_data['page'] = str(page)
            form_data['_drupal_ajax'] = "1"
            form_data['ajax_page_state%5Btheme%5D'] = "miller"
            form_data['ajax_page_state%5Btheme_token%5D'] = ""
            form_data['ajax_page_state%5Blibraries%5D'] = "better_exposed_filters%2Fdatepickers%2Cbetter_exposed_" \
                                                          "filters%2Fgeneral%2Ccore%2Fhtml5shiv%2Ccore%2Fjquery.ui." \
                                                          "datepicker%2Ccore%2Fpicturefill%2Cextlink%2Fdrupal.extlink%2C" \
                                                          "google_analytics%2Fgoogle_analytics%2Cmiller%2Fableplayer%2C" \
                                                          "miller%2Fformstone%2Cmiller%2Fglobal-styling%2Cmiller%2F" \
                                                          "swiper%2Csharethis%2Fsharethis%2Csharethis%2Fsharethispicker" \
                                                          "externalbuttons%2Csharethis%2Fsharethispickerexternalbuttonsws" \
                                                          "%2Csystem%2Fbase%2Cviews%2Fviews.ajax%2Cviews%2Fviews.module" \
                                                          "%2Cviews_infinite_scroll%2Fviews-infinite-scroll"

            # Headers
            headers = dict()
            headers['Accept'] = "application/json, text/javascript, */*; q=0.01"
            headers['Origin'] = "https://millercenter.org"
            headers['X-Requested-With'] = "XMLHttpRequest"
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                                    "Chrome/56.0.2924.87 Safari/537.36"
            headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
            headers['Referer'] = "https://millercenter.org/the-presidency/presidential-speeches?" \
                                 "field_president_target_id[" + str(president_id) + "]=" + str(president_id)
            headers['Accept-Encoding'] = "gzip, deflate, br"
            headers['Accept-Language'] = "en-US,en;q=0.8,et;q=0.6,fr;q=0.4"

            # Get data
            result = requests.post(url=speeches_url, data=form_data, headers=headers)

            # Parse JSON
            json_data = json.loads(result.text)

            # Get HTML data
            if 'data' not in json_data[-1]:
                print(json_data)
            # end if
            html_data = json_data[-1]['data']

            # Get speech list
            speeches = PySpeechesMillerCenterDownloader.parse_speech_list(html_data=html_data)
            if len(speeches) > 0:
                speeches_list += speeches
            else:
                cont = False

            # Next page
            page += 1

        # end while

        return speeches_list
    # end get_speeches_list_ajax

    @staticmethod
    def get_speeches_list_main(president_id):
        """

        :param president_id:
        :return:
        """

        # HTTPS entry
        speeches_url = "https://millercenter.org/the-presidency/presidential-speeches?field_president_target_id[" + \
                       str(president_id) + "]=" + str(president_id)

        # List
        speeches_list = []

        # Get data
        result = requests.get(url=speeches_url)

        # Get speech list
        speeches_list += PySpeechesMillerCenterDownloader.parse_speech_list(html_data=result.text)

        return speeches_list
    # end get_speeches_list_main

    @staticmethod
    def get_speeches_list(president_id):
        speeches_list = PySpeechesMillerCenterDownloader.get_speeches_list_ajax(president_id)
        speeches_list += PySpeechesMillerCenterDownloader.get_speeches_list_main(president_id)
        return speeches_list
    # end get_speeches_list

# end PySpeechesMillerCenterDownloader
