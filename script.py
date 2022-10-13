from dotenv import load_dotenv
from instapy2.instapy2 import InstaPy2

import os

load_dotenv()

client = InstaPy2(username=os.getenv('insta_username'), password=os.getenv('insta_password'))

"""
    MARK: Configure Commenting
"""
# client.configuration.comments.set_enabled(enabled=True) # enables comments
# client.configuration.comments.set_comments(comments=['WOW {}']) # comments: WOW @username
# client.configuration.comments.set_percentage(percentage=100) # comments on all media

"""
    MARK: Configure Following
"""
# client.configuration.follows.set_enabled(enabled=True) enables following
# client.configuration.follows.set_percentage(percentage=100) # follows all users
# client.configuration.follows.set_times(times=1) # TODO: Add this functionality

"""
    MARK: Media Configuration
"""
#client.media.ignore(hashtags=['ballpythoncommunity', 'javaprogramingmadeeasy']) # ignore skip(hashtags:) entirely if any in caption
#client.media.require(hashtags=['ai', 'objectivec']) # only like if all in caption
#client.media.skip(hashtags=['python3']) # skip if any in caption

# client.configuration.people.skip_friends(usernames=[]) # disables unfollowing for the usernames added
# client.configuration.people.skip_users(usernames=[]) # disables all interaction for the usernames added


"""Functions"""
"""
    MARK: Follow Users By Locations
    NOTE: Use client.configuration.location.get_pk(query=) to get the needed pks.
"""
# pk = client.configuration.location.get_pk(query='Perth, Western Australia') # gets the pk from a location
# client.follow_locations(amount=20, locations=[212940986], randomize_media=True, skip_top=True)

"""
    MARK: Follow Users By Tags
"""
# client.follow_tags(amount=10, tags=['python3'], skip_top=False)

"""
    Follow Users By Usernames
"""
# client.follow_usernames(usernames=[])

"""
    MARK: Like By Tags
"""
# client.like(amount=1, tags=['python3'], randomize_media=True, randomize_tags=True, skip_top=True)

"""
    MARK: Unfollow Users
"""
# client.unfollow_usernames(amount=3)