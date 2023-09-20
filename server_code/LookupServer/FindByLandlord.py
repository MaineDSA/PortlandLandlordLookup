from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def find_by_landlord(**kwargs):
  landlord = str(kwargs.get('landlord', None))

  # Find all units that match the landlord name
  units = app_tables.units.search(q.any_of(
      #tables.order_by('unitNumber1'),
      Owner1=q.ilike(f'%{landlord}%'),
      Owner2=q.ilike(f'%{landlord}%'),
    ))
  print("Found " + str(len(units)) + " units.")

  landlord_addresses = {}
  for unit in units:
    landlord_addresses[unit["Address"]] = unit
    
  print('Found ' + str(len(landlord_addresses)) + 'addresses listed.')

  # Give up if no units found at address 
  if len(landlord_addresses) == 0:
    return False
  
  return landlord_addresses