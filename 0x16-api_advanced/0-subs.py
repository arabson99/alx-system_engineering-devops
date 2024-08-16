import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API for the number of subscribers of a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if an error
             occurs or the subreddit is invalid.
    """

    # Base URL for subreddit information endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent header to avoid rate limiting issues
    headers = {
        "User-Agent": "My Reddit API Client v1.0"
    }

    # Send a GET request with no redirects
    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )
        response.raise_for_status()
        data = response.json()
        return data.get(
            "subscribers",
            0
        )  # Return subscribers or 0 if not found
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
