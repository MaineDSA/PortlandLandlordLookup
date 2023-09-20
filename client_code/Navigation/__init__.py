from ._anvil_designer import NavigationTemplate
from anvil import *
import anvil.server

import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..LandlordLookup import LandlordLookup
from ..UnitLookup import UnitLookup

class Navigation(NavigationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    url_query = get_url_hash()
    if not url_query or not ('l' in url_query):
      self.content_panel.add_component(UnitLookup())
      self.unit_link.role = 'selected'
    else:
      self.content_panel.add_component(LandlordLookup())
      self.landlord_link.role = 'selected'

    # set each Link's `tag.form_to_open` attribute to an instance of the Form you want to open
    self.unit_link.tag.form_to_open = UnitLookup()
    self.landlord_link.tag.form_to_open = LandlordLookup()

  def reset_links(self, **event_args):
    self.unit_link.role = ''
    self.landlord_link.role = ''

  def nav_link_click(self, **event_args):
    # Find out which Form this Link wants to open
    form_to_open = event_args['sender'].tag.form_to_open

    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)

    self.reset_links()
    event_args['sender'].role = 'selected'