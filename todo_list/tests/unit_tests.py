import pytest
from django.urls import reverse
from todo_list.models import TodoItem

@pytest.mark.django_db
@pytest.mark.parametrize('title, description', [
  ('', 'This is a test to-do item.'),
  ('Test To-Do', ''),
  ('', ''),
  ('   ', '   '),
  ('', '   '),
  ('   ', ''),
])
def test_create_todo_with_empty_fields(client, title, description):
  response = client.post(reverse('add'), {'title': title, 'description': description})
  assert response.status_code == 400  # Assuming the view returns a 400 for bad requests

@pytest.mark.django_db
@pytest.mark.parametrize('title, description', [
  ("a"*31, "aaaa"),
  ("aaaa", "a" * 1_000)
])
def test_create_todo_with_too_long_inputs(client, title, description):
  response = client.post(reverse('add'), {'title': title, 'description': description})
  assert response.status_code == 400  # Assuming the view returns a 400 for bad requests
