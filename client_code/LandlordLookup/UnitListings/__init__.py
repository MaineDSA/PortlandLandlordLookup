from ._anvil_designer import UnitListingsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class UnitListings(UnitListingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.unittitle.text = self.item['Address'] + ', ' + self.item['unitNumber1']
    self.unitnumber.text = self.item['unitNumber1']
    self.unitaddress.text = self.item['Address']
    self.unitbedrooms.text = self.item['nbrBedRms1']
    self.unitcurrentrent.text = self.item['CurrentRent1']
    if self.item['Likely to Exempt'] == True:
      self.unitislikely.text = 'is likely to'
      self.disclaimer.text = ''
    else:
      self.unitislikely.text = 'may not'
      self.disclaimer.text = 'However, if the landlord were to change the ownership structure, it may suffer the same fate as the 4,300 other units we KNOW will no longer be protected.'
    self.unitowner1.text = self.item['Owner 1']
    self.unitowner2.text = self.item['Owner 2']
    self.unitownercity.text = self.item['Owner City']
    self.unitownerstate.text = self.item['Owner State']

