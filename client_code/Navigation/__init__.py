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

    # set each Link's `tag.form_to_open` attribute to an instance of the Form you want to open
    self.unit_link.tag.form_to_open = UnitLookup()
    self.landlord_link.tag.form_to_open = LandlordLookup()

    url_query = get_url_hash()
    if not url_query or not ('l' in url_query):
      self.content_panel.add_component(self.unit_link.tag.form_to_open)
      self.unit_link.role = 'selected'
      # nav_link_click(self, sender=self.unit_link)
    else:
      self.content_panel.add_component(self.landlord_link.tag.form_to_open)
      self.landlord_link.role = 'selected'
      # nav_link_click(self, sender=self.landlord_link)

  def reset_links(self, **event_args):
    self.unit_link.role = ''
    self.landlord_link.role = ''

  def nav_link_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(event_args['sender'].tag.form_to_open)

    self.reset_links()
    event_args['sender'].role = 'selected'