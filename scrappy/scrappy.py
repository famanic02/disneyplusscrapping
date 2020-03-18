from user_agent_rotator import UserAgentRotator

import requests


class Scrappy:
    """
    Scrappy class use for creating and handling the session or cookies for request object.
    During initializing the Scrapy object a random user-agent set in request object.
    """

    session = None
    url = None
    user_agent = None

    def __init__(self, url=None, headers=None):
        self.url = url  # set url

        # create userAgentRotator object
        self.user_agent_rotator = UserAgentRotator()

        # set random user-agent
        self.user_agent = self.get_user_agent()

        self.headers = headers if headers else {}  # set headers
        self.session = requests.session()  # create request session

    def get_user_agent(self):

        """ Method return the dynamic user-agent """
        return self.user_agent_rotator.get_user_agent()

    def set_url(self, url):

        """ Method set the headers """
        self.url = url

    def set_headers(self, **args):

        """ Method set the headers """
        self.headers = args

    def update_headers(self, **args):

        """ Method update the headers"""
        for key, val in args.items():
            self.headers[key] = val

    def get_request(self, params=None, update_user_agent=False):

        """ handle the get request of the requests object by setting the headers and url """

        # get user-agent
        user_agent_headers = {"User-Agent": self.get_user_agent() if update_user_agent else self.user_agent}

        # update headers
        self.update_headers(**user_agent_headers)

        return self.session.get(self.url, params=params, headers=self.headers, cookies=self.session.cookies)

    def post_request(self, data, update_user_agent=False):

        """ handle the post request of the requests object by setting the headers, params and url """

        # get user-agent
        user_agent_headers = {"User-Agent": self.get_user_agent() if update_user_agent else self.user_agent}

        # update headers
        self.update_headers(**user_agent_headers)

        return self.session.post(self.url, data=data, headers=self.headers, cookies=self.session.cookies)


class ScrapeProcess:
    """
        ScrapeProcess, initialize the Scrappy object and process each pages and return its response.

        For processing the pages its use same Scrappy object to maintain the session and cookies.
        During initializing the ScrapeProcess object its accept 'site_pages' (dictionary).
    """
    def __init__(self):

        """ Create Scrapy Object and set 'site_pages' and current_page """

        self.scrappy = self.createScrapyObject()  # create Scrappy Object
        self.method = 'get'

    def createScrapyObject(self):

        """ Create and Return the Scrappy Object"""
        return Scrappy()

    def configureScrapyObject(self, obj):

        """ Configured the Scrappy objects by given 'site_pages' value."""

        if ('url' in obj) and obj["url"] and ('method' in obj) and (obj["method"].lower() in ["get", "post"]):
            self.scrappy.set_url(obj["url"])

            self.method = obj["method"].lower()

            if ("headers" in obj) and obj['headers']:
                self.scrappy.set_headers(**obj['headers'])

