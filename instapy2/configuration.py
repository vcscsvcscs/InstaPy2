from .helpers import people
from .utilities import comments, follows, media

class Configuration:
    def __init__(self):
        self.comments = comments.CommentsUtility()
        self.follows = follows.FollowUtility()
        self.media = media.MediaUtil()
        self.people = people.PeopleUtility()