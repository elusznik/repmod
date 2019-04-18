"""
bot's component dedicated to weekly roundup
to be used with cron
witten by /u/elusznik
deticated for /r/FashionReps
"""
import praw

def main():
    """
    main function, generating and posting the roundup
    """

    print("Authenticating...")
    reddit = praw.Reddit("repmod", user_agent="repmod (by /u/elusznik)")
    print("Authenticated as {}\n".format(reddit.user.me()))
    sub = reddit.subreddit("FashionReps")

    review = 0
    find = 0
    news = 0
    top_posts = {}
    top_posts["⚠️ MODPOST ⚠️"] = []
    top_posts["REVIEW"] = []
    top_posts["FIND"] = []
    top_posts["NEWS"] = []
    week_summary = ""
    week_summary_title = "FashionReps Weekly Roundup"
    week_summary_flair = "WEEKLY NEWS"

    for item in sub.top("week"):

        #print(item.title)
        # if item.link_flair_template_id:
        #     print(item.link_flair_template_id)
        # if item.link_flair_text:
        #     print(item.title)
        #     print(item.link_flair_text)
        #     print(item.permalink+'\n')

        if item.link_flair_text:
            if item.link_flair_text == "⚠️ MODPOST ⚠️":
                top_posts[item.link_flair_text].append((item.title, item.permalink))

            if item.link_flair_text == "REVIEW" and review < 10:
                top_posts[item.link_flair_text].append((item.title, item.permalink))
                review += 1

            if item.link_flair_text == "FIND" and find < 10:
                top_posts[item.link_flair_text].append((item.title, item.permalink))
                find += 1

            if item.link_flair_text == "NEWS" and news < 10:
                top_posts[item.link_flair_text].append((item.title, item.permalink))
                news += 1

    for flair, posts in top_posts.items():
        if posts:
            week_summary += "#" + flair + "\n\n"
            for post in posts:
                week_summary += "[{}](https://www.reddit.com".format(post[0]) + post[1] + ")\n\n"
            week_summary += "\n"

    print(week_summary_title)
    print(week_summary.rstrip())

    if week_summary:
        sub.submit(week_summary_title, selftext=week_summary.rstrip(), flair_id="1e13f32e-61c9-11e9-9893-0e1929d25dca")

if __name__ == "__main__":
    main()
