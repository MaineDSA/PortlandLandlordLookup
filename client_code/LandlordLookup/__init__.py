from ._anvil_designer import LandlordLookupTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LandlordLookup(LandlordLookupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def query_lookup(self):
    # need at least an address
    if self.textbox_address.text != "":
      building_units = app_tables.units.search(
          Address=q.ilike(f'%{self.textbox_address.text}%')
        )
      print("Found " + str(len(building_units)) + " building matches.")
      if len(building_units) > 0:
        unit_matches = app_tables.units.search(q.all_of(
            Address=q.ilike(f'%{self.textbox_address.text}%'),
            unitNumber1=q.ilike(f'%{self.textbox_address_unit.text}%')
          ))
        print("Found " + str(len(unit_matches)) + " unit matches.")
        if len(unit_matches) > 0:
          self.units.items = unit_matches
        else:
          self.units.items = building_units

  def submit_click(self, **event_args):
    self.query_lookup()

  def textbox_address_pressed_enter(self, **event_args):
    self.query_lookup()

  def textbox_address_unit_pressed_enter(self, **event_args):
    self.query_lookup()

