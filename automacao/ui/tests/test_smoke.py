from playwright.sync_api import Page, expect

URL = "https://logitrack.danieldiegosantana.me/"


def test_tela_de_login_carrega(page: Page):
    page.goto(URL)
    expect(page.get_by_role("button", name="Entrar")).to_be_visible()
