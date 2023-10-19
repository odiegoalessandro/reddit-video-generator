from constants import *
from reddit.client import reddit_client
from services.log import *
from services.post import process_post

if __name__ == "__main__":
    print_observation("Inicializando script...")

    subreddit = reddit_client.subreddit(SUBREDDIT)
    top_posts = subreddit.top(time_filter=TIME_FILTER, limit=LIMIT_OF_POSTS)

    for index, post in enumerate(top_posts):
        process_post(post, index, GET_COMMENTS)

    print_success("Script finalizado com sucesso.")
