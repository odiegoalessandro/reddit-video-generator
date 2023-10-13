from constants import *
from reddit_client import reddit_client
from services import *

subreddit = reddit_client.subreddit(SUBREDDIT)
top_posts = subreddit.top(time_filter=TIME_FILTER, limit=1)

for post in top_posts:
    text_parts = split_text(post.selftext)
    translated_text_parts = [translate_text(text) for text in text_parts]
    final_title = translate_text(post.title)
    final_text = join_text(translated_text_parts)
    print(final_title + "\n" + final_text)
