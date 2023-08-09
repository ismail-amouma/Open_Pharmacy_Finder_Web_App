from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def if_exist(key, dict):
    if key in dict:
        return dict[key]
    else:
        return None

def get_countries():
    return {
        "us": "United States",
        "ca": "Canada",
        "uk": "United Kingdom",
        "au": "Australia",
        "nz": "New Zealand",
        "ie": "Ireland",
        "in": "India",
        "jp": "Japan",
        "cn": "China",
        "fr": "France",
        "de": "Germany",
        "it": "Italy",
        "es": "Spain",
        "mx": "Mexico",
        "br": "Brazil",
        "ar": "Argentina",
        "za": "South Africa",
        "eg": "Egypt",
        "ng": "Nigeria",
        "ke": "Kenya",
        "sa": "Saudi Arabia",
        "ae": "United Arab Emirates",
        "kw": "Kuwait",
        "qa": "Qatar",
        "tr": "Turkey",
        "th": "Thailand",
        "vn": "Vietnam",
        "sg": "Singapore",
        "id": "Indonesia",
        "ph": "Philippines",
        "my": "Malaysia",
        "pk": "Pakistan",
        "bd": "Bangladesh",
        "lk": "Sri Lanka",
        "np": "Nepal",
        "bd": "Bangladesh",
        "ua": "Ukraine",
        "ru": "Russia",
        "pl": "Poland",
        "se": "Sweden",
        "no": "Norway",
        "dk": "Denmark",
        "fi": "Finland",
        "nl": "Netherlands",
        "be": "Belgium",
        "ch": "Switzerland",
        "at": "Austria",
        "gr": "Greece",
        "hu": "Hungary",
        "ma": "Morocco",

        # Add more countries and codes as needed
    }

def get_data(city, country):
    url = "https://google.serper.dev/places"
    payload = json.dumps({
        "q": f"open pharmacy in {city}",
        "gl": country,
        "page": 15
    })
    headers = {
        'X-API-KEY': #Your API KEY HERE ,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    pharmacies = [{"title": if_exist("title", pharmacy), 'address': if_exist("address", pharmacy),
                   'phoneNumber': if_exist("phoneNumber", pharmacy),
                   'mapsLink': f"https://www.google.com/maps/search/?api=1&query={pharmacy['title']}+{pharmacy['address']}"}  for pharmacy in data['places']]
    return pharmacies

@app.route('/', methods=['GET', 'POST'])
def main():
    countries = get_countries()

    if request.method == 'POST':
        selected_country = request.form['country']
        selected_city = request.form['city']
        pharmacies = get_data(selected_city, selected_country)
        return render_template('index.html', pharmacies=pharmacies,countries=countries)
    else:
        return render_template('index.html', countries=countries)

if __name__ == "__main__":
    app.run(debug=True)
