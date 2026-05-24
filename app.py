import streamlit as st

# Global safety patch for custom spacing method to prevent AttributeErrors
st.space = lambda: st.markdown("<div style='margin: 12px 0;'></div>", unsafe_allow_html=True)

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

from src.components.header import LOGO_URL

def main():
    st.set_page_config(
        page_title="Smart Class — AI Attendance",
        page_icon=LOGO_URL,
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()


    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state['login_type'] != 'student':
            st.session_state['login_type'] = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
main()