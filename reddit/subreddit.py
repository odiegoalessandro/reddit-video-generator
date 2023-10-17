from constants import *
from reddit.client import reddit_client


def get_subreddit_thread(id):
    post = reddit_client.submission(id=id)
    list_comments = post.comments.list()[:LIMIT_OF_COMMENTS]
    comments = []

    for comment in list_comments:
        comments.append({
            "id": comment.id,
            "body": comment.body,
            "url": f"{REDDIT_BASE_URL}{comment.permalink}"
        })

    return {
        "title": post.title,
        "body": post.selftext,
        "comment": comments 
    }

def get_subreddit_post(id):
    post = reddit_client.submission(id=id)

    return {
        "title": post.title,
        "body": post.selftext,
        "url": post.url
    }
