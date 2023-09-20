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

    self.address.text = self.item['Address']
    self.numberofrentalunits.text = self.item['NumberOfRentalUnits']
    self.viewunits.url = "https://no-on-a.anvil.app/#?a=" + self.item['Address']