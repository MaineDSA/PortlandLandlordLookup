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

    self.unittitle.text = f"{self.item['Address']}, {self.item['unitNumber1']}"
    
    questiona = '**This unit '
    if (self.item['Exmption'] == '2to4 unit building one of which landlord occupies'):
      questiona += 'is already exempt as the landlord claims to live in the building.'
    elif (self.item['Likely to Exempt'] == True):
      questiona += 'is likely to be kicked off of rent control if Question A passes.**'
    else:
      questiona += 'may not be kicked off of rent control if Question A passes.**'
    self.questiona.content = questiona
    self.questionadisclaimer.visible = (self.item['Likely to Exempt'] == False)

    currentrent = f"The official rent for this {self.item['nbrBedRms1']}-bedroom unit as of November 2022 was ${self.item['CurrentRent1']}."
    if (float(self.item['CurrentRent1']) == 0) or (float(self.item['nbrBedRms1']) == 0):
      currentrent += ' Some reasons for the missing information could be: some types of exempt units, improper reporting, or data issues from the Housing Safety Office.'
    self.currentrent.text = currentrent

    owner2 = ''
    if self.item['Owner2']:
      owner2 += f" "
    self.unitowner.text = f"The landlord is listed as {self.item['Owner1']} {owner2}of {self.item['Owner City']}, {self.item['Owner State']}."

    self.viewlandlord.url = "https://no-on-a.anvil.app/#?l=" + self.item['Owner1']
