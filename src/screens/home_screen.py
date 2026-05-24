import streamlit as st

from src.components.header import header_home
from src.ui.base_layout import apply_page_styles


def home_screen():
    apply_page_styles(home_portal=True)

    header_home()

    st.markdown(
        '<p class="smart-caption" style="text-align:center;margin-bottom:var(--space-xl);">'
        "Choose your portal</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("Student")
        st.image("icons/edited-photo (4).png", width=140)
        st.markdown(
            '<p style="font-family:var(--font-body);color:var(--color-body);'
            'margin-bottom:var(--space-lg);">Sign in with Face ID and manage your classes.</p>',
            unsafe_allow_html=True,
        )
        if st.button(
            "Student Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
            use_container_width=True,
        ):
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:
        st.header("Teacher")
        st.image("icons/edited-photo (3).png", width=145)
        st.markdown(
            '<p style="font-family:var(--font-body);color:var(--color-body);'
            'margin-bottom:var(--space-lg);">Take AI attendance and manage subjects.</p>',
            unsafe_allow_html=True,
        )
        if st.button(
            "Teacher Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
            use_container_width=True,
        ):
            st.session_state["login_type"] = "teacher"
            st.rerun()
