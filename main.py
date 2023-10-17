from constants import *
from reddit.client import reddit_client
from reddit.subreddit import get_subreddit_thread
from services.log import *
from services.tts import text_to_mp3
from services.utils import *

if __name__ == "__main__":
    print_observation("Inicializando script...")

    subreddit = reddit_client.subreddit(SUBREDDIT)
    top_posts = subreddit.top(time_filter=TIME_FILTER, limit=LIMIT_OF_POSTS)

    print_success("Pegar posts concluido.")

    for index, post in enumerate(top_posts):
        post_thread = get_subreddit_thread(post.id)
        text_to_mp3(filename=f"{index}-title", text=post.title)
        text_to_mp3(filename=f"{index}-body", text=post.selftext)
        for comment_index, comment in enumerate(post_thread["comments"]):
            text_to_mp3(
                filename=f"{index}-comment-{comment_index}", text=comment["body"])

        print_success(f"Gerar arquivos .mp3 do post {
                      index} finalizado com sucesso.")

    print_success("Script finalizado com sucesso.")
