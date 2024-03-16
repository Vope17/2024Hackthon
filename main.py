from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

attractions_data = []
headers = {
    'accept' : 'application/json'
}
Attractions_filter = ["address", "category", "elong", "nlat", "email", "images", "introduction", "name", "official_site", "open_time", "remind", "service", "tel", "ticket", "url"]
def filter(data):
    new_data = []
    for d in data:
        new_dict = dict()
        for k, v in d.items():
            if k in Attractions_filter:
                new_dict.update({k : v})
        new_data.append(new_dict) 

    return new_data 
            
# Get Event Data
def Get_Attractions_Data():
    api_base_url = "https://www.travel.taipei/open-api/zh-tw/Attractions/All"
    try:
        response = requests.get(api_base_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            new_data = filter(data["data"])
            return new_data
    except Exception as e:
        return f'error:${e}'

# 回傳Data
@app.route("/attractions", methods=["GET"])
def send_attractions_data():
    attractions_data = Get_Attractions_Data()
    return attractions_data

if __name__ == '__main__':
    app.run(debug=True)
    print(attractions_data)
