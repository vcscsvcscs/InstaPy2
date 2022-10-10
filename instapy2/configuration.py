from .helpers import location, people
from .utilities import comments, follows, media

from instagrapi import Client

class Configuration:
    def __init__(self, session: Client):
        self.comments = comments.CommentsUtility()
        self.follows = follows.FollowUtility()
        self.media = media.MediaUtil()

        self.location = location.LocationHelper(session=session)
        self.people = people.PeopleHelper()