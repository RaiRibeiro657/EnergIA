import streamlit as st
import pandas as pd
import requests

API_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="EnergIA", layout="wide")

st.title("⚡ EnergIA - Painel de Energia")

try:
    response = requests.get(f"{API_URL}/status").json()
except:
    st.error("Não foi possível conectar à API. Verifique se o Flask está rodando.")
    st.stop()

battery = response['battery_level']
carga_critica = response['carga_critica']
carga_secundaria = response['carga_secundaria']

st.subheader("🔋 Nível da Bateria")
st.progress(battery / 100)
st.write(f"{battery}%")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Carga Crítica")
    st.metric(label="Status", value="Ligada" if carga_critica else "Desligada")
with col2:
    st.subheader("Carga Secundária")
    st.metric(label="Status", value="Ligada" if carga_secundaria else "Desligada")

st.subheader("Controle Manual")
col1, col2 = st.columns(2)
with col1:
    if st.button("Desligar Carga Crítica"):
        requests.post(f"{API_URL}/update", json={"carga_critica": False})
with col2:
    if st.button("Ligar Carga Crítica"):
        requests.post(f"{API_URL}/update", json={"carga_critica": True})

col1, col2 = st.columns(2)
with col1:
    if st.button("Desligar Carga Secundária"):
        requests.post(f"{API_URL}/update", json={"carga_secundaria": False})
with col2:
    if st.button("Ligar Carga Secundária"):
        requests.post(f"{API_URL}/update", json={"carga_secundaria": True})

st.subheader("📈 Histórico da Bateria")
data = {
    "Tempo": ["12:00", "12:05", "12:10", "12:15"],
    "Bateria": [100, 98, 95, 93]
}
df = pd.DataFrame(data)
st.line_chart(df.set_index("Tempo"))
