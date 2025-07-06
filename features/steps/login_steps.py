# steps/login_steps.py
from behave import *
from pages.login_page import LoginPage
from utils.config_reader import Config
from playwright.sync_api import expect

@given('que estoy en la página de inicio de sesión')
def step_impl(context):
    context.login_page = LoginPage(context.page)
    context.login_page.goto_login_page()
    expect(context.page).to_have_url(Config.BASE_URL)

@when('introduzco un nombre de usuario y contraseña válidos')
def step_impl(context):
    context.login_page.fill_text_input(context.login_page.username_input, Config.VALID_USERNAME)
    context.login_page.fill_text_input(context.login_page.password_input, Config.VALID_PASSWORD)

@when('introduzco un nombre de usuario y contraseña no válidos')
def step_impl(context):
    context.login_page.fill_text_input(context.login_page.username_input, Config.INVALID_USERNAME)
    context.login_page.fill_text_input(context.login_page.password_input, Config.INVALID_PASSWORD)

@when('introduzco solo la contraseña')
def step_impl(context):
    context.login_page.fill_text_input(context.login_page.password_input, Config.VALID_PASSWORD)
    context.login_page.fill_text_input(context.login_page.username_input, "")

@when('hago clic en el botón de Login')
def step_impl(context):
    context.login_page.click_element(context.login_page.login_button)

@then('debería ser redirigido al tablero con un mensaje de bienvenida "{message}"')
def step_impl(context, message):
    expect(context.page.locator(context.login_page.success_message)).to_contain_text(message)
    expect(context.page).not_to_have_url(Config.BASE_URL)

@then('debería ver un mensaje de error "{message}"')
def step_impl(context, message):
    expect(context.page.locator(context.login_page.error_message)).to_contain_text(message)
    expect(context.page).to_have_url(Config.BASE_URL) 

@then('cierro sesión')
def step_impl(context):
    context.login_page.logout()
    expect(context.page).to_have_url(Config.BASE_URL) 