from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import pytest

@pytest.mark.django_db(transaction=True)
def test_add_todo():
  with webdriver.Firefox() as browser:
    browser.get("http://localhost:8000")

    sample_todo = {
      "title": "Sample To-Do",
      "description": "This is a sample to-do item."
    }

    browser.find_element(By.ID, "open-add-button").click()
    browser.implicitly_wait(5)
    input_title = browser.find_element(By.ID, "id_title")
    input_desc = browser.find_element(By.ID, "id_desc")
    
    input_title.send_keys(sample_todo["title"])

    input_desc.send_keys(sample_todo["description"])

    browser.find_element(By.ID, "confirm-add-button").click()
    todos_table = browser.find_element(By.ID, "todos-table")
    rows: List[WebElement] = todos_table.find_elements(By.TAG_NAME, "tr")

    assert todos_table is not None and rows is not None

    assert sample_todo["title"] in rows[-1].text
  # browser.close(); pytest.fail("Finish Test")  # noqa: E702

