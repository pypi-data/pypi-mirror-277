from pythed.app import Vinted

app = Vinted.Vinted()

print(app.search_items(page=1, search_text="Jordan", perPage=10))