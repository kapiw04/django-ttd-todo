from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import pytest

@pytest.mark.django_db(transaction=True)
def test_crud_todo():
  with webdriver.Firefox() as browser:
    browser.get("http://localhost:8000")

    assert "To-Do List" in browser.title


    #* create
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

    # check if todo modal is no longer visible
    with pytest.raises(Exception):
      browser.find_element(By.ID, "id_title")

    todos_table = browser.find_element(By.ID, "todos-table")
    rows: List[WebElement] = todos_table.find_elements(By.TAG_NAME, "tr")

    #* read
    assert todos_table is not None and rows is not None
    assert sample_todo["title"] in rows[-1].text

    #* update
    updated_todo = {
      "title": "Updated To-Do",
      "description": "This was a sample to-do. Now it's updated."
    }
    update_button = rows[-1].find_element(By.ID, "update-button")
    update_button.click()
    browser.implicitly_wait(5)
    input_title = browser.find_element(By.ID, "id_title")
    input_desc = browser.find_element(By.ID, "id_desc")

    # check if previous values are stored
    assert input_title == sample_todo["title"]
    assert input_desc == sample_todo["description"]

    input_title.clear()
    input_desc.clear()
    pytest.fail("Finish Test")

    input_title.send_keys(updated_todo["title"])
    input_desc.send_keys(updated_todo["description"])

    browser.find_element(By.ID, "confirm-update-button").click()

    rows = todos_table.find_elements(By.TAG_NAME, "tr")
    assert updated_todo["title"] in rows[-1].text

    #* delete
    rows_count = len(rows)
    delete_button = rows[-1].find_element(By.ID, "delete-button")
    delete_button.click()
    rows = todos_table.find_elements(By.TAG_NAME, "tr")
    assert rows_count - 1 == len(rows)

