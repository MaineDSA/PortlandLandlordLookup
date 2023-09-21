from ._anvil_designer import BuildingUnitsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import navigator

class BuildingUnits(BuildingUnitsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.unittitle.text = self.item['Address'] + ', ' + self.item['unitNumber1']

    questiona = 'This unit '
    if self.item['Likely to Exempt'] == True:
      questiona += 'is likely to be kicked off of rent control if Question A passes.'
    else:
      questiona += 'may not be kicked off of rent control if Question A passes.'
      questiona += ' However, if the landlord changes the ownership structure this unit could easily suffer the same fate as the 4,300 other units we have identified as likely to lose protections.'
    self.questiona.text = questiona

    currentrent = 'The official rent for this '
    currentrent += self.item['nbrBedRms1']
    currentrent += '-bedroom unit as of November 2022 was $' + self.item['CurrentRent1']
    if self.item['CurrentRent1'] == "":
      currentrent += '.'
    elif float(self.item['CurrentRent1']) == 0:
      currentrent += ', as the landlord has not reported this appropriately, the unit is exempt, or the Housing Safety Office has not entered it into their systems.'
    else:
      currentrent += '.'
    self.currentrent.text = currentrent

    unitowner = 'The landlord is listed as '
    unitowner += self.item['Owner1']
    unitowner += self.item['Owner2']
    unitowner += ' of '
    unitowner += self.item['Owner City']
    unitowner += ', '
    unitowner += self.item['Owner State']
    unitowner += '.'
    self.unitowner.text = unitowner
    self.unitowner.url = "https://no-on-a.anvil.app/#?l=" + self.item['Owner1']

