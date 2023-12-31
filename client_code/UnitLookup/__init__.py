from ._anvil_designer import UnitLookupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import navigator

BYPASS = False

class UnitLookup(UnitLookupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    url_query = get_url_hash()
    if not url_query:
      return
    if 'u' in url_query:
      self.textbox_address_unit.text = url_query['u'].replace('"', '')
    if 'a' in url_query:
      self.textbox_address.text = url_query['a'].replace('"', '')
    if 'b' in url_query:
      BYPASS = True

  def query_lookup(self):
    # Give up if no address is supplied
    if not self.textbox_address.text:
      n = Notification("No street address entered.")
      n.show()
      return False

    self.textcontactustitle.text = 'Contact Us'
    self.textcontactusbody.text = "Want to learn more and help keep Portland tenants safe? Leave your name and email here!"

    found_units = anvil.server.call('find_by_address', address=self.textbox_address.text, unit=self.textbox_address_unit.text)
    if len(found_units) == 0:
      n = Notification("No units found.")
      return False
    elif (len(found_units) == 1) & (found_units[0]['Likely to Exempt'] == True):
      self.textcontactustitle.text = 'Your unit could lose rent control!'
      self.textcontactusbody.text = "Please fill out the below to help prevent that from happening.\nElection day is November 7th. Get involved!"

    self.units.items = found_units
    n = Notification(f"Found {len(self.units.items)} matching units.")
    n.show()

    if self.units.items:
      self.retrievedinfo.visible = True
      self.tenantcontact.visible = True
      self.copylink.visible = True
      return True

    self.retrievedinfo.visible = False
    self.tenantcontact.visible = False
    self.copylink.visible = False

  # Triggering when button is clicked
  def submit_click(self, **event_args):
    self.query_lookup()

  def textbox_pressed_enter(self, **event_args):
    self.query_lookup()

  def tenantinfo_submit_click(self, **event_args):
    saved_message = anvil.server.call(
        'save_message',
        firstname=self.tenantname_first.text,
        lastname=self.tenantname_last.text,
        email=self.tenantemail.text,
        story=self.tenantstory.text,
    )
    if saved_message:
      self.messagesubmitted.visible = True
      self.tenantcontact.visible = False

  def copylink_click(self, **event_args):
    link = f"https://no-on-a.anvil.app/#?a={self.textbox_address.text}&u={self.textbox_address_unit.text}"
    navigator.clipboard.writeText(link)
    n = Notification(f"Copied \"{link}\" to clipboard.", title="Link Copied")
    n.show()