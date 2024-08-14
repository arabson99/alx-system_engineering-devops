#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances=None, after=None, count=0):
    """Print counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Dictionary to store the count of words.
        after (str): The 'after' parameter for the next page of API results.
        count (int): The count of results matched thus far.
    """
    if instances is None:
        instances = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/yourusername)"
    }
    params = {"after": after, "count": count, "limit": 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 404:
            return

        data = response.json().get("data")
        after = data.get("after")
        posts = data.get("children")

        word_list = [word.lower() for word in word_list]

        for post in posts:
            title = post.get("data").get("title").lower().split()
            for word in word_list:
                occurrences = title.count(word)
                if occurrences > 0:
                    if word in instances:
                        instances[word] += occurrences
                    else:
                        instances[word] = occurrences

        if after is not None:
            return count_words(subreddit, word_list, instances, after, count + len(posts))

        if instances:
            sorted_instances = sorted(instances.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_instances:
                print(f"{word}: {count}")
        else:
            print("")

    except Exception:
        print("")
        return
