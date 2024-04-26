#!/usr/bin/python3
"""Displays GitHub user ID using Basic Authentication."""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(
        "https://api.github.com/user",
        auth=(username, password)
    )

    try:
        user_info = response.json()
        print(user_info.get("id"))
    except ValueError:
        print("None")
