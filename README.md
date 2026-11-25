# 🌆 Python City Info App (PyQt5)

A modern, lightweight desktop application built using **Python** and **PyQt5**. Designed as a cleaner, faster alternative to searching the web for basic city details, this app integrates the OpenTripMap API to deliver instant location information for cities around the world.

---

## ✨ Features

* **🌍 Global City Search:** Look up location data for any city worldwide.
* **🕒 Timezone Lookup:** Displays the exact timezone of the city (e.g., *Asia/Kolkata*).
* **📍 Coordinates at a Glance:** Shows accurate **latitude** and **longitude** values for the searched city.
* **⚠️ Friendly Error Handling:** Clear messages for invalid cities, wrong API keys, no internet, timeouts and server errors.
* **🔐 Secure API Key:** Your key stays in a private `.env` file, never inside the source code.
* **🖥️ Modern GUI:** Built from scratch with **PyQt5** for a clean, dark-themed desktop experience.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **UI Framework:** PyQt5
* **Data Source:** OpenTripMap API (JSON / REST)
* **Libraries:** `requests`, `python-dotenv`

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.10 or higher installed (the code uses `match` / `case`), along with `PyQt5`, `requests` and `python-dotenv`:

```bash
pip install PyQt5 requests python-dotenv
```

### 🔑 Get an API Key

1. Go to [opentripmap.com](https://opentripmap.com/product) and sign up for a free API key.
2. Copy your key.

### ⚙️ Setup

1. Clone or download this project:

```bash
git clone https://github.com/your-username/city-info-app.git
cd city-info-app
```

2. Create a file named `.env` in the project folder and add your key:

```
OPENTRIPMAP_API_KEY=your_api_key_here
```

3. Add `.env` to your `.gitignore` so your key is never uploaded:

```
.env
```

### ▶️ Run the App

```bash
python city_api.py
```

---

## 📖 How to Use

1. Enter a city name,
