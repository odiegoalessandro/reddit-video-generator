from constants import *
from reddit.client import reddit_client
from reddit.subreddit import get_subreddit_thread
from services.utils import *

subreddit = reddit_client.subreddit(SUBREDDIT)
top_posts = subreddit.top(time_filter=TIME_FILTER, limit=LIMIT_OF_POSTS)

if __name__=="__main__":    
    for post in top_posts:
        print(get_subreddit_thread(post.id))