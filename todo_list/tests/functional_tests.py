from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

def test_add_todo():
  browser = webdriver.Firefox()
  browser.get("http://localhost:8000")

  sample_todo = {
    "title": "Sample To-Do",
    "description": "This is a sample to-do item."
  }

  browser.find_element(By.ID, "open_add_button").click()
  browser.implicitly_wait(5)
  input_title = browser.find_element(By.ID, "input_title")
  input_desc = browser.find_element(By.ID, "input_desc")
  
  input_title.send_keys(sample_todo["title"])
  input_desc.send_keys(sample_todo["description"])

  browser.find_element(By.ID, "confirm_add_button").click()

  todos_table = browser.find_element(By.ID, "todos_table")
  rows: List[WebElement] = todos_table.find_elements(By.TAG_NAME, "tr")

  assert sample_todo["title"] in rows[-1].text
