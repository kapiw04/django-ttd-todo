from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import pytest

@pytest.mark.django_db(transaction=True)
def test_crud_todo():
  options = Options()
  options.add_argument("--headless")
  with webdriver.Firefox(options=options) as browser:
    browser.get("http://localhost:8000")

    assert "To-Do List" in browser.title
    todos_table = browser.find_element(By.ID, "todos-table")
    rows: List[WebElement] = todos_table.find_elements(By.TAG_NAME, "tr")
    rows_count = len(rows)

    #* create
    sample_todo = {
      "title": "Sample To-Do",
      "description": "This is a sample to-do item."
    }
    browser.find_element(By.ID, "open-add-button").click()
    browser.implicitly_wait(5)
    input_title = browser.find_element(By.ID, "title-input")
    input_desc = browser.find_element(By.ID, "desc-input")
    
    input_title.send_keys(sample_todo["title"])

    input_desc.send_keys(sample_todo["description"])

    browser.find_element(By.ID, "confirm-add-button").click()

    # check if todo modal is no longer visible
    assert not browser.find_element(By.ID, "title-input").is_displayed()

    todos_table = browser.find_element(By.ID, "todos-table")
    rows: List[WebElement] = todos_table.find_elements(By.TAG_NAME, "tr")

    #* read
    assert rows_count + 1 == len(rows)
    assert todos_table is not None and rows is not None
    assert sample_todo["title"] in rows[-1].text

    #* update
    updated_todo = {
      "title": "Updated To-Do",
      "description": "This was a sample to-do. Now it's updated."
    }
    details_button = rows[-1].find_element(By.ID, "details-button")
    details_button.click()
    browser.implicitly_wait(5)
    update_button = browser.find_element(By.ID, "open-update-button")
    update_button.click()
    browser.implicitly_wait(5)
    input_title = browser.find_element(By.ID, "title-input")
    input_desc = browser.find_element(By.ID, "desc-input")

    # check if previous values are stored
    assert input_title.get_attribute("value")== sample_todo["title"]
    assert input_desc.get_attribute("value") == sample_todo["description"]

    input_title.clear()
    input_desc.clear()

    input_title.send_keys(updated_todo["title"])
    input_desc.send_keys(updated_todo["description"])

    browser.find_element(By.ID, "confirm-update-button").click()
    # browser.find_element(By.ID, "go-back-button").click()

    browser.implicitly_wait(5)
    todos_table = browser.find_element(By.ID, "todos-table")
    rows = todos_table.find_elements(By.TAG_NAME, "tr")
    assert updated_todo["title"] in rows[-1].text

    #* delete
    rows_count = len(rows)
    details_button = rows[-1].find_element(By.ID, "details-button")
    details_button.click()
    browser.implicitly_wait(5)
    delete_button = browser.find_element(By.ID, "delete-button")
    delete_button.click()
    todos_table = browser.find_element(By.ID, "todos-table")
    rows = todos_table.find_elements(By.TAG_NAME, "tr")
    assert rows_count - 1 == len(rows)

@pytest.mark.django_db
def test_checking_todo():
  options = Options()
  options.add_argument("--headless")
  with webdriver.Firefox(options=options) as browser:
    # adding sample todos
    todos = [
      {
        "title": "Buy milk",
        "desc": "No lactose",
      },
      {
        "title": "Load the dishwasher",
        "desc": "Then unload it after it's done!"
      }
    ]
    browser.get("http://localhost:8000")
    # add todos
    for todo in todos:
      browser.find_element(By.ID, "open-add-button").click()
      browser.implicitly_wait(5)
      input_title = browser.find_element(By.ID, "title-input")
      input_desc = browser.find_element(By.ID, "desc-input")
      
      input_title.send_keys(todo["title"])

      input_desc.send_keys(todo["desc"])

      browser.find_element(By.ID, "confirm-add-button").click()
      browser.implicitly_wait(5)    

    todos_table = browser.find_element(By.ID, "todos-table")
    rows: List[WebElement] = todos_table.find_elements(By.TAG_NAME, "tr")

    milk_todo, eggs_todo = rows[-2:]
    milk_todo.find_element(By.ID, "check-button").click()

    #* check the 'buy milk' task
    todos_table = browser.find_element(By.ID, "todos-table")
    todos_rows: List[WebElement] = todos_table.find_elements(By.TAG_NAME, "tr")
    assert len(todos_rows) < 2 or todos_rows[-2].text != todos[0]["title"]
    assert todos_rows[-1].text == todos[1]["title"]

    checked_rows = browser.find_element(By.ID, "checked-table").find_elements(By.TAG_NAME, "tr")
    assert checked_rows[-1].text == todos[0]["title"]

    #* uncheck the 'buy milk' task
    check_count = len(checked_rows)
    todos_table = browser.find_element(By.ID, "todos-table")
    milk_todo = browser.find_element(By.ID, "checked-table").find_elements(By.TAG_NAME, "tr")[1] # row 0 is the header
    print(milk_todo.get_attribute("innerHTML"))
    checkbox = milk_todo.find_element(By.ID, "check-button")
    checkbox.click()
    todos_table = browser.find_element(By.ID, "todos-table")
    checked_rows = browser.find_element(By.ID, "checked-table").find_elements(By.TAG_NAME, "tr")
    # import pdb; pdb.set_trace()
    assert check_count - 1 == len(checked_rows)

    todos_rows: List[WebElement] = todos_table.find_elements(By.TAG_NAME, "tr")
