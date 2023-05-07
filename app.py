from pathlib import Path

import streamlit as st
from PIL import Image

# --- Path settings ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- General settings ---

PAGE_TITLE = "CV digitale | Emiliano Ascenzi"
PAGE_ICON = ":wave:"
NAME = "Emiliano Ascenzi"
DESCRIPTION = """
Business Analyst, supporto la mia azienda nel prendere decisioni basate sui dati
"""
EMAIL = "emilianoascenzi00@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/emiliano-ascenzi-3ab7b815a/",
    "GitHub": "https://github.com/EmilianoAscenzi"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Curriculum Vitae Digitale")

# --- Load CSS, PDF & Profile pic ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

# --- Hero section ---

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📝 Scarica il CV in formato PDF",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)

# --- Social links ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Skills ---
st.write("#")
st.subheader("Skills")
st.write(
    """
- 🗄️ Esperienza nel raccogliere, pulire, trasformare, analizzare e rappresentare dati
- 👨‍💻 Linguaggi di programmazione: Python, R, SQL e MATLAB
- 📈 Strumenti di visualizzazione dati: Power BI, Tableau e MS Excel
    """
)

# --- Work history ---

st.write("#")
st.subheader("Esperienza lavorativa")
st.write("---")

# Job 1

st.write("🧑‍💼","**Business Analyst  |  Amplia Infrastructures S.p.A.**")
st.write("Marzo 2023 - presente")
st.write(
    """
- Monitoraggio dell’avanzamento dei progetti tramite la redazione e l’aggiornamento di cronoprogrammi e dashboard in Power BI
- Individuazione di KPI sulla baseline digitale dell’azienda
- Identificazione e miglioramento dei processi in uso nel contesto aziendale
    """
)

# Job 2

st.write("🧑‍💼","**Associate  |  Intellera consulting S.p.A.**")
st.write("Maggio 2022 - Febbraio 2023 ")
st.write(
    """
- Analisi della baseline digitale di Pubbliche Amministrazioni clienti
- Progettazione di soluzioni digitali che incontrino i fabbisogni del cliente
- Analisi su open data PNRR al fine di individuare un numero ristretto di progettualità di interesse per il cliente

    """
)

# Job 3

st.write("🧑‍💼","**Infrastructure Planning Engineer – FTTH Network  |  Accenture S.p.A.**")
st.write("Agosto 2020 - Maggio 2022")
st.write(
    """
- Progettazione ottico e civile di reti in fibra FTTH per oltre 60 comuni
- Formazione rivolta a 7 membri del team di progettazione finalizzata all'accrescimento dell'autonomia ed efficienza in ambito operativo
- Supporto al regional lead nella risoluzione di conflitti fra il team di progettazione e le squadre in campo con conseguente riduzione di lavoro sprecato del 70% nei primi 5 mesi

    """
)

# Job 4

st.write("🧑‍💼","**Digital Solutions Internship  |  Bridgestone NVSA**")
st.write("Gennaio 2020 - Giugno 2020")
st.write(
    """
- Implementazione di un modello fisico che riproduca il comportamento delle sospensioni di un veicolo target
- Analisi dati di telemetria tramite l’utilizzo di SQL (extraction), MATLAB e Python (transformation) risultanti una correlazione fra le vibrazioni registrate all’interno dell’abitacolo e la rugosità longitudinale delle pavimentazioni autostradali

    """
)

