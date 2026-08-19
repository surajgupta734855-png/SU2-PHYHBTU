import streamlit as st
import math

# ============================================================
# HBTU NPH-605
# SI <-> CGS MAGNETIC UNIT CONVERTER
# ============================================================

APP_NAME = "SG_PHYHBTU"  # Change SG to first two letters of your name

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🧲",
    layout="centered"
)

# ------------------------------------------------------------
# CSS
# ------------------------------------------------------------

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    border: 2px solid #4CAF50;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}

.info-box {
    padding: 15px;
    border-radius: 10px;
    background-color: rgba(100,100,100,0.10);
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------

st.markdown(
    '<div class="main-title">🧲 Magnetic Unit Converter</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">SI ↔ CGS Conversion | HBTU NPH-605</div>',
    unsafe_allow_html=True
)

st.write("")

# ------------------------------------------------------------
# CONVERSION DATA
# factor means:
# CGS = SI × factor
# ------------------------------------------------------------

quantities = {

    "1. Magnetic Induction (B)": {
        "symbol": "B",
        "si": "tesla (T)",
        "cgs": "gauss (G)",
        "factor": 1e4,
        "formula": "1 T = 10⁴ G"
    },

    "2. Magnetic Field Strength (H)": {
        "symbol": "H",
        "si": "A/m",
        "cgs": "oersted (Oe)",
        "factor": 4 * math.pi * 1e-3,
        "formula": "1 A/m = 4π × 10⁻³ Oe"
    },

    "3. Magnetization (M)": {
        "symbol": "M",
        "si": "A/m",
        "cgs": "emu/cm³",
        "factor": 1e-3,
        "formula": "1 A/m = 10⁻³ emu/cm³"
    },

    "4. Magnetic Polarization (J)": {
        "symbol": "J",
        "si": "tesla (T)",
        "cgs": "gauss (G)",
        "factor": 1e4,
        "formula": "1 T = 10⁴ G"
    },

    "5. Magnetic Moment (m)": {
        "symbol": "m",
        "si": "A m²",
        "cgs": "emu = G cm³",
        "factor": 1e3,
        "formula": "1 A m² = 10³ emu"
    },

    "6. Magnetic Moment per Unit Mass (σ)": {
        "symbol": "σ",
        "si": "A m²/kg",
        "cgs": "emu/g",
        "factor": 1,
        "formula": "1 A m²/kg = 1 emu/g"
    },

    "7. Volume Magnetic Susceptibility (χ)": {
        "symbol": "χ",
        "si": "dimensionless",
        "cgs": "dimensionless",
        "factor": 1 / (4 * math.pi),
        "formula": "1 SI = 1/(4π) CGS"
    },

    "8. Mass Magnetic Susceptibility (χmass)": {
        "symbol": "χmass",
        "si": "m³/kg",
        "cgs": "emu/g",
        "factor": 1e3 / (4 * math.pi),
        "formula": "1 m³/kg = 10³/(4π) emu/g"
    },

    "9. Molar Magnetic Susceptibility (χm)": {
        "symbol": "χm",
        "si": "m³/mol",
        "cgs": "emu/mol",
        "factor": 1e6 / (4 * math.pi),
        "formula": "1 m³/mol = 10⁶/(4π) emu/mol"
    },

    "10. Magnetic Permeability (μ)": {
        "symbol": "μ",
        "si": "H/m",
        "cgs": "G/Oe",
        "factor": 1e7 / (4 * math.pi),
        "formula": "1 H/m = 10⁷/(4π) G/Oe"
    },

    "11. Magnetic Flux (Φ)": {
        "symbol": "Φ",
        "si": "weber (Wb)",
        "cgs": "maxwell (Mx)",
        "factor": 1e8,
        "formula": "1 Wb = 10⁸ Mx"
    },

    "12. Magnetic Scalar Potential / MMF": {
        "symbol": "φ, F",
        "si": "ampere (A)",
        "cgs": "gilbert (Gb)",
        "factor": 4 * math.pi / 10,
        "formula": "1 A = 4π/10 gilbert"
    },

    "13. Magnetic Vector Potential (A)": {
        "symbol": "A",
        "si": "Wb/m",
        "cgs": "emu/cm = G cm",
        "factor": 1e6,
        "formula": "1 Wb/m = 10⁶ emu/cm"
    },

    "14. Magnetic Pole Strength (p)": {
        "symbol": "p",
        "si": "A m",
        "cgs": "emu = G cm²",
        "factor": 10,
        "formula": "1 A m = 10 emu"
    },

    "15. Demagnetizing Factor (N)": {
        "symbol": "N",
        "si": "dimensionless",
        "cgs": "dimensionless",
        "factor": 4 * math.pi,
        "formula": "1 SI = 4π CGS"
    },

    "16. Magnetostriction Constant (λ)": {
        "symbol": "λ",
        "si": "dimensionless",
        "cgs": "dimensionless",
        "factor": 1,
        "formula": "1 SI = 1 CGS"
    },

    "17. Anisotropy Constant (K, K₁, Ku)": {
        "symbol": "K",
        "si": "J/m³",
        "cgs": "erg/cm³",
        "factor": 10,
        "formula": "1 J/m³ = 10 erg/cm³"
    },

    "18. Magnetostatic Energy (Em)": {
        "symbol": "Em",
        "si": "J/m³",
        "cgs": "erg/cm³",
        "factor": 10,
        "formula": "1 J/m³ = 10 erg/cm³"
    },

    "19. Energy Product ((BH)max)": {
        "symbol": "(BH)max",
        "si": "J/m³",
        "cgs": "erg/cm³",
        "factor": 10,
        "formula": "1 J/m³ = 10 erg/cm³"
    }
}

# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

st.sidebar.title("🧲 Converter Menu")

selected_quantity = st.sidebar.selectbox(
    "Select Physical Quantity",
    list(quantities.keys())
)

st.sidebar.markdown("---")

st.sidebar.info(
    "HBTU\n"
    "M.Sc. Physics\n"
    "NPH-605\n"
    "Spintronics: Fundamentals and Applications"
)

# ------------------------------------------------------------
# SELECTED DATA
# ------------------------------------------------------------

data = quantities[selected_quantity]

st.subheader(selected_quantity)

col1, col2 = st.columns(2)

with col1:
    st.write("**SI Unit:**")
    st.info(data["si"])

with col2:
    st.write("**CGS Unit:**")
    st.info(data["cgs"])

# ------------------------------------------------------------
# CONVERSION DIRECTION
# ------------------------------------------------------------

direction = st.radio(
    "Select Conversion Direction",
    [
        "SI → CGS",
        "CGS → SI"
    ],
    horizontal=True
)

# ------------------------------------------------------------
# INPUT
# ------------------------------------------------------------

value = st.number_input(
    f"Enter value in {'SI' if direction == 'SI → CGS' else 'CGS'} unit",
    value=0.0,
    format="%.10g"
)

# ------------------------------------------------------------
# CONVERT BUTTON
# ------------------------------------------------------------

if st.button("🔄 Convert", use_container_width=True):

    if direction == "SI → CGS":
        result = value * data["factor"]
        result_unit = data["cgs"]
        input_unit = data["si"]

    else:
        if data["factor"] == 0:
            st.error("Conversion factor cannot be zero.")
            st.stop()

        result = value / data["factor"]
        result_unit = data["si"]
        input_unit = data["cgs"]

    st.markdown("---")

    st.write(f"**Input:** {value:g} {input_unit}")

    st.markdown(
        f'<div class="result-box">'
        f'{result:.8g} {result_unit}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.success("Conversion completed successfully.")

# ------------------------------------------------------------
# FORMULA
# ------------------------------------------------------------

st.markdown("---")

st.subheader("📐 Conversion Formula")

st.info(data["formula"])

if direction == "SI → CGS":
    st.write(
        f"CGS Value = SI Value × {data['factor']:.8g}"
    )
else:
    st.write(
        f"SI Value = CGS Value ÷ {data['factor']:.8g}"
    )

# ------------------------------------------------------------
# QUICK REFERENCE
# ------------------------------------------------------------

st.markdown("---")

with st.expander("📚 Quick Reference Table - All 19 Quantities"):

    for name, item in quantities.items():

        st.markdown(
            f"""
**{name}**

- Symbol: `{item['symbol']}`
- SI Unit: `{item['si']}`
- CGS Unit: `{item['cgs']}`
- Conversion: `{item['formula']}`

---
"""
        )

# ------------------------------------------------------------
# ABOUT
# ------------------------------------------------------------

st.markdown("---")

with st.expander("ℹ️ About Assignment"):

    st.write("""
    This application is developed for:

    Harcourt Butler Technical University (HBTU)
    
    Department of Physics
    
    M.Sc. Physics – II Year
    
    Course Code: NPH-605
    
    Course: Spintronics: Fundamentals and Applications
    
    Assignment-I
    
    Purpose:
    SI to CGS and CGS to SI conversion of magnetic quantities.
    """)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

st.markdown("---")

st.caption(
    f"{APP_NAME} | HBTU | NPH-605 | Magnetic Unit Converter"
)
