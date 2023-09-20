from ._anvil_designer import UnitLookupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class UnitLookup(UnitLookupTemplate):
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
  def submit_click(self, **event_args):
    self.query_lookup()

  def textbox_pressed_enter(self, **event_args):
    self.query_lookup()

  def tenantinfo_submit_click(self, **event_args):
    saved_message = anvil.server.call(
        'save_message',
        firstname=self.tenantname_first.text,
        lastname=self.tenantname_last.text,
        email=self.tenantemail.text,
        story=self.tenantstory.text,
        address=self.textbox_address.text,
        unit=self.textbox_address_unit.text
    )
    if saved_message:
      self.messagesubmitted.visible = True
      self.tenantcontact.visible = False

  def lookuplandlord_click(self, **event_args):
    open_form('LandlordLookup')
