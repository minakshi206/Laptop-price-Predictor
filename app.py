import streamlit as st
import pickle
import pandas as pd

st.markdown("""
<style>
/* Remove default Streamlit padding */
.block-container {
    padding-top: 0rem !important;
}

/* Hide Streamlit header space */
header {
    visibility: hidden;
    height: 0px;
}

/* Optional: remove footer */
footer {
    visibility: hidden;
    height: 0px;
}
</style>
""", unsafe_allow_html=True)


# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Laptop Price Predictor",
    layout="centered",
    page_icon="💻"
)

# ================== LOAD MODEL ==================
model = pickle.load(open("laptop_price_model.pkl", "rb"))

# ================== CUSTOM CSS ==================
st.markdown("""
<style>
/* App background */
.stApp {
    background-color: #f4f6f9;
}

/* Text color */
h1, h2, h3, label, p {
    color: Black !important;
}

/* Selectbox & sliders */
div[data-baseweb="select"] > div {
    background-color: #1f2937;
    color: white;
}

/* Button */
div.stButton > button {
    background-color: #ff4b4b;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 25px;
    border: none;
}

/* Success box */
div[data-testid="stSuccess"] {
    background-color: #1f2937;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ================== MAIN CARD ==================
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.title("💻 Laptop Price Predictor")
st.write("Predict laptop price based on configuration")

# ================== ROW 1 ==================
col1, col2, col3 = st.columns(3)

with col1:
    company = st.selectbox("Brand", ["Dell", "HP", "Lenovo", "Asus", "Acer"])
    type_name = st.selectbox("Laptop Type", ["Ultrabook", "Notebook", "Gaming"])
    os = st.selectbox("Operating System", ["Windows", "Mac", "Linux"])

with col2:
    cpu_company = st.selectbox("CPU Company", ["Intel", "AMD"])
    cpu_model = st.selectbox("CPU Model", ["Core i3", "Core i5", "Core i7", "Ryzen 5", "Ryzen 7"])
    cpu_freq = st.slider("CPU Frequency (GHz)", 1.0, 4.5, 2.5)

with col3:
    ram = st.slider("RAM (GB)", 4, 64, 8)
    weight = st.slider("Weight (kg)", 1.0, 4.0, 1.5)
    inches = st.slider("Screen Size (Inches)", 10.0, 18.0, 13.3)

# ================== ROW 2 ==================
col4, col5, col6 = st.columns(3)

with col4:
    gpu_company = st.selectbox("GPU Company", ["Intel", "Nvidia", "AMD"])
    gpu_model = st.selectbox("GPU Model", ["HD Graphics", "UHD Graphics", "GTX", "RTX"])

with col5:
    primary_storage_type = st.selectbox("Primary Storage Type", ["SSD", "HDD"])
    primary_storage = st.slider("Primary Storage (GB)", 128, 2048, 256)

with col6:
    secondary_storage_type = st.selectbox("Secondary Storage Type", ["None", "SSD", "HDD"])
    secondary_storage = st.slider("Secondary Storage (GB)", 0, 2048, 0)

col10, col11 = st.columns(2)

with col10:
    screen_w = st.selectbox("Screen Width", [1366, 1600, 1920, 2560])

with col11:
    screen_h = st.selectbox("Screen Height", [768, 900, 1080, 1440])


# ================== ROW 3 ==================
col7, col8, col9 = st.columns(3)

with col7:
    touchscreen = st.checkbox("Touchscreen")

with col8:
    ips = st.checkbox("IPS Panel")

with col9:
    retina = st.checkbox("Retina Display")

st.markdown("<br>", unsafe_allow_html=True)



# ================== PREDICTION ==================
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        'Company': company,
        'TypeName': type_name,
        'OS': os,
        'CPU_company': cpu_company,
        'CPU_model': cpu_model,
        'GPU_company': gpu_company,
        'GPU_model': gpu_model,
        'PrimaryStorageType': primary_storage_type,
        'SecondaryStorageType': secondary_storage_type,
        'Inches': inches,
        'Ram': ram,
        'Weight': weight,
	'ScreenW': screen_w,          
    	'ScreenH': screen_h,
        'Touchscreen': int(touchscreen),
        'IPSpanel': int(ips),
        'RetinaDisplay': int(retina),
        'CPU_freq': cpu_freq,
        'PrimaryStorage': primary_storage,
        'SecondaryStorage': secondary_storage
    }])

    prediction_euro = model.predict(input_df)[0]	

# Convert Euro to INR (approx)
    prediction_inr = int(prediction_euro * 90)

    st.success(f"💰 Estimated Laptop Price: ₹ {prediction_inr:,}")


st.markdown('</div>', unsafe_allow_html=True)
