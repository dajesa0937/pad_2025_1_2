import streamlit as st
import pandas as pd
import altair as alt
import os
from ydata_profiling import ProfileReport  # ✅ IMPORT CORRECTO
from streamlit_pandas_profiling import st_profile_report  # ✅ PARA STREAMLIT

def main():
    # ✅ Cargar el CSV
    df = pd.read_csv("src/edu_pad/static/csv/data_extractor.csv")

    # ✅ Crear el informe de perfil
    pr = ProfileReport(df, title="Reporte de Perfil Financiero", explorative=True)

    # ✅ Mostrar en Streamlit
    st.title("Dashboard Financiero 📊")
    st_profile_report(pr)

if __name__ == "__main__":
    st.set_page_config(page_title="Dashboard Financiero", page_icon="🎈", layout="wide")
    main()
