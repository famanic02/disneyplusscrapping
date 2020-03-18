from scrappy.scrappy import ScrapeProcess
from request_pages import DisneyPages
from requests.exceptions import HTTPError, TooManyRedirects, Timeout, RequestException
from contants import credentials

import json


class DisneyPlusScrape(ScrapeProcess):

    def __init__(self):

        """ Create Scrapy Object and set 'site_pages' and current_page """

        super(DisneyPlusScrape, self).__init__()

    def __getPageResponse(self, data=None, params=None, updateUserAgent=False):

        """ Return the current page response. """

        if self.method == 'get':
            return self.scrappy.get_request(params=params, update_user_agent=updateUserAgent)

        elif self.method == 'post':
            return self.scrappy.post_request(data=data, update_user_agent=updateUserAgent)

    def getPageResponse(self, data=None, params=None, updateUserAgent=False):
        """ Handled the Server Errors and Return the current page response."""
        try:
            return self.__getPageResponse(data=data, params=params, updateUserAgent=updateUserAgent)
        except Timeout as err:
            print("Timeout Error:", err)

        except TooManyRedirects as err:
            print("Too many redirect")

        except RequestException as err:
            print("OOps: Something Else", err)
        except Exception as err:
            print("Interval server error", err)

    def _getAssertionKey(self):
        """ return the Assertion key that is used for generating the token """

        assertionPage = DisneyPages['getAssertionKey']
        data = '{"deviceFamily":"browser","applicationRuntime":"' + \
               self.scrappy.user_agent_rotator.random_user_agent['browser'] + '","deviceProfile":"macosx","attributes":{}}'
        self.configureScrapyObject(assertionPage)
        resp = self.getPageResponse(data=data)
        return resp.json()

    def _getToken(self):
        """ return the Token key """

        resp = self._getAssertionKey()
        tokenPage = DisneyPages['getToken']
        data = {
            'grant_type': 'urn:ietf:params:oauth:grant-type:token-exchange',
            'latitude': '0',
            'longitude': '0',
            'platform': 'browser',
            'subject_token': resp['assertion'],
            'subject_token_type': 'urn:bamtech:params:oauth:token-type:device'
        }
        self.configureScrapyObject(tokenPage)
        resp = self.getPageResponse(data=data)
        return resp.json()

    def _login(self):
        """ Login the user by using the credentials and return the access token """

        resp = self._getToken()
        self.accessToken = resp['access_token']  # set the accessToken
        loginPage = DisneyPages['login']
        data = '{"email": "' + credentials['email'] + '", "password": "' + credentials['password'] + '"}'
        headers = {"authorization": 'Bearer {access_token}'.format(access_token=self.accessToken)}
        self.configureScrapyObject(loginPage)
        self.scrappy.update_headers(**headers)  # updated headers (add authorization)
        resp = self.getPageResponse(data=data)
        return resp.json()

    def _grant(self):
        """ Validate the Access Token and generate a new assertion key"""

        resp = self._login()
        grantPage = DisneyPages['grant']
        data = '{"id_token":"' + resp['id_token'] + '"}'
        headers = {"authorization": 'Bearer {access_token}'.format(access_token=self.accessToken)}
        self.configureScrapyObject(grantPage)
        self.scrappy.update_headers(**headers)  # updated headers (add authorization)
        resp = self.getPageResponse(data=data)
        return resp.json()

    def _newAssertionKey(self):
        """ Validate the new assertion Token and generate a new Access key"""

        resp = self._grant()
        grantPage = DisneyPages['newToken']
        data = {
            'grant_type': 'urn:ietf:params:oauth:grant-type:token-exchange',
            'latitude': '0',
            'longitude': '0',
            'platform': 'browser',
            'subject_token': resp['assertion'],
            'subject_token_type': 'urn:bamtech:params:oauth:token-type:account'
        }
        self.configureScrapyObject(grantPage)
        resp = self.getPageResponse(data=data)
        return resp.json()

    def _getCollection(self):
        """ Return the dictionary that contain the information about each section of homepage"""
        resp = self._newAssertionKey()

        self.accessToken = resp['access_token']
        collectionSetPage = DisneyPages['collectionSet']
        params = (
            ('variables',
             '{"preferredLanguage":["en"],"contentClass":"home","slug":"home",'
             '"contentTransactionId":"8d32d56f-c127-4021-9ebb-0f7a32ef8c91"}'),
        )
        self.configureScrapyObject(collectionSetPage)
        headers = {"authorization": 'Bearer {access_token}'.format(access_token=self.accessToken)}
        self.scrappy.update_headers(**headers)  # updated headers (add authorization)
        resp = self.getPageResponse(params=params)
        return resp.json()

    def _getSectionData(self, params):
        """ Return the each section information """
        sectionPage = DisneyPages['section']

        self.configureScrapyObject(sectionPage)
        headers = {"authorization": 'Bearer {access_token}'.format(access_token=self.accessToken)}
        self.scrappy.update_headers(**headers)  # updated headers (add authorization)
        resp = self.getPageResponse(params=params)
        return resp.json()

    @staticmethod
    def __getTitle(containig_list):
        for text in containig_list:
            if text['field'] == 'title' and text['type'] == 'full':
                return text['content']
        return ""

    def __getSectionItem(self, items):
        """ Return the Items """

        display_items = []
        for item in items:
            display_item = {
                'Name': self.__getTitle(item['texts']),
                'URL':  item['playbackUrls'] if 'playbackUrls' in item else [],
                'Images': item['images'][0] if len(item['images']) > 0 else [],
            }
            display_items.append(display_item)
        return display_items

    def getData(self):
        resp = self._getCollection()

        containers = resp['data']['CollectionBySlug']['containers']
        data = []
        for container in containers:
            section = {}
            if "items" in container['set']:
                section['Name'] = self.__getTitle(container['set']['texts'])
                section['Items'] = self.__getSectionItem(container['set']['items'])
            else:
                param_dict = {
                    "preferredLanguage": ["en"],
                    "setId": container['set']['refId'],
                    "setType": container['set']['refType'],
                    "contentTransactionId": "8d32d56f-c127-4021-9ebb-0f7a32ef8c91"
                }
                if 'ContinueWatchingSet' == container['set']['refType']:
                    param_dict['lastBookmark'] = None

                params = (
                    ('variables', json.dumps(param_dict)),
                )

                item_resp = self._getSectionData(params=params)
                section['Name'] = self.__getTitle(item_resp['data']['SetBySetId']['texts'])
                section['Items'] = self.__getSectionItem(item_resp['data']['SetBySetId']['items'])
            data.append(section)
        return data
