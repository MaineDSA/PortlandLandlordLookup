import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#

@anvil.server.callable
def find_units(**kwargs):
  address = kwargs.get('address', None)
  unit = kwargs.get('unit', None)
  
  # Find all units that match the address
  building_units = app_tables.units.search(
      #tables.order_by('unitNumber1'),
      Address=q.ilike(f'%{address}%'),
    )
  print("Found " + str(len(building_units)) + " building matches.")

  # Give up if no units found at address 
  if len(building_units) == 0:
    return False
  
  # Find all units that match the unit AND the address
  unit_matches = app_tables.units.search(q.all_of(
      #tables.order_by('unitNumber1'),
      Address=q.ilike(f'%{address}%'),
      unitNumber1=q.ilike(f'%{unit}%'),
    ))
  print("Found " + str(len(unit_matches)) + " unit matches.")
  
  # If there are specific unit matches, show them
  # If not, show the building matches
  if len(unit_matches) > 0:
    return unit_matches
  else:
    return building_units
