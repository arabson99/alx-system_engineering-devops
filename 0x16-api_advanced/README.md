<p align="center">
	<img src="https://github.com/arabson99/alx-system_engineering-devops/blob/master/0x16-api_advanced/assets/API%20advanced.png" alt="API advanced">

# API advanced

The API advanced project is aimed at enhancing skills in working with APIs using the Reddit API. This project includes Python scripts designed to interact with various Reddit endpoints and perform different data handling tasks.

## Project Overview

This project focuses on querying the Reddit API to achieve specific functionalities:
  - Fetching the number of subscribers for a subreddit.
  - Retrieving and displaying the top ten hottest posts from a subreddit.
  - Recursively collecting titles of hot articles.
  - Analyzing and counting keyword occurrences in article titles.

## Function Implementations

The following functions are implemented:
  - `number_of_subscribers(subreddit)`: Returns the total number of subscribers for a specified subreddit. Returns `0` if the subreddit is invalid.
  - `top_ten(subreddit)`: Prints the top ten hottest posts for a given subreddit. Prints `None` if the subreddit is invalid.
  - `recurse(subreddit, hot_list=[])`: Recursively collects and returns a list of titles from all hot articles on a subreddit. Returns `None` if no articles are found.
  - `count_words(subreddit, word_list)`: Counts and prints the occurrences of specified keywords in titles of hot articles. Results are sorted by frequency and alphabetically if counts are identical.

