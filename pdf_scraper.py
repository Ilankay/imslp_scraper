import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


if __name__ == "__main__":
    with open("jsons/links.json", 'r') as links_json:
        links = json.load(links_json)
 #  print(links['0'],links['1'],links['250'])

    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    pdf_links = {}
    for index, i in enumerate(links.keys()):
        print(f"we are on document {index}")
        driver.get(links[i])
        try:
            span = driver.find_element(By.CSS_SELECTOR, "span[title = 'Download this file']")
            link = span.find_element(By.XPATH, "..")
        except Exception as e:
            print("skipped! ")
            continue
        pdf_links[index] = link.get_attribute('href')
        print(pdf_links[index])

    with open("jsons/pdf_links.json", 'w') as f:
        json.dump(pdf_links, f)
