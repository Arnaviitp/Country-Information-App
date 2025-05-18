
# 🌍 Country Information App

A stylish and interactive web app built with **Streamlit** to fetch and display real-time information about any country using the [REST Countries API](https://restcountries.com/).

## 🚀 Features

- 🌐 Fetch real-time data for any country
- 🏳️ Displays country flag
- 🏛️ Shows capital, population, area, currency, and region
- 🎨 Beautiful, responsive UI styled using custom HTML and CSS
- ⚙️ Error-handling for invalid country names

## 🖥️ Preview

![Screenshot](screenshot.png) <!-- Replace with actual screenshot filename -->

## 🛠️ Technologies Used

- Python
- [Streamlit](https://streamlit.io/)
- REST Countries API

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/country-info-app.git
   cd country-info-app
   ```

2. **Install dependencies**:
   ```bash
   pip install streamlit requests
   ```

3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## 📝 How It Works

- The app takes a country name as input.
- It calls the REST Countries API to retrieve country data.
- It then displays a well-designed card with all the key info and the country's flag.

## 📄 Example

Try searching for:
- `India`
- `Japan`
- `France`
- `Brazil`

## 📌 Notes

- The app handles missing values gracefully.
- Works well in both light and dark Streamlit themes.

## 📃 License

MIT License. Feel free to fork and customize!

---

Made with ❤️ by Arnav
