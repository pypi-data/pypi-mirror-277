from pythed.app import Vinted

app = Vinted.Vinted()

print(app.get_shipping_details(item_id="4596708317"))