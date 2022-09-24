# Research

## explore_tags.json
This file contains the JSON response for the [/explore/tags/python3](https://instagram.com/explore/tags/python3) request.  

### Notes
1. Recent
    - Instagram no longer shows Recent posts alongside Top posts in the explore page.
        - Recent posts can however, still be found within the JSON.
        - Changing pages requires setting the *max_id* within the request which may mean moving from Selenium in some instances.