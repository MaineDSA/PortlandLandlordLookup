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

    if self.item['Owner2']:
      self.item['Owner2'] += " "
    self.landlord.text = f"{self.item['Owner1']} {self.item['Owner2']}of {self.item['Owner City']}, {self.item['Owner State']}."
    
    self.unitclass.text = self.item['Class']
    self.landuse.text = self.item['Land Use Code']

    if self.item['Exmption'] == '2to4 unit building one of which landlord occupies':
      self.landlordlivesthere.text = "claims to"
    else:
      self.landlordlivesthere.text = "may not"
    self.viewunits.url = "https://no-on-a.anvil.app/#?a=" + self.item['Address']