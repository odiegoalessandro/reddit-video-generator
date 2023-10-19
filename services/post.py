import os

from reddit.subreddit import get_subreddit_thread
from services.log import print_observation, print_success
from services.tts import text_to_mp3
from services.utils import get_mp3_duration


def process_post(post, index, GET_COMMENTS):
    voices_path = os.path.join(os.getcwd(), "voices")

    post_title = f"post-{index}-title"
    post_body = f"post-{index}-body"

    post_thread = get_subreddit_thread(post.id)

    text_to_mp3(filename=post_title, text=post.title)
    text_to_mp3(filename=post_body, text=post.selftext)

    post_audio_duration = int(get_mp3_duration(
        f"{voices_path}/{post_title}.mp3") + get_mp3_duration(f"{voices_path}/{post_body}.mp3"))

    print_observation(f"Post {index} tem a duração de {
                      post_audio_duration} segundos.")

    if GET_COMMENTS:
        for comment_index, comment in enumerate(post_thread["comments"]):
            text_to_mp3(
                filename=f"post-{index}-comment-{comment_index}", text=comment["body"])

    print_success(f"Gerar arquivos .mp3 do post {
                  index} finalizado com sucesso.")
