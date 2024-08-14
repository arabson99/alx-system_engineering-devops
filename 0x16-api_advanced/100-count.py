#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    # Normalize the word list to lowercase
    word_list = [word.lower() for word in word_list]
    
    # Make the request to Reddit's API
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        # Check for 404 error indicating subreddit not found
        if response.status_code == 404:
            print("OK")
            return

        # Get the JSON data
        results = response.json()
        results = results.get("data")
        after = results.get("after")
        count += results.get("dist")

        # Process each post title
        for c in results.get("children"):
            title = c.get("data").get("title").lower().split()
            for word in word_list:
                if word in title:
                    times = title.count(word)
                    if instances.get(word) is None:
                        instances[word] = times
                    else:
                        instances[word] += times

        # Check if there's another page of results
        if after is None:
            if len(instances) == 0:
                print("OK")
                return

            # Sort and print the results
            sorted_instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
            for k, v in sorted_instances:
                print("{}: {}".format(k, v))
        else:
            count_words(subreddit, word_list, instances, after, count)

    except Exception:
        print("OK")
