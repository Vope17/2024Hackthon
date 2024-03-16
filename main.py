from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

attractions_data = []
headers = {
    'accept' : 'application/json'
}

# Get Event Data
def Get_Event_Data():
    api_base_url = "https://www.travel.taipei/open-api/zh-tw/Attractions/All"
    try:
        response = requests.get(api_base_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
    except Exception as e:
        return f'error:${e}'

# 回傳Data
@app.route("/attractions", methods=["GET"])
def send_attractions_data():
    attractions_data = Get_Event_Data()
    return attractions_data

if __name__ == '__main__':
    app.run(debug=True)
    print(attractions_data)
