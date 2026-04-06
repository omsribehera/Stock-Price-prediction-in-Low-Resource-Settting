# --- IMPORTS ---
import streamlit as st
import pandas as pd
import numpy as np
import os

# Import functions
from Import_Functions_Deployed import *

# --- PAGE CONFIG ---
st.set_page_config(page_title="Stock Prediction")

# --- DATA PATH ---
DATASET_DIR = "Codes/Historical_Data_Analysis/Preprocessed_Dataset"

# --- MAIN FUNCTION ---
def main():
    st.title("📈 Stock Market Prediction")

    # Sidebar
    st.sidebar.title("Explore")

    selected_section = st.sidebar.radio(
        "Go to",
        [
            "Stock Market Description 📈",
            "Project Description 🧾",
            "Companies 🏢",
            "Numerical Dataset Visualization 📊",
            "Numerical Model Prediction 🎯",
        ],
    )

    # ------------------ SECTIONS ------------------

    if selected_section == "Stock Market Description 📈":
        display_stock_market_description()

    elif selected_section == "Project Description 🧾":
        display_project_description()

    elif selected_section == "Companies 🏢":
        display_company_data_table()

    elif selected_section == "Numerical Dataset Visualization 📊":
        ticker = st.sidebar.selectbox(
            "Select Stock",
            ["AAPL", "GOOG", "AMZN", "MSFT"]
        )

        try:
            file_path = os.path.join(
                DATASET_DIR,
                f"Preprocessed_{ticker}_Dataset.csv"
            )

            df = pd.read_csv(file_path)

            st.subheader(f"{ticker} Closing Price")

            st.line_chart(df["close"])

        except Exception as e:
            st.error(f"Error loading dataset: {e}")

    elif selected_section == "Numerical Model Prediction 🎯":
        ticker = st.sidebar.selectbox(
            "Select Stock",
            ["AAPL", "GOOG", "AMZN", "MSFT"]
        )

        st.subheader(f"Predict {ticker} Closing Price")

        open_price = st.number_input("Open Price")
        high = st.number_input("High Price")
        low = st.number_input("Low Price")
        volume = st.number_input("Volume")

        if st.button("Predict"):
            display_numerical_model_predicted(
                ticker, open_price, high, low, volume
            )

# --- RUN APP ---
if __name__ == "__main__":
    display_background_image(
        "https://vectormine.b-cdn.net/wp-content/uploads/Stock_Market.jpg",
        0.8,
    )
    main()