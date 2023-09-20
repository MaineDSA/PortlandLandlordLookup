from ._anvil_designer import LandlordBuildingsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import navigator

class LandlordBuildings(LandlordBuildingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.address.text = 'test'
    self.numberofrentalunits.text = 0

  def copylink_click(self, **event_args):
    navigator.clipboard.writeText("Hello World!")


