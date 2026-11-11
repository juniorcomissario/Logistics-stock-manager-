
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Logistics Manager", layout="wide")

st.title("📦 Logistics Stock Manager")
st.write("Inventory control and replenishment system")

dados = pd.DataFrame({
    "Product": ["Rice", "Oil", "Sugar", "Flour"],
    "Current Stock": [120, 25, 80, 15],
    "Minimum Stock": [50, 40, 30, 25],
    "Unit Price (MZN)": [100, 150, 80, 120]
})

dados = st.data_editor(dados, num_rows="dynamic")

dados["To Order"] = (
    dados["Minimum Stock"] * 2 - dados["Current Stock"]
).clip(lower=0)

dados["Replenishment Cost"] = (
    dados["To Order"] * dados["Unit Price (MZN)"]
)

st.subheader("Stock Report")

col1, col2, col3 = st.columns(3)

col1.metric("Products", len(dados))
col2.metric("Products to replenish",
            int((dados["To Order"] > 0).sum()))
col3.metric("Total Cost",
            f'{dados["Replenishment Cost"].sum():,.2f} MZN')

st.dataframe(dados, use_container_width=True)

st.download_button(
    "Download Stock Report",
    dados.to_csv(index=False),
    "stock_report.csv",
    "text/csv"
)
