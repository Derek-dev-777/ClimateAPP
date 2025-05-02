# 🌤️ Weather Forecast App

A simple and modern weather forecast app built with **Python** and **Flet**.
It allows users to check the current weather in any region of the world and view the forecast for the next 5 days.

---

## 📸 Preview

---![Captura de tela 2025-05-01 234403](https://github.com/user-attachments/assets/cd4d2e8f-c507-4576-a800-7877fdf747f0)

---

## 🚀 Features

* 🔍 Search the weather by city or country
* 📍 Get current location weather using your IP
* 🗕️ 5-day forecast with temperature, description, humidity, and wind
* 🧽 Clean and intuitive UI built with Flet
* 🔐 Environment variables support for secure API key handling

---

## 🛠️ Technologies

* Python 3.10+
* [Flet](https://flet.dev)
* [OpenWeatherMap API](https://openweathermap.org/api)
* `.env` file with `python-dotenv`




## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Derek-dev-777/weather-forecast-app.git
cd weather-forecast-app
```

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file**

```env
API_KEY=your_openweathermap_api_key
```

5. **Run the app**

```bash
python main.py
```

---

## 💡 Notes

* You need an API key from [OpenWeatherMap](https://openweathermap.org/api).
* The app uses IP-based location to guess the user's location.
* Works best in desktop environments (not fully responsive for mobile yet).

---

## 📜 License

This project is licensed under the MIT License. Feel free to use and modify it.
