"""
reddit bot for auto-approving website links in rep-related subreddits
weekly roundup included since 1.1 alpha
witten by /u/elusznik
deticated for /r/FashionReps
"""
import time
import re
import praw

def main():
    """
    main function, checking the spam page every 5 minutes
    """

    print("Authenticating...")
    reddit = praw.Reddit("repmod", user_agent="repmod (by /u/elusznik)")
    print("Authenticated as {}\n".format(reddit.user.me()))
    sub = reddit.subreddit("FashionReps")

    sites = []
    with open("sites.txt", "r", encoding="utf-8") as file:
        print("Approved sites:")
        for line in file:
            sites.append("." + line.strip().replace(".", r"\.") + ".")
            print(line.strip())
    file.close()
    print()

    # review = 0
    # find = 0
    # news = 0
    # top_posts = {}
    # top_posts["⚠️ MODPOST ⚠️"] = []
    # top_posts["REVIEW"] = []
    # top_posts["FIND"] = []
    # top_posts["NEWS"] = []
    # week_summary = ""
    # week_summary_title = "Past week's summary"

    # for item in sub.top("week"):

    #     #print(item.title)
    #     # if item.link_flair_template_id:
    #     #     print(item.link_flair_template_id)
    #     # if item.link_flair_text:
    #     #     print(item.title)
    #     #     print(item.link_flair_text)
    #     #     print(item.permalink+'\n')

    #     if item.link_flair_text:
    #         if item.link_flair_text == "⚠️ MODPOST ⚠️":
    #             top_posts[item.link_flair_text].append((item.title, item.permalink))

    #         if item.link_flair_text == "REVIEW" and review < 10:
    #             top_posts[item.link_flair_text].append((item.title, item.permalink))
    #             review += 1

    #         if item.link_flair_text == "FIND" and find < 10:
    #             top_posts[item.link_flair_text].append((item.title, item.permalink))
    #             find += 1

    #         if item.link_flair_text == "NEWS" and news < 10:
    #             top_posts[item.link_flair_text].append((item.title, item.permalink))
    #             news += 1

    # for flair, posts in top_posts.items():
    #     if posts:
    #         week_summary += flair + "\n\n"
    #         for post in posts:
    #             week_summary += "[{}](https://www.reddit.com".format(post[0]) + post[1] + ")\n"
    #         week_summary += "\n"

    # print(week_summary_title)
    # print(week_summary.rstrip())
    # sub.submit(week_summary_title, selftext=week_summary.rstrip())

    while True:
        for item in sub.mod.spam():
            link_approved = False
            if isinstance(item, praw.models.Comment):
                link_approved = any(re.search(site, item.body.lower(), re.IGNORECASE) for site in sites)
                if link_approved:
                    print(item.body)
            elif isinstance(item, praw.models.Submission):
                link_approved = any(re.search(site, item.title.lower(), re.IGNORECASE) for site in sites) or any(re.search(site, item.url.lower(), re.IGNORECASE) for site in sites) or any(re.search(site, item.selftext.lower(), re.IGNORECASE) for site in sites)
                if link_approved:
                    print(item.title)
            if link_approved:
                item.mod.approve()
                print("Item {} approved".format(item))
        time.sleep(300)

if __name__ == "__main__":
    main()
