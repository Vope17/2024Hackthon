from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

attractions_data = []
headers = {
    'accept' : 'application/json'
}
Attractions_filter = ["address", "category", "elong", "nlat", "email", "images", "introduction", "name", "official_site", "open_time", "remind", "service", "tel", "ticket", "url"]
Events_filter = ["elong", "nlat", "tltle", "description", "begin", "end", "url", "links"]
def _filter(data, switch):
    new_data = []
    for d in data:
        new_dict = dict()
        for k, v in d.items():
            if switch == 0:
                if k in Attractions_filter:
                    new_dict.update({k : v})
            else:
                if k in Events_filter:
                    new_dict.update({k : v})

        new_data.append(new_dict) 

    return new_data 

    
# Get Data
def Get_Data(switch):
    api_base_url = ""
    if switch == 0:
        api_base_url = "https://www.travel.taipei/open-api/zh-tw/Attractions/All"
    else:
        api_base_url = "https://www.travel.taipei/open-api/zh-tw/Events/Activity"

    try:
        response = requests.get(api_base_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            new_data = _filter(data["data"], switch)
            return new_data
    except Exception as e:
        return f'error:${e}'

# 回傳Data
@app.route("/attractions", methods=["GET"])
def send_attractions_data():
    attractions_data = Get_Data(0)
    return attractions_data

@app.route("/events", methods=["GET"])
def send_events_data():
    events_data = Get_Data(1)
    return events_data 

if __name__ == '__main__':
    app.run(debug=True)
    print(attractions_data)
