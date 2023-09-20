import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def find_by_landlord(**kwargs):
  landlord = kwargs.get('landlord', None)
  
  # Find all units that match the landlord name
  units = app_tables.units.search(
      q.any_of(
        Owner1=q.ilike(f'%{landlord}%'),
        Owner2=q.ilike(f'%{landlord}%'),
      )
    )
  print("Found " + str(len(units)) + " units.")

  # Give up if no units found at address 
  if len(units) == 0:
    return False

  print(units)
  
  return units