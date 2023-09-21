from ._anvil_designer import LandlordLookupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import navigator

class LandlordLookup(LandlordLookupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    url_query = get_url_hash()
    if url_query:
      if 'l' in url_query:
        self.textbox_landlord.text = url_query['l']
        self.query_lookup()

  def query_lookup(self):
    # Give up if no address is supplied
    if not self.textbox_landlord.text:
      n = Notification()("No landlord name entered.")
      n.show()
      return False

    found_buildings = anvil.server.call('find_by_landlord', landlord=self.textbox_landlord.text)
    if not found_buildings:
      return False
    self.buildings.items = found_buildings
    n = Notification('Found ' + str(len(self.buildings.items)) + ' matching buildings.')
    n.show()

    if self.buildings.items:
      self.retrievedinfo.visible = True
      self.copylink.visible = True
    else:
      self.retrievedinfo.visible = False
      self.copylink.visible = False

  # Triggering when button is clicked
  def search_click(self, **event_args):
    self.query_lookup()

  def textbox_pressed_enter(self, **event_args):
    self.query_lookup()

  def copylink_click(self, **event_args):
    link = "https://no-on-a.anvil.app/#?l=" + self.textbox_landlord.text
    navigator.clipboard.writeText(link)
    n = Notification(content="Copied " + link + " to clipboard.", title="Search Complete", large=False)
    n.show()