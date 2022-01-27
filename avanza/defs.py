from helpers import FormatTable, FormatTitle, FormatJson
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver
import colorful as cf

def init_AvanzaFund(args):
    """
        Initiate selenium, trigger AvanzaFund() and start/stop headless
        display.
    """
    display = Display(visible=0, size=(1024, 768))
    display.start()
    opts = webdriver.ChromeOptions()
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-setuid-sandbox')
    browser = webdriver.Chrome(options=opts)
    AvanzaFund(args, browser)
    display.stop()

def AvanzaFund(args, browser):
    """
        Grab fund source code, soup it and return beautiful
        terminal tables.
    """
    browser.get('https://www.avanza.se/fonder/om-fonden.html/{}/'.format(args.id))
    soup = BeautifulSoup(browser.page_source, "html.parser")
    title = soup.find("h1")
    if len(title.text) > 2:
        search = soup.find_all("aza-period-button")
        data = []
        for option in search:
            try:
                time = option.find('span', attrs={'class':'ng-star-inserted'})
                change = option.find('span', attrs={'class':'change'})
                if change.text.startswith('+'):
                    change = cf.cyan(change.text)
                else:
                    change = cf.red(change.text)
                obj = [time.text, str(change)]
                data.append(obj)
            except Exception as E:
                pass
        if args.json:
            FormatJson(title.text, data)
        else:
            FormatTitle(title, "title")
            FormatTable(data)
    else:
        FormatTitle(f"Fund {args.id} not found ({fund_url}). Maybe wrong fund id?", "warning")
