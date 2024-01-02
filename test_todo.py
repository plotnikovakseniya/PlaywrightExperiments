from playwright.sync_api import Playwright, sync_playwright, expect

def test_add_todo_fixture_playwright(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("search me something")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    context.close()
    browser.close()


def test_add_todo_fixture_page(page) -> None:
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("search me something")
    page.get_by_placeholder("What needs to be done?").press("Enter")


def test_add_todo_expect(page) -> None:
    url_to_go = 'https://demo.playwright.dev/todomvc/#/'
    page.goto(url_to_go)
    expect(page).to_have_url(url_to_go)
    todo_input = page.locator('.new-todo')
    expect(todo_input).to_be_empty()
    todo_input.fill('Задача №1')
    todo_input.press('Enter')
    todo_input.fill('Задача №2')
    todo_input.press('Enter')
    expect(page.locator('.todo-list > li')).to_have_count(2)

    page.locator(".todo-list >> li >> [type='checkbox']").first.click()
    expect(page.locator('.todo-list >> li').first).to_have_class('completed')
    expect(page.locator('.todo-list >> li >> label').first).to_have_css('text-decoration-line', 'line-through')

# with sync_playwright() as playwright:
#     run(playwright)
