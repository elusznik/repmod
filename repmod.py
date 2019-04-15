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
            sites.append("." + line.strip().replace(".",r"\.") + ".")
            print("." + line.strip().replace(".",r"\.") + ".")
    f.close()

    for item in sub.mod.spam():
        link_approved = False
        if type(item) is praw.models.Comment:
            print(item.body)
            link_approved = any(re.search(site, item.body.lower(), re.IGNORECASE) for site in sites)
        if type(item) is praw.models.Submission:
            link_approved = any(re.search(site,item.title.lower(), re.IGNORECASE) for site in sites) or any(re.search(site, item.url.lower(), re.IGNORECASE) for site in sites) or any(re.search(site, item.selftext.lower(), re.IGNORECASE) for site in sites)
        if link_approved:
            print("Item {} to approve".format(item))

if __name__ == "__main__":
    main()
