# Freight Fare Finder 🚚

A Python Flask-based web application that compares estimated freight transportation fares across multiple transport providers.

## 📌 Project Overview

Freight Fare Finder helps users compare estimated transportation costs based on pickup location, drop location, vehicle type, and travel distance.

The application calculates fares from sample provider rates and highlights the lowest available fare.

## ✨ Features

- Enter pickup and drop locations.
- Select Mini Truck or Large Truck.
- Enter transportation distance in kilometres.
- Compare fares from three transport providers.
- Automatically identify the lowest fare.
- Handle equal lowest-fare results.
- Validate user inputs and display error messages.
- Responsive user interface.

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS

## 📂 Project Structure

```text
FREIGHT_FARE_FINDER/
│
├── app.py
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd freight-fare-finder
```

### 3. Install Flask

```bash
python -m pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

```text
http://127.0.0.1:5000
```

## 🧮 Fare Calculation

**Estimated Fare = Base Fare + (Distance × Rate per KM)**

The provider with the lowest calculated fare is highlighted.

## ⚠️ Note

This project currently uses sample transportation rates for demonstration purposes. It does not fetch live transport-provider quotations.

## 👨‍💻 Author

**Abufaizal**

Computer Science and Engineering

GitHub: [https://github.com/AbuFaizal2408](https://github.com/AbuFaizal2408)