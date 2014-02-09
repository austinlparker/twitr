import StringIO
import requests
from time import strftime
from bs4 import BeautifulSoup
from printer import print_new_posts

class Scraper(object):
    def __init__(self, username, password, thread, posts):
        self.username = username
        self.password = password
        self.thread = thread
        self.posts = posts

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
            if new_token['author'] == "Adbot":
                continue
            else:
                self.posts.append(new_token)


    def scrape_thread(self):
        # next_post = last_post
        thread_url = 'http://forums.somethingawful.com/showthread.php?threadid=' + self.thread +'&goto=newpost'
        self.thread = requests.get(thread_url)
        self.scrape_page()


        print_new_posts(self.posts)
