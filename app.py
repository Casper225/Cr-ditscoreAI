import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ─── CONFIG PAGE ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CréditScore AI",
    page_icon="🏦",
    layout="centered"
)

# ─── CSS PERSONNALISÉ ───────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Fond général */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    font-family: 'Inter', sans-serif;
}

/* Cacher éléments Streamlit par défaut */
#MainMenu, footer, header { visibility: hidden; }

/* Titre principal */
.hero-title {
    text-align: center;
    font-size: 2.4rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.5px;
    margin-bottom: 0.2rem;
}
.hero-sub {
    text-align: center;
    font-size: 1rem;
    color: #a0a8c8;
    margin-bottom: 2rem;
    font-weight: 300;
}

/* Carte principale */
.card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 2rem;
    backdrop-filter: blur(10px);
    margin-bottom: 1.5rem;
}

/* Section label */
.section-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #7c85b3;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

/* Labels des inputs */
label, .stSelectbox label, .stNumberInput label, .stSlider label {
    color: #c8cee8 !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
}

/* Inputs */
.stSelectbox > div > div,
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: #ffffff !important;
}

/* Bouton */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.85rem 2rem;
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 0.02em;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 1rem;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

/* Résultat accordé */
.result-accordé {
    background: linear-gradient(135deg, rgba(16,185,129,0.2), rgba(5,150,105,0.1));
    border: 1px solid rgba(16,185,129,0.4);
    border-radius: 16px;
    padding: 1.8rem;
    text-align: center;
}
.result-accordé h2 { color: #10b981; font-size: 1.8rem; margin: 0.5rem 0; }

/* Résultat refusé */
.result-refusé {
    background: linear-gradient(135deg, rgba(239,68,68,0.2), rgba(185,28,28,0.1));
    border: 1px solid rgba(239,68,68,0.4);
    border-radius: 16px;
    padding: 1.8rem;
    text-align: center;
}
.result-refusé h2 { color: #ef4444; font-size: 1.8rem; margin: 0.5rem 0; }

.result-icon { font-size: 3rem; }
.result-prob { color: #a0a8c8; font-size: 0.9rem; margin-top: 0.5rem; }

/* Slider */
.stSlider > div > div > div { color: #667eea !important; }
</style>
""", unsafe_allow_html=True)


# ─── CHARGEMENT DU MODÈLE ──────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    model  = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

try:
    model, scaler = load_model()
    model_loaded = True
except:
    model_loaded = False


# ─── EN-TÊTE ───────────────────────────────────────────────────────────────────
st.markdown('<p class="hero-title">🏦 CréditScore AI</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">Évaluation intelligente de demande de prêt</p>', unsafe_allow_html=True)


# ─── FORMULAIRE ────────────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="section-label">Profil du demandeur</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    gender    = st.selectbox("Genre", ["Male", "Female"])
    married   = st.selectbox("Situation matrimoniale", ["Yes", "No"])
    education = st.selectbox("Niveau d'études", ["Graduate", "Not Graduate"])
with col2:
    dependents    = st.selectbox("Personnes à charge", ["0", "1", "2", "3+"])
    self_employed = st.selectbox("Travailleur indépendant", ["No", "Yes"])
    property_area = st.selectbox("Zone d'habitation", ["Urban", "Semiurban", "Rural"])

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<p class="section-label">Informations financières</p>', unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    applicant_income   = st.number_input("Revenu du demandeur (€)", min_value=0, value=3000, step=500)
    coapplicant_income = st.number_input("Revenu du co-demandeur (€)", min_value=0, value=0, step=500)
with col4:
    loan_amount = st.number_input("Montant du prêt (€)", min_value=0, value=120000, step=5000)
    loan_term   = st.selectbox("Durée du prêt (mois)", [360, 180, 120, 84, 60, 36, 12])

credit_history = st.selectbox(
    "Historique de crédit",
    [1.0, 0.0],
    format_func=lambda x: "✅ Bon historique" if x == 1.0 else "❌ Mauvais historique"
)

st.markdown('</div>', unsafe_allow_html=True)


# ─── PRÉDICTION ────────────────────────────────────────────────────────────────
if st.button("Analyser ma demande →"):

    if not model_loaded:
        st.error("⚠️ Modèle non trouvé. Assure-toi que model.pkl et scaler.pkl sont dans le même dossier.")
    else:
        # Encodage identique à l'entraînement
        gender_enc        = 1 if gender == "Male" else 0
        married_enc       = 1 if married == "Yes" else 0
        dependents_enc    = 3 if dependents == "3+" else int(dependents)
        education_enc     = 0 if education == "Graduate" else 1
        self_employed_enc = 1 if self_employed == "Yes" else 0
        property_enc      = {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]
        total_income      = applicant_income + coapplicant_income

        input_data = pd.DataFrame([{
            "Gender"          : gender_enc,
            "Married"         : married_enc,
            "Dependents"      : dependents_enc,
            "Education"       : education_enc,
            "Self_Employed"   : self_employed_enc,
            "LoanAmount"      : loan_amount,
            "Loan_Amount_Term": loan_term,
            "Credit_History"  : credit_history,
            "Property_Area"   : property_enc,
            "Total_Income"    : total_income
        }])

        input_scaled = scaler.transform(input_data)
        proba        = model.predict_proba(input_scaled)[0][1]
        decision     = "Accordé" if proba >= 0.3 else "Refusé"

        st.markdown("---")

        if decision == "Accordé":
            st.markdown(f"""
            <div class="result-accordé">
                <div class="result-icon">✅</div>
                <h2>Prêt Accordé</h2>
                <p style="color:#d1fae5; font-size:1.05rem;">
                    La demande présente un profil favorable.
                </p>
                <p class="result-prob">Probabilité d'accord : <strong>{proba*100:.1f}%</strong></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-refusé">
                <div class="result-icon">❌</div>
                <h2>Prêt Refusé</h2>
                <p style="color:#fee2e2; font-size:1.05rem;">
                    Le profil présente un risque trop élevé.
                </p>
                <p class="result-prob">Probabilité d'accord : <strong>{proba*100:.1f}%</strong></p>
            </div>
            """, unsafe_allow_html=True)

