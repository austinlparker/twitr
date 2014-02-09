import StringIO
import requests
from bs4 import BeautifulSoup

class Poster(object):
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

    def make_post(self, message):
        formkeys = self.get_keys()
        post_url = 'http://forums.somethingawful.com/newreply.php'
        data = {
            'action': 'newreply',
            'threadid': self.thread,
            'formkey': formkeys[0],
            'form_cookie': formkeys[1],
            'message': message,
            'parseurl': 'yes',
            'bookmark': 'no',
            'disablesmilies': 'no',
            'signature': 'no',
            'MAX_FILE_SIZE': '2097152',
            'attachment': '',
            'submit': 'Submit Reply'
        }

        print self.session.post(post_url, data)

    def get_keys(self):
        keys = []
        page_content = self.session.get('http://forums.somethingawful.com/newreply.php?action=newreply&threadid='+self.thread)
        soup = BeautifulSoup(page_content.content)
        keys.append(soup.find_all("input", "formkey"))
        keys.append(soup.find_all("input", "form_cookie"))
        return keys
