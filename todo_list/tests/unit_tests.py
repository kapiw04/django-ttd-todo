import pytest 

def test_home_page(client):
  response = client.get("/")    
  assert response.status_code == 200
  assert "<title>To-Do List</title>" in str(response.content)
    



