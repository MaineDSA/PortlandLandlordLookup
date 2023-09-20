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

  def query_lookup(self):
    # Give up if no address is supplied
    if not self.textbox_address.text:
      Notification("No street address entered.")
      return False

    found_units = anvil.server.call('find_units', address=self.textbox_address.text, unit=self.textbox_address_unit.text)
    if not found_units:
      self.tenantcontact.visible = False
      return False
    self.units.items = found_units
    Notification('Found ' + str(len(self.units.items)) + 'matching units.')

    if len(self.units.items) > 0:
      self.tenantcontact.visible = True

  # Triggering when button is clicked
  def search_click(self, **event_args):
    self.query_lookup()

  def textbox_landlord_pressed_enter(self, **event_args):
    self.query_lookup()

  def lookupunits_click(self, **event_args):
    open_form('UnitLookup')
