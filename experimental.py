import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
async def func(num):
    options = Options()
    options.add_argument("start-maximized")
    webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
async def func2():
    print("hello man")
loop = asyncio.new_event_loop()
async def create_tasks_func():
    await asyncio.wait({asyncio.create_task(func(2)),asyncio.create_task(func2())})
loop.run_until_complete(create_tasks_func())
loop.close()