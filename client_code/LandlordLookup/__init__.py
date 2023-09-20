from ._anvil_designer import LandlordLookupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LandlordLookup(LandlordLookupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    url_query = get_url_hash()
    if url_query:
      if 'l' in url_query:
        self.textbox_landlord.text = url_query['l']
        self.query_lookup()

  def query_lookup(self):
    # Give up if no address is supplied
    if not self.textbox_landlord.text:
      Notification("No landlord name entered.")
      return False

    found_buildings = anvil.server.call('find_by_landlord', landlord=self.textbox_landlord.text)
    if not found_buildings:
      self.retrievedinfo.visible = False
      return False
    Notification('Found ' + str(len(found_buildings)) + 'matching units.')

    landlord_addresses = {}
    for unit in found_buildings:
      landlord_addresses[unit["Address"]] = unit
    
    Notification('Found ' + str(len(self.buildings.items)) + 'addresses listed.')
    self.buildings.items = landlord_addresses

    if len(self.buildings.items) > 0:
      self.retrievedinfo.visible = True

  # Triggering when button is clicked
  def search_click(self, **event_args):
    self.query_lookup()

  def textbox_pressed_enter(self, **event_args):
    self.query_lookup()