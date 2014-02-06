import StringIO
from time import strftime

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

    def scrape_page(self):
        page_content = self.thread.content
        soup = BeautifulSoup(page_content)
        post_number = 0
        for post in soup.find_all("table", class_="post"):
            post_number = post['data-idx']
            new_token = {
                'author': post.find("dt", class_="author").get_text("", strip=True),
                'body': post.find("td", class_= "postbody").get_text(" ", strip=True),
                'time': strftime('%a, %d %b %Y %H:%M:%S')
            }
            print new_token['time']
            print new_token['author']
            print new_token['body']





    def scrape_thread(self):
        thread_url = 'http://forums.somethingawful.com/showthread.php?threadid=' + self.thread +'&goto=newpost'
        self.thread = requests.get(thread_url)
        return self.scrape_page()

