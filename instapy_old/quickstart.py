from dotenv import load_dotenv
from instapy2 import InstaPy2
from instapy2 import smart_run
import os

load_dotenv()

# login credentials
insta_username = os.getenv('insta_username')
insta_password = os.getenv('insta_password')

# get an InstaPy2 session!
# set headless_browser=True to run InstaPy2 in the background
session = InstaPy2(username=insta_username, password=insta_password,
                headless_browser=True)

with smart_run(session):
    session.like_by_tags([
        'objectivec',
        'python3'
    ], amount=6)