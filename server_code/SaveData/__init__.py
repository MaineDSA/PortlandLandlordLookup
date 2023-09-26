import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def save_data(**kwargs):
  return app_tables.messages.add_row(
      email = kwargs.get('email', None),
      address = kwargs.get('address', None),
      unit = kwargs.get('unit', None)
    )