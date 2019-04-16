# repmod
## reddit bot for auto-approving website links in rep-related subreddits and generating a weekly summary, created by [/u/elusznik](https://www.reddit.com/u/Elusznik) for the [FashionReps](https://www.reddit.com/r/FashionReps)

Firstly, clone the repo to your machine.
In order to run the code on your servers, you will need Python 3 installed as well as the praw module. PRAW is the reddit API wrapper for Python and you can install it with

`pip3 install praw` on Linux and macOS

or

`pip install praw` on Windows.

You will also need to configure it with a `praw.ini` file, I'll send you one with the code. It will be preconfigured with API keys and credentials for reddit user /u/repfammod. It's a fresh account that I created a few days ago with the bot in mind. The account which the bot uses will need to have moderator privileges.
`praw.ini` needs to look like this:
```
[DEFAULT]
# A boolean to indicate whether or not to check for package updates.
check_for_updates=True

# Object to kind mappings
comment_kind=t1
message_kind=t4
redditor_kind=t2
submission_kind=t3
subreddit_kind=t5

# The URL prefix for OAuth-related requests.
oauth_url=https://oauth.reddit.com

# The URL prefix for regular requests.
reddit_url=https://www.reddit.com

# The URL prefix for short URLs.
short_url=https://redd.it

[repmod]
client_id=
client_secret=
password=
username=
user_agent=repmod (by /u/elusznik)

```
With linec `client_id`, `client_secret`, `password` and `username` being filled with your API keys and bot account's username and password.

After configuring, you will just need to run

`python3 repmod.py`

Be advised, if you use SSH or some other form of remote connection to your server, the bot needs to run in something like GNU screen or tmux session in order for the script to not be closed on disconnect.
_____

## bot's component dedicated to weekly roundup
## to be used with cron

In order to run the summary component, you need to have `cron` installed on your server.
Then, run

`crontab -e`

and select your desired editor.
Then, add the line

`00 12 * * sat cd BOTDIR; python3 roundup.py`

with `BOTDIR` being the directory in which scripts are located. This particular cron setting will run the script **on Saturday at 12:00 (midday)**.
Save & close your editor. The weekly roundup script should now be set up.
