import streamlit as st
import numpy as np
import joblib


model = joblib.load("house_model.pkl")


st.set_page_config(
    page_title="Home worth",
    layout="wide"
)


st.markdown("""
<style>
body {
    background: #020617;
}

/* Main Header */
.header {
    background: linear-gradient(90deg, #0ea5e9, #2563eb);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 15px;
}

/* Info Banner */
.info-banner {
    background: #020617;
    border: 1px solid #1e293b;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 25px;
    box-shadow: inset 0 0 15px rgba(14,165,233,0.2);
}

/* Card */
.card {
    background: #0f172a;
    padding: 30px;
    border-radius: 20px;
    margin-top: 20px;
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
}

/* Card Title */
.card-title {
    background: linear-gradient(90deg, #1d4ed8, #2563eb);
    padding: 14px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    color: white;
    margin-bottom: 25px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    color: white;
    font-size: 18px;
    padding: 10px 30px;
    border-radius: 12px;
    border: none;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #020617;
}

/* Sidebar Header */
.sidebar-header {
    background: linear-gradient(90deg, #0ea5e9, #2563eb);
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    color: white;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Advertisement Box */
.ad-box {
    background: linear-gradient(135deg, #020617, #0f172a);
    border: 1px solid #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-top: 25px;
    text-align: center;
    color: #e5e7eb;
}

.ad-box h4 {
    color: #38bdf8;
    margin-bottom: 10px;
}

.ad-box button {
    background: linear-gradient(90deg, #f59e0b, #f97316);
    color: black;
    border: none;
    padding: 8px 18px;
    border-radius: 10px;
    font-weight: bold;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<div class='header'>Home worth</div>", unsafe_allow_html=True)


st.sidebar.markdown("<div class='sidebar-header'>Go To</div>", unsafe_allow_html=True)
page = st.sidebar.radio("", ["Home", "Predict", "About"])


st.sidebar.markdown("""
<div class="ad-box">
    <h4> Sponsored</h4>
    <p>
    Learn <b>Data Science & AI</b><br>
    Build real-world ML projects
    </p>
    <button>Join Now</button>
</div>
""", unsafe_allow_html=True)


if page == "Home":

   
    st.markdown("<div class='info-banner'>", unsafe_allow_html=True)

    

    st.markdown(
        "This  is a **Machine Learning web application**  that predicts "
        "**Bangalore house prices** using **Linear Regression**."
    )

    st.markdown("""
    ###  Features Used
    - Total Square Feet  
    - Bathrooms  
    - Balconies  
    - Bedrooms (BHK)

     Use  **Predict**  to estimate the  house price.
    """)

    
    st.markdown("</div>", unsafe_allow_html=True)


elif page == "Predict":

    st.markdown("""
    <div class='card'>
        <div class='card-title'>Predict House Price</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        sqft = st.number_input("Total Square Feet", min_value=0.0)
        bath = st.number_input("Bathrooms", min_value=1.0, step=1.0)

    with col2:
        balcony = st.number_input("Balconies", min_value=0.0, step=1.0)
        bhk = st.number_input("Bedrooms (BHK)", min_value=1.0, step=1.0)

    if st.button("Predict Price"):
        features = np.array([[sqft, bath, balcony, bhk]])
        price = model.predict(features)
        st.success(f" Estimated Price: ₹ {round(price[0], 2)} Lakhs")

    st.markdown("</div>", unsafe_allow_html=True)


elif page == "About":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("About This Project")
    st.write("""
    **Tech Stack Used**
    - Python  
    - Streamlit  
    - Scikit-learn  
    - Linear Regression  

    **Dataset:** Bangalore House Price Dataset
    """)
    st.markdown("</div>", unsafe_allow_html=True)

