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

    liveinlandlord = (self.item['Exmption'] == '2to4 unit building one of which landlord occupies')
    
    self.unittitle.text = self.item['Address'] + ', ' + self.item['unitNumber1']

    questiona = 'This unit '
    if (liveinlandlord):
      questiona += 'is already exempt as the landlord claims to live in the building.'
    elif (self.item['Likely to Exempt'] == True):
      questiona += '**is** likely to be kicked off of rent control if Question A passes.'
    else:
      questiona += '**may not be** kicked off of rent control if Question A passes.'
      questiona += ' However, if the landlord changes the ownership structure this unit could easily suffer the same fate as the 4,300 other units we have identified as likely to lose protections.'
    self.questiona.content = questiona

    currentrent = 'The official rent for this '
    currentrent += self.item['nbrBedRms1']
    currentrent += '-bedroom unit as of November 2022 was $' + self.item['CurrentRent1'] + '.'
    if (float(self.item['CurrentRent1']) == 0) or (float(self.item['nbrBedRms1']) == 0):
      currentrent += ' Some reasons for the missing information could be: improper reporting, some types of exempt units, or data issues from the Housing Safety Office.'
    self.currentrent.text = currentrent

    unitowner = 'The landlord is listed as '
    unitowner += self.item['Owner1']
    if self.item['Owner2']:
      unitowner += ' ' + self.item['Owner2']
    unitowner += ' of '
    unitowner += self.item['Owner City']
    unitowner += ', '
    unitowner += self.item['Owner State']
    unitowner += '.'
    self.unitowner.text = unitowner

    self.viewlandlord.url = "https://no-on-a.anvil.app/#?l=" + self.item['Owner1']
