import os
import re

import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://logitrack.danieldiegosantana.me"
EMAIL = os.environ.get("LOGITRACK_EMAIL")
SENHA = os.environ.get("LOGITRACK_PASSWORD")

precisa_credenciais = pytest.mark.skipif(
    not (EMAIL and SENHA),
    reason="Defina LOGITRACK_EMAIL e LOGITRACK_PASSWORD (credenciais do desafio)",
)


def fazer_login(page: Page, email: str, senha: str) -> None:
    page.goto(f"{BASE_URL}/login")
    page.get_by_role("textbox", name="Email").fill(email)
    page.get_by_role("textbox", name="Senha").fill(senha)
    page.get_by_role("button", name="Entrar").click()


@precisa_credenciais
def test_ct_log_01_login_valido_acessa_o_dashboard(page: Page):
    fazer_login(page, EMAIL, SENHA)
    expect(page).to_have_url(re.compile(r"/dashboard"))


def test_ct_log_03_email_inexistente_exibe_erro(page: Page):
    fazer_login(page, "inexistente.qa@exemplo.com", "abcdef")
    expect(page.get_by_text("Invalid email or password")).to_be_visible()
    expect(page).to_have_url(re.compile(r"/login"))


@precisa_credenciais
@pytest.mark.xfail(reason="BUG-01: o sistema aceita senha incorreta para e-mail cadastrado")
def test_ct_log_02_senha_incorreta_deve_ser_rejeitada(page: Page):
    fazer_login(page, EMAIL, "123456")
    expect(page.get_by_text("Invalid email or password")).to_be_visible()
    expect(page).to_have_url(re.compile(r"/login"))


def test_dashboard_sem_login_redireciona_para_o_login(page: Page):
    page.goto(f"{BASE_URL}/dashboard")
    expect(page).to_have_url(re.compile(r"/login"))
