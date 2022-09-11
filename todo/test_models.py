from django.test import TestCase
from .models import Item


class TestModels(TestCase):

  def test_done_defaults_to_false(self):
    # Test if a new created item has default done value 
    # set to false. 
    # We expect the assert returns false if the values done is set to true.
    item = Item.objects.create(name='Test Todo Item')
    self.assertFalse(item.done)

  def test_item_string_method_returns_name(self):
    item = Item.objects.create(name='Test Todo Item')
    self.assertEqual(str(item), 'Test Todo Item')