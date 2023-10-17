from constants import *
from reddit.client import reddit_client
from reddit.subreddit import get_subreddit_thread
from services.tts import text_to_mp3
from services.utils import *

subreddit = reddit_client.subreddit(SUBREDDIT)
top_posts = subreddit.top(time_filter=TIME_FILTER, limit=LIMIT_OF_POSTS)

if __name__=="__main__":    
    for index, post in enumerate(top_posts):
        post_thread = get_subreddit_thread(post.id)
        text_to_mp3(filename=f"{index}-title", text=post.title)
        text_to_mp3(filename=f"{index}-body", text=post.selftext)
        # criar a logica para obter os comentarios em formato de mp3