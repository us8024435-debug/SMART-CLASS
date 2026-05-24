import streamlit as st
import html


def subject_card(name, code, section, stats=None, footer_callback=None):
    safe_name = html.escape(name)
    safe_code = html.escape(code)
    safe_section = html.escape(section) if section else ""

    html_content = f"""
    <div class="smart-subject-card">
        <h3>{safe_name}</h3>
        <p class="meta">
            Code: <span class="code-badge">{safe_code}</span>
            &nbsp;|&nbsp; Section: {safe_section}
        </p>
    """

    if stats:
        html_content += '<div class="smart-stat-row">'
        for icon, label, value in stats:
            html_content += (
                f'<span class="smart-stat-pill">{icon} '
                f"<b>{value}</b> {label}</span>"
            )
        html_content += "</div>"

    html_content += "</div>"

    st.markdown(html_content, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
