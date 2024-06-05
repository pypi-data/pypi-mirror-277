from src.app import Vinted

app = Vinted.Vinted()

print(app.get_user_reviews("34311177"))