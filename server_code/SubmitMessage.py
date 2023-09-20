import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def save_message(**kwargs):
  return app_tables.messages.add_row(
      firstname = kwargs.get('firstname', None),
      lastname = kwargs.get('lastname', None),
      email = kwargs.get('email', None),
      story = kwargs.get('story', None),
      address = kwargs.get('address', None),
      unit = kwargs.get('unit', None)
    )