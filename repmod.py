"""reddit bot for auto-approving website links in rep-related subreddits"""
import time
import re
import praw

def main():
    """main function, checking the spam page every 5 minutes"""
    print("Authenticating...")
    reddit = praw.Reddit("repmod")
    print("Authenticated as {}\n".format(reddit.user.me()))
    sub = reddit.subreddit("eluszniktest")

    sites = []
    with open("sites.txt", "r", encoding="utf-8") as file:
        for line in file:
            sites.append("." + line.strip().replace(".", r"\.") + ".")
            print("." + line.strip().replace(".", r"\.") + ".")
    file.close()

    for item in sub.top("week"):
        print(item.title)

    while True:
        for item in sub.mod.spam():
            link_approved = False
            if isinstance(item, praw.models.Comment):
                link_approved = any(re.search(site, item.body.lower(), re.IGNORECASE) for site in sites)
            if isinstance(item, praw.models.Submission):
                link_approved = any(re.search(site, item.title.lower(), re.IGNORECASE) for site in sites) or any(re.search(site, item.url.lower(), re.IGNORECASE) for site in sites) or any(re.search(site, item.selftext.lower(), re.IGNORECASE) for site in sites)
            if link_approved:
                item.mod.approve()
                print("Item {} approved".format(item))
        time.sleep(300)

if __name__ == "__main__":
    main()
