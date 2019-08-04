import unittest
from flask_blog import create_app
from flask_blog.models import User

class BaseTestCase(unittest.TestCase):

    def create_app(self):
        app = create_app(TestConfig)
        return app

if __name__ == '__main__':
    unittest.main()