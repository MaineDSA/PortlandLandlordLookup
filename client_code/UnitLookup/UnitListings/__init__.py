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

    questiona = 'This unit '
    if self.item['Likely to Exempt'] == True:
      questiona += 'is likely to be kicked off of rent control if Question A passes.'
    else:
      questiona += 'may not be kicked off of rent control if Question A passes.'
      questiona += ' However, if the landlord were to change the ownership structure, it may suffer the same fate as the 4,300 other units we KNOW will no longer be protected.'
    self.questiona.text = questiona

    currentrent = 'The current rent for this '
    currentrent += self.item['nbrBedRms1']
    currentrent += '-bedroom unit is listed as ' + self.item['CurrentRent1']
    if float(self.item['CurrentRent1']) == 0:
      currentrent += ', as your landlord has not reported this appropriately or the Housing Safety Office has not entered it into their systems.'
    else:
      currentrent += '.'
    self.currentrent.text = currentrent

    unitowner = 'The landlord is listed as '
    unitowner += self.item['Owner 1']
    unitowner += self.item['Owner 2']
    unitowner += ' of '
    unitowner += self.item['Owner City']
    unitowner += ', '
    unitowner += self.item['Owner State']
    unitowner += '.'
    self.unitowner.text = unitowner

