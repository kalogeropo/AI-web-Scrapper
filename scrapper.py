
import selenium.webdriver as webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
def scrape_website(website:str) -> str:
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    try:
        driver.get(website)
        print("page loaded")
        html = driver.page_source
        return html
    finally:
        driver.quit()
        print("driver closed")

def extract_body(html:str) -> str:
    """
    :param html: str html content of the website
    :return: str extract the body of the html extract the body of the html
    """
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    if body:
        return str(body)
    return ""

def clean_body(body:str) -> str:
    """
    :param body: str body of the html
    :return: str clean the body of the html from useless tags
    """
    try:
        soup = BeautifulSoup(body, 'html.parser')
        for script_style in soup(["script", "style"]):
            script_style.extract()
        clean_content = soup.get_text(separator="\n")
        clean_content = "\n".join([line.strip() for line in clean_content.split("\n") if line.strip()])
        return clean_content
    except TypeError:
        print("ERROR")
        return ""




#split the text into paragraphs-batches in order to feed to a LLM model

def create_dom_baches(clean_content:str, batch_size:int = 6000) -> list:
    """
    :param clean_content: str clean content of the html
    :param batch_size: int number of terms in each batch
    :return: list split the content into batches
    """
    return [clean_content[i:i+batch_size] for i in range(0, len(clean_content), batch_size)]

