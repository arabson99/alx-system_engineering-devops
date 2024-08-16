#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if an error occurs or
              the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Ensure that the status code is OK
        response.raise_for_status()
        # Get the JSON data
        data = response.json()
        # Check for the 'data' key and get the number of subscribers
        if "data" in data:
            return data["data"].get("subscribers", 0)
    except requests.RequestException:
        return 0

    return 0
