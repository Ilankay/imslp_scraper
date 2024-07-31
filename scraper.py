import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import threading


def main(links):
    options = Options()
    options.add_experimental_option('prefs', {
        "download.default_directory": "/home/ilan/Documents/ml/personal_project/scalper/sheets_pdf/",
        "download.prompt_for_download": False,  # To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True 
    })
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    for index, i in enumerate(links):
        print(f"{threading.current_thread().name}: we are on document {index}")
        link = i
        link = link.replace("ImagefromIndex", "IMSLPDisclaimerAccept")

        driver.get(link)

        if "IMSLPImageHandler" in driver.current_url:
            time.sleep(15.5)
            span = driver.find_element(By.CSS_SELECTOR, "span[id = 'sm_dl_wait']")
            href = span.get_attribute('data-id')
            driver.get(href)


if __name__ == "__main__":
    with open('jsons/pdf_links.json', 'r') as links_json:
        links_dict = json.load(links_json)

    links = []
    for i in links_dict.keys():
        links.append(links_dict[i])

    t1 = threading.Thread(target=main, args=[links[:len(links)//3]])
    t2 = threading.Thread(target=main, args=[links[len(links)//3:(len(links)//3)*2]])
    t3 = threading.Thread(target=main, args=[links[(len(links)//3)*2:]])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
