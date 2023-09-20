from ._anvil_designer import NavigationTemplate
from anvil import *
import anvil.server
from ..LandlordLookup import LandlordLookup
from ..UnitLookup import UnitLookup

class Form1():
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # set each Link's `tag.form_to_open` attribute to an instance of the Form you want to open
    self.unit_link.tag.form_to_open = UnitLookup()
    self.landlord_link.tag.form_to_open = LandlordLookup()

  def nav_link_click(self, **event_args):
    """A generalised click handler that you can bind to any nav link."""
    # Find out which Form this Link wants to open
    form_to_open = event_args['sender'].tag.form_to_open

    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)