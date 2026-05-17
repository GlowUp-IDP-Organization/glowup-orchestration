import requests
import streamlit as st

# Configurare pagină tematică GlowUp (Roz/Premium)
st.set_page_config(page_title="GlowUp - Skincare Assistant", page_icon="✨", layout="centered")

st.title("✨ GlowUp - Cloud-Native Skincare Assistant ✨")
st.markdown("---")

# Mape de produse pentru a fi mai ușor de selectat în UI
PRODUCT_MAP = {
    1: "💧 Glow Serum (Vit. C) - ID 1",
    2: "🌙 Night Renewal (Retinol) - ID 2",
    3: "🧪 Exfoliant Lichid (AHA/BHA) - ID 3",
    4: "🧴 Daily Moisture (Ceramide) - ID 4",
    5: "☀️ Sun Shield (SPF) - ID 5"
}

# URL-ul către Kong API Gateway
BASE_URL = "http://localhost:8000"

# Gestiune sesiune utilizator (stocăm username-ul global ca să nu-l reintroducem)
if "username" not in st.session_state:
    st.session_state["username"] = "anca_anda"

# Crearea tab-urilor pentru fiecare funcționalitate din cerințe
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔐 Autentificare", 
    "➕ Adaugă pe Raft", 
    "📦 The Shelf (Inventar & PAO)", 
    "🧠 Generator Rutină", 
    "⚠️ Verificator Incompatibilități"
])

# --- TAB 1: MANAGEMENT PROFIL ȘI AUTENTIFICARE ---
with tab1:
    st.header("👤 Profil Utilizator nou")
    with st.form("register_form"):
        username = st.text_input("Username", value=st.session_state["username"])
        password = st.text_input("Parolă", type="password", value="nota10")
        skin_type = st.selectbox("Tip de ten", ["mixt", "gras", "uscat"])
        sensitivities = st.text_input("Sensibilități / Alergii", value="retinol")
        
        submit_auth = st.form_submit_button("Înregistrează Profil")
        
        if submit_auth:
            payload = {
                "username": username,
                "password": password,
                "skin_type": skin_type,
                "sensitivities": sensitivities
            }
            try:
                res = requests.post(f"{BASE_URL}/auth/register", json=payload)
                if res.status_code == 200:
                    st.session_state["username"] = username
                    st.success(f"🎉 {res.json()['message']} Token-ul JWT a fost generat cu succes pentru utilizatorul: **{username}** (Ten {skin_type}).")
                else:
                    st.error("Eroare la autentificare.")
            except Exception as e:
                st.error(f"Nu s-a putut contacta API Gateway: {e}")

# --- TAB 2: GESTIUNEA INVENTARULUI (ADĂUGARE) ---
with tab2:
    st.header("📥 Pune un produs pe raftul tău virtual")
    st.info(f"Utilizator curent: **{st.session_state['username']}**")
    
    prod_label = st.selectbox("Selectează produsul achiziționat", list(PRODUCT_MAP.values()))
    selected_id = [k for k, v in PRODUCT_MAP.items() if v == prod_label][0]
    
    pao = st.slider("Termen de valabilitate de la deschidere (PAO - Luni)", min_value=3, max_value=24, value=6, step=3)
    
    if st.button("Adaugă în Inventar"):
        payload = {
            "username": st.session_state["username"],
            "product_id": selected_id,
            "pao_months": pao
        }
        try:
            res = requests.post(f"{BASE_URL}/io/shelf", json=payload)
            if res.status_code == 200:
                st.success(f"✅ {res.json()['message']} Produsul a fost plasat securizat în baza de date PostgreSQL.")
            else:
                st.error("Eroare din IO MS: Produsul nu a putut fi adăugat.")
        except Exception as e:
            st.error(f"Eroare conexiune: {e}")

# --- TAB 3: THE SHELF (VIZUALIZARE & ALERTE EXPIRARE) ---
with tab3:
    st.header("🗄️ Raftul Tău - Monitorizare PAO și Expirare")
    st.write(f"Inventarul curent pentru: **{st.session_state['username']}**")
    
    if st.button("Actualizează și Încarcă Raftul"):
        try:
            res = requests.get(f"{BASE_URL}/io/shelf/{st.session_state['username']}")
            if res.status_code == 200:
                items = res.json().get("shelf_items", [])
                if not items:
                    st.warning("Raftul tău este gol momentan. Adaugă produse din Tab-ul anterior.")
                else:
                    for item in items:
                        # Curățăm formatul datei pentru un aspect vizual premium
                        exp_date = item['expiry_date'].split("T")[0]
                        st.metric(
                            label=f"🧴 {item['name']} ({item['category'].capitalize()})", 
                            value=f"Expiră la: {exp_date}", 
                            delta=f"PAO: {item['pao_months']} luni"
                        )
            else:
                st.error("Nu s-au putut extrage datele din IO MS.")
        except Exception as e:
            st.error(f"Eroare conexiune: {e}")

# --- TAB 4: GENERATOR DE RUTINĂ INTELIGENT ---
with tab4:
    st.header("🧠 Generator Automate de Rutină (Sortare după Consistență)")
    st.write("Algoritmul analizează produsele de pe raftul tău și le așează în ordinea corectă a pH-ului și densității.")
    
    if st.button("Generează Rutina Optimă"):
        try:
            res = requests.get(f"{BASE_URL}/logic/generate-routine/{st.session_state['username']}")
            if res.status_code == 200:
                data = res.json()
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("☀️ Rutina de Dimineață (AM)")
                    if data["am_routine"]:
                        for idx, p in enumerate(data["am_routine"], 1):
                            st.write(f"**Pasul {idx}:** {p}")
                    else:
                        st.caption("Fără produse dedicate dimineții pe raft.")
                        
                with col2:
                    st.subheader("🌙 Rutina de Seară (PM)")
                    if data["pm_routine"]:
                        for idx, p in enumerate(data["pm_routine"], 1):
                            st.write(f"**Pasul {idx}:** {p}")
                    else:
                        st.caption("Fără produse dedicate serii pe raft.")
                
                st.caption(f"💡 *Regulă de business aplicată:* {data['sorting_rule']}")
            else:
                st.error("Eroare la procesarea rutinei de către Logic MS.")
        except Exception as e:
            st.error(f"Eroare conexiune: {e}")

# --- TAB 5: VERIFICATOR DE INCOMPATIBILITĂȚI ---
with tab5:
    st.header("⚠️ Scaner Medical de Incompatibilități Active")
    st.write("Selectează manual produsele pe care vrei să le aplici simultan pentru a rula testul de siguranță:")
    
    selected_labels = st.multiselect("Alege produsele din sesiune:", list(PRODUCT_MAP.values()))
    
    if st.button("Rulează Analiza de Siguranță"):
        if not selected_labels:
            st.warning("Selectează cel puțin un produs!")
        else:
            # Mapăm etichetele înapoi la ID-uri simple pentru backend
            ids = [[k for k, v in PRODUCT_MAP.items() if v == label][0] for label in selected_labels]
            try:
                res = requests.post(f"{BASE_URL}/logic/analyze-routine", json={"product_ids": ids})
                if res.status_code == 200:
                    data = res.json()
                    if data["safe"]:
                        st.success(f"✅ {data['message']}")
                    else:
                        st.error(f"🚫 {data['warning']}")
                else:
                    st.error("Eroare la Logic MS.")
            except Exception as e:
                st.error(f"Eroare conexiune: {e}")