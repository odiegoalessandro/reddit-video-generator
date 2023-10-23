import os

from dotenv import load_dotenv
from log import *
from playwright.sync_api import Page, sync_playwright

from constants import *

load_dotenv(".env")


def login_to_reddit(page: Page, username: str, password: str):
    try:
        page.goto(REDDIT_URL_LOGIN)

        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)

        page.click('button[type="submit"]')
        page.wait_for_function(
            'window.location.href.includes("https://www.reddit.com/")', timeout=10000)
        print_success("Login realizado com sucesso")

    except Exception as e:
        print_error(f"Erro ao fazer login: {str(e)}")
        

def run_scraping():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        USERNAME = os.getenv("REDDIT_USER_NAME")
        PASSWORD = os.getenv("REDDIT_PASSWORD")

        login_to_reddit(page, USERNAME, PASSWORD)

        browser.close()
