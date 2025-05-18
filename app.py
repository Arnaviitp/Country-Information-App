import streamlit as st
import requests

# Configure page
st.set_page_config(page_title="Country Info", page_icon="🌍", layout="centered")

# Function to fetch country data
def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        country_data = data[0]

        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["Unknown"])[0]
        population = country_data.get("population", 0)
        area = country_data.get("area", 0)
        region = country_data.get("region", "Unknown")
        flag = country_data.get("flags", {}).get("png", "")

        currency_data = country_data.get("currencies", {})
        currency = ', '.join([f"{v['name']} ({k})" for k, v in currency_data.items()]) if currency_data else "Unknown"

        return name, capital, population, area, currency, region, flag
    else:
        return None

# Main function
def main():
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🌍 Country Information App</h1>", unsafe_allow_html=True)

    country_name = st.text_input("🔎 Enter a Country Name:")

    if country_name:
        country_info = fetch_country_data(country_name)

        if country_info:
            name, capital, population, area, currency, region, flag = country_info

            # Display flag
            if flag:
                st.image(flag, width=150, caption=f"Flag of {name}")

            # Styled country info card
            st.markdown(f"""
                <div style='
                    background-color: #f9f9f9;
                    border-radius: 12px;
                    padding: 20px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                    font-size: 18px;
                    line-height: 1.8;
                    color: #222222;
                '>
                    <p><strong>🗺️ Country:</strong> {name}</p>
                    <p><strong>🏛️ Capital:</strong> {capital}</p>
                    <p><strong>👥 Population:</strong> {population:,}</p>
                    <p><strong>📐 Area:</strong> {area:,} sq. km</p>
                    <p><strong>💱 Currency:</strong> {currency}</p>
                    <p><strong>🌐 Region:</strong> {region}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Country data not found. Please check the name.")

# Run the app
if __name__ == "__main__":
    main()
