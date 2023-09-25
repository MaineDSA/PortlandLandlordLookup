from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import re

@anvil.server.callable
def find_by_address(**kwargs):
  address = str(kwargs.get('address', None))
  unit = str(kwargs.get('unit', None))
  
  # Find all units that match the address
  building_units = app_tables.units.search(
      #tables.order_by('unitNumber1'),
      Address=q.ilike(f'%{address}%'),
    )
  print("Found " + str(len(building_units)) + " building matches.")
  
  if len(building_units) == 0:
    address_parts = re.split('^(\d+)', address, 1)
    if len(address_parts) > 1:
      prev_address = str(int(address_parts[1]) - 2) + address_parts[2]
      next_address = str(int(address_parts[1]) + 2) + address_parts[2]
      # Find all units that match the address
      building_units = app_tables.units.search(
          #tables.order_by('unitNumber1'),
          Address=q.any_of(
              q.ilike(f'%{prev_address}%'),
              q.ilike(f'%{next_address}%'),
            )
        )
      print("Found " + str(len(building_units)) + " building matches.")

  if len(building_units) == 0:
    return building_units
  
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

  return building_units