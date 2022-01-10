import requests

r=requests.get("https://opentdb.com/api.php?amount=30&category=9&type=boolean")
r=r.json()
question_data=r['results']
