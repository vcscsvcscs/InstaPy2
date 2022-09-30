# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Released]

## [0.0.15] - 2022-09-30
### Added
- Added basic *like_by_users* functionality with support for following.

### Changed
- Modified some existing code to use Union allowing for multiple types within a single parameter.

## [0.0.14] - 2022-09-29
### Added
- Added support for *set_can_follow*.
    - Users can now set whether the bot will follow a user.
        - Configure this option with both *set_can_follow* and *set_friends_to_skip*.

### Changed
- Changed version number to conform with Semantic Versioning (x.y.z, not w.x.y.z).

## [0.0.1.3] - 2022-09-28
### Added
- Added support for *comment_on_liked_media*.
    - Setting *comment_on_liked_media* to *True* will enable commenting for currently parsed and liked media.
    - Media that is not liked will not receive a comment.
        - This will be improved so users can comment on unliked media at a later date.

### Changed
- Created a better *media_passes_all_checks* function to check whether media can be interacted with.
- Moved some functions from [instapy2.py](instapy2.py) to their respective *_util.py files.
    - [comment_util.py](comment_util.py), [like_util.py](like_util.py), etc.
- Changed *media_contains_mandatory_\** from *any()* to *all()*.
    - This change was made to correspond with how InstaPy handles the same check.

### Fixed
- Fixed an issue caused by commenting out the comment and like code.
    - InstaPy2 will now **ACTUALLY** comment and like media based on user configuration.

## [0.0.1.2] - 2022-09-27
### Added
- Implemented most features of *like_by_tags*.
    - *like_by_tags* will now comment on and like media based on the configuration set by you, the user (see [script.py](script.py)).

### Changed
- Improved the way InstaPy2 checks for hashtags, phrases or words within the caption text of media.

### TODO
- Clean up the code and move features into their respective *_util.py files.
- Add the ability to unlike once likes, etc. from InstaPy.

## [0.0.1.1] - 2022-09-27
### Added
- Added basic *like_by_tags* functionality with support for skipping media containing hashtags or phrases.
    - Users can also limit likes to media with a current like count between a given range (only like if media currently has between 0-100 likes).
- Added Pillow requirement to [requirements.txt](requirements.txt)

## [0.0.1] - 2022-09-26
### Added
- Added *like_by_tags* with **very** limited functionality.
    - *like_by_tags* only retrieves media at the moment and does not actually interact with said media.

### Changed
- Changed from Selenium to [Instagrapi](https://github.com/adw0rd/instagrapi).

### Removed
- Removed old InstaPy code in favour of InstaPy2's.

## [0.6.19] - 2022-09-23
No functional changes were made to 0.6.19.