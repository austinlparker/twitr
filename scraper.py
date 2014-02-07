import StringIO
import requests
from time import strftime
from bs4 import BeautifulSoup
from printer import print_new_posts

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


    @property
    def scrape_page(self):
        posts = []
        page_content = self.thread.content
        soup = BeautifulSoup(page_content)
        for post in soup.find_all("table", class_="post"):
            post_number = post['data-idx']
            new_token = {
                'author': post.find("dt", class_="author").get_text("", strip=True),
                'body': post.find("td", class_= "postbody").get_text(" ", strip=True),
                'time': strftime('%a, %d %b %Y %H:%M:%S'),
                'postid': post_number
            }
            # print new_token['time']
            # print new_token['author']
            # print new_token['body']
            # print new_token['postid']
            posts.append(new_token)

        return posts


    def scrape_thread(self):
        # next_post = last_post
        thread_url = 'http://forums.somethingawful.com/showthread.php?threadid=' + self.thread +'&goto=newpost'
        self.thread = requests.get(thread_url)
        posts = [self.scrape_page]
        next_post = posts[-1]['postid']

        print_new_posts(posts)
