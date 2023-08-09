# Open_Pharmacy_Finder_Web_App
![Untitled](https://github.com/ismail-amouma/Open_Pharmacy_Finder_Web_App/assets/91847466/c6bbe128-3aee-4537-9bcf-a8a082c19f3b)

The Pharmacy Finder App is a Flask-based web application that allows users to find open pharmacies in a specified city and country. It utilizes the Serper API to retrieve pharmacy information and presents it in a user-friendly format.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Key](#api-key)
- [Contributing](#contributing)


## Features

- Search for open pharmacies in a specific city and country.
- View pharmacy details including name, address, phone number, and a link to Google Maps.
- Choose from a list of supported countries.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pharmacy-finder-app.git
   ```


2. Install the required dependencies:

   ```bash
   pip install flask
   ```

## Usage

1. Obtain a Serper API  key by following the instructions on the [Try 2,500 queries for free](https://serper.dev/).

2. Replace `'YOUR_API_KEY'` in the `app.py` file with your actual Google Places API key:

   ```python
   'X-API-KEY': 'YOUR_API_KEY',
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your web browser and navigate to `http://localhost:5000` to use the Pharmacy Finder App.

## Contributing

Contributions to the Pharmacy Finder App are welcome! If you find a bug, want to add a feature, or improve the code, please feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature` or `bugfix/issue-description`.
3. Make your changes and commit them: `git commit -m "Description of changes"`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.
