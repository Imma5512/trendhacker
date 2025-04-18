import streamlit as st
from trend_utils import get_google_trends, get_etsy_results
from report_generator import generate_pdf_report
import pandas as pd

st.set_page_config(page_title="TrendHacker", layout="wide")
st.title("📈 TrendHacker - Scopri i prodotti digitali in tendenza")

keyword = st.text_input("Inserisci una parola chiave da analizzare", "")

if keyword:
    with st.spinner("Analisi in corso..."):
        trends = get_google_trends(keyword)
        etsy = get_etsy_results(keyword)
        df_trends = pd.DataFrame(trends, columns=["Data", "Interesse"])
        df_etsy = pd.DataFrame(etsy)

        st.subheader("📊 Tendenze Google")
        st.line_chart(df_trends.set_index("Data"))

        st.subheader("🛍️ Prodotti più venduti su Etsy")
        st.dataframe(df_etsy)

        st.download_button(
            label="📄 Scarica risultati in CSV",
            data=df_etsy.to_csv(index=False),
            file_name=f"{keyword}_etsy.csv",
            mime="text/csv",
        )

        if st.button("📥 Genera PDF Report"):
            pdf = generate_pdf_report(keyword, trends, etsy)
            st.download_button(
                label="Scarica Report PDF",
                data=pdf,
                file_name=f"{keyword}_report.pdf",
                mime="application/pdf",
            )
