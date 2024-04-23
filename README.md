Restaurant Data Fetch and Display Application

---

Overview:

This application fetches restaurant data from an external API for a particular postal code in the United Kingdom. It then displays this data including restaurant name, address, cuisine, and ratings in a user-friendly format.

---

Usage:

1. Setup:
   - Ensure you have and IDE and python interpreter installed on your system.
   - Install Flask and requests libraries using pip:
     ```
     pip install Flask requests
     ```

2. Running the Application:
   - Change the directory in your terminal to your project directory. 
   - Execute the Python script `main.py` in your terminal:
     ```
     python main.py
     ```
   - By default, the application will run on `http://127.0.0.1:5000/` in your web browser.
   - Headers are mandatory to ensure the data fetch goes through from the API without authentication error 403
     ``` 
     headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 }
     ```
3. Using the Application:
   - Run the application and open the link `http://127.0.0.1:5000/` on your browser.
   - The application will fetch restaurant data based on the provided postal code at the end of the API Url and display it on the webpage.
   - As a standard, the postal code used is for EC4M7RF, so postal code = EC4M7RF. This can be changed to suit the user requirements by replacing EC4M7RF with other postal codes in United Kingdom.
     ```
     url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postal code}"
     ```
   - Only United Kingdom postal codes are valid to fetch the data from the API
   - Each restaurant name is clickable. Clicking on a restaurant name will reveal additional details including its rating and address.

---

Files:

1. main.py: This Python script contains the Flask application code. It fetches restaurant data from the external API and renders the HTML template.

2. index.html: This HTML file defines the structure of the webpage and contains the template for displaying restaurant data fetched by the Flask application.

---

API Used:

- The application uses the Just Eat API (https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/) to fetch restaurant data based on the provided postal code.

---

Dependencies:

- Flask: Python web framework used to create the web application.
- requests: Python library used to send HTTP requests to the Just Eat API and retrieve data.

---

Styling:

- The application uses simple styling for a clean and user-friendly interface.
- Colors and fonts have been chosen for readability and aesthetic appeal.
- Links used from W3 schools for styling
  ```
  "https://www.w3schools.com/w3css/4/w3.css"
  ```
---

Note:

- Ensure a stable internet connection to fetch data from the external API.
- The application fetches and displays the data for the first 10 restaurants only.

---

Contributors:

- This application was created by Karthik Kolar Sudhindra.
- W3 Schools for styling, rendering of the web interface and colour selection

---

Held back on:

-Headers were a point of concern and learning without which I could not have run past the authentication error 403

---

Possible improvements:

-Search bar to include the search for cuisines and restaurants at different postal codes
-A drop down filter for postal codes in the UK that helps filtering during search for all postal codes. This would eliminate updating the API at the code level everytime to accesss data for all restaurants
-Multi page model to include all restaurants with 10 restaurants in each page
-More interactive UI

---
