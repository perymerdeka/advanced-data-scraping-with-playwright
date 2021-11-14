from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()

    # requests
    page.goto('https://demo.opencart.com/admin')

    # bypass login
    page.fill('input#input-username', 'demo')
    page.fill('input#input-password', 'demo')
    page.click('button[type=submit]')

    # tag parameter if this tag is exists we can scrape the data
    page.is_visible('div.tile-body')

    # getting content header
    html = page.inner_html('#content')
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find('h2', attrs={'class':'pull-right'}).text
    print(price)

