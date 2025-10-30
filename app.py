import streamlit as st
from scipy.stats import hypergeom

st.set_page_config(page_title="Calculadora Hipergeométrica", layout="centered")
st.title("📊 Calculadora de Distribución Hipergeométrica")

st.write("Introduce los valores y presiona **Calcular**.")

N = st.number_input("Tamaño de la población (N):", min_value=1, value=20)
K = st.number_input("Número de éxitos en la población (K):", min_value=0, value=8)
n = st.number_input("Tamaño de la muestra (n):", min_value=1, value=5)
x = st.number_input("Número de éxitos deseados (x):", min_value=0, value=3)

tipo = st.selectbox("Tipo de probabilidad:", ["Exactamente x", "No más de x", "Al menos x"])

if st.button("Calcular"):
    rv = hypergeom(N, K, n)
    if tipo == "Exactamente x":
        prob = rv.pmf(x)
        texto = f"P(X={x}) = {prob:.6f} ({prob*100:.2f}%)"
    elif tipo == "No más de x":
        prob = rv.cdf(x)
        texto = f"P(X ≤ {x}) = {prob:.6f} ({prob*100:.2f}%)"
    else:
        prob = 1 - rv.cdf(x-1) if x > 0 else 1.0
        texto = f"P(X ≥ {x}) = {prob:.6f} ({prob*100:.2f}%)"

    st.success(texto)
    st.write(f"**Media:** {rv.mean():.3f}")
    st.write(f"**Varianza:** {rv.var():.3f}")
