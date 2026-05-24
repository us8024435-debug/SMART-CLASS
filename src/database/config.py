import os
import streamlit as st
from supabase import create_client, Client

URL = os.environ.get("SUPABASE_URL") or st.secrets.get("SUPABASE_URL")
KEY = os.environ.get("SUPABASE_KEY") or st.secrets.get("SUPABASE_KEY")

if not URL or not KEY:
    st.error("⚠️ Supabase configuration missing! Please set SUPABASE_URL and SUPABASE_KEY in your Environment Variables or .streamlit/secrets.toml.")
    st.stop()

supabase: Client = create_client(URL, KEY)