from dotenv import load_dotenv
from instapy2 import InstaPy2

import os

load_dotenv()

session = InstaPy2(username=os.getenv(key='insta_username'), password=os.getenv(key='insta_password'))
session.like_by_tags(tags=['python3'], amount=2)