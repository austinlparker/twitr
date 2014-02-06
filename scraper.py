import StringIO

import requests
from bs4 import BeautifulSoup
from datetime import time


class Scraper(object):
    def __init__(self, username, password, thread):
        self.username = username
        self.password = password
        self.thread = thread

        self.session = requests.Session()
        self.login()

    def login(self):
        login_url = 'https://forums.somethingawful.com/account.php'
        data = {
            'action': 'login',
            'username': self.username,
            'password': self.password,
            'next': '/'
        }

        self.session.post(login_url, data)

    def scrape_page(self, response, *args, **kwargs):
        if response == 200:
            request = BeautifulSoup(open(*args[0]))
            content = request.content
            soup = BeautifulSoup(content)
            for post in soup.find_all('table'):
                innerpost = BeautifulSoup(post)
                new_token = {
                    innerpost.select('author'),
                    innerpost.select('postbody'),
                    time}
                print new_token


    def scrape_thread(self, start_page, threads):
        return

