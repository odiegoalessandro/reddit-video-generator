import os

from dotenv import load_dotenv
from playwright.sync_api import Page, sync_playwright

from constants import *
from services.log import *

load_dotenv(".env")


def login_to_reddit(page: Page, username: str, password: str):
    try:
        page.goto(REDDIT_URL_LOGIN)

        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)

        page.click('button[type="submit"]')
        page.wait_for_timeout(5000)
        # page.wait_for_url("")
        print_success("Login realizado com sucesso")

    except Exception as e:
        print_error(f"Erro ao fazer login: {str(e)}")


def take_screenshot(page: Page, url: str, filename: str):
    screenshots_path = os.path.join(os.getcwd(), "screenshots")

    if not os.path.exists:
        print_observation("Criando diretorio screenshots...")
        os.mkdir(screenshots_path)

    page.goto(url)
    page.set_viewport_size({'height': 800, 'width': 1200})

    element = page.locator("data-testid=post-container")
    page.wait_for_load_state("load")

    page.screenshot(
        path=f"{os.path.join(screenshots_path, filename)}.png", clip=element.first.bounding_box())


def run_scraping(post, index: int):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        USERNAME = os.getenv("REDDIT_USER_NAME")
        PASSWORD = os.getenv("REDDIT_PASSWORD")

        login_to_reddit(page, USERNAME, PASSWORD)
        take_screenshot(page, post.url, str(index))

        browser.close()
