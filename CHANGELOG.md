# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Released]

## [0.0.1.2] - 2022-09-27
### Added
- Implemented most features of *like_by_tags*.
    - *like_by_tags* will now comment on and like posts based on the configuration set by you, the user (see [script.py](script.py)).

### Changed
- Improved the way InstaPy2 checks for hashtags, phrases or words within the caption text of media.

### TODO
- Clean up the code and move features into their respective *_util.py files.
- Add the ability to unlike once likes, etc. from InstaPy.
- Add 

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