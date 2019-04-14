import praw
import re

def main():
    print("Authenticating...")
    reddit = praw.Reddit("repmod")
    print("Authenticated as {}\n".format(reddit.user.me()))
    sub = reddit.subreddit("eluszniktest")
    sites = []
    with open("sites.txt","r",encoding="utf-8") as f:
        for line in f:
            sites.append('.' + line.strip().replace('.',r'\.') + '.')
            print('.' + line.strip().replace('.',r'\.') + '.')
    f.close()

    for item in sub.mod.spam():
        print(type(item))

if __name__ == "__main__":
    main()
