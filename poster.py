import StringIO
import requests

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
        post_url = 'http://forums.somethingawful.com/newreply.php'
        data = {
            'action': 'newreply',
            'threadid': self.thread,
            'message': message,
            'next': '/'
        }

        self.session.post(post_url, data)
