import streamlit as st
import base64
from pathlib import Path

from src.ui.theme import hairline_div

def get_base64_logo():
    logo_path = Path("icons/edited-photo.png")
    if logo_path.exists():
        with open(logo_path, "rb") as f:
            data = f.read()
            return f"data:image/png;base64,{base64.b64encode(data).decode()}"
    return "https://i.ibb.co/YTYGn5qV/logo.png"

LOGO_URL = get_base64_logo()
_WRAP = "div"


def header_home():
    st.markdown(
        f"""
        <{_WRAP} class="smartclass-brand" style="display:flex;flex-direction:column;
            align-items:center;text-align:center;margin:var(--space-xl) 0 var(--space-lg);">
            <img src="{LOGO_URL}" alt="" style="height:120px;opacity:0.95;border-radius:25%;object-fit:cover;" />
            <p class="smart-wordmark" style="margin-top:var(--space-lg);">SMART CLASS</p>
            <h1 class="smart-display-xl">Making Attendance<br/>Effortless</h1>
            <p class="smart-caption">AI · Face · Voice</p>
            {hairline_div(margin="var(--space-lg) auto 0")}
        </{_WRAP}>
        """,
        unsafe_allow_html=True,
    )


def header_dashboard():
    w = _WRAP
    st.markdown(
        f"""
        <{w} class="smartclass-brand" style="display:flex;align-items:center;
            gap:var(--space-md);margin-bottom:var(--space-md);">
            <img src="{LOGO_URL}" alt="" style="height:56px;opacity:0.95;border-radius:25%;object-fit:cover;" />
            <{w}>
                <p class="smart-wordmark">SMART CLASS</p>
                <p class="smart-caption" style="margin-top:var(--space-xxs);">Attendance System</p>
            </{w}>
        </{w}>
        {hairline_div(margin="0 0 var(--space-md)")}
        """,
        unsafe_allow_html=True,
    )
