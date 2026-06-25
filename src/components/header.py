import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/k27XkLNW/logo.png"

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center;justify-content:center; margin-button:30px; margin-top:30px">        
            <img src='{logo_url}' style='height:100px;'/>
            <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
        </div>

                """, unsafe_allow_html=True)