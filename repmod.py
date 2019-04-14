import praw
import re

def main():
    print("Authenticating...")
    reddit = praw.Reddit("repmod")
    print("Authenticated as {}\n".format(reddit.user.me()))
    sub = reddit.subreddit("eluszniktest")

    for item in sub.mod.spam():
        print(item)

if __name__ == "__main__":
    main()
