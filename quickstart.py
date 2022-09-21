from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''
insta_password = ''

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username, password=insta_password)

with smart_run(session):
    session.like_by_tags([
        'objectivec',
        'python3'
    ], amount=10)