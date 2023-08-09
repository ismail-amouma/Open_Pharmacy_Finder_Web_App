# Open_Pharmacy_Finder_Web_App

The Pharmacy Finder App is a Flask-based web application that allows users to find open pharmacies in a specified city and country. It utilizes the Google Places API to retrieve pharmacy information and presents it in a user-friendly format.

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

2. Change into the project directory:

   ```bash
   cd pharmacy-finder-app
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Obtain a Google Places API key by following the instructions on the [Google Places API documentation](https://developers.google.com/maps/documentation/places/web-service/get-api-key).

2. Replace `'YOUR_API_KEY'` in the `app.py` file with your actual Google Places API key:

   ```python
   'X-API-KEY': 'YOUR_API_KEY',
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your web browser and navigate to `http://localhost:5000` to use the Pharmacy Finder App.

## API Key

In order to use the Pharmacy Finder App, you need to obtain an API key from the Google Places API. Follow the instructions provided by Google to generate an API key and ensure it is kept secure. Replace `'YOUR_API_KEY'` in the `app.py` file with your actual API key.

## Contributing

Contributions to the Pharmacy Finder App are welcome! If you find a bug, want to add a feature, or improve the code, please feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature` or `bugfix/issue-description`.
3. Make your changes and commit them: `git commit -m "Description of changes"`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README to provide more specific information about your application. If you have any questions or need further assistance, please don't hesitate to reach out. Happy coding!
