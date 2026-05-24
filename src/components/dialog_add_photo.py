import streamlit as st
from PIL import Image


@st.dialog("Capture or upload photos")
def add_photos_dialog():

    st.write('Add classroom photos to scan for attendance')

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'tertiary'
        if st.button('Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'



    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'tertiary'
        if st.button('Upload photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Take Snapshot', key='dialog_cam')
        if cam_photo:
            if len(st.session_state.attendance_images) >= 10:
                st.error("⚠️ Maximum of 10 photos reached. Please clear some before adding more.")
            else:
                try:
                    img = Image.open(cam_photo)
                    st.session_state.attendance_images.append(img)
                    st.toast('Photo Captured')
                    st.rerun()
                except Exception:
                    st.error("Failed to read the captured photo.")


    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader('Choose image files', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key='dialog_upload')

        if uploaded_files:
            added = 0
            for f in uploaded_files:
                if len(st.session_state.attendance_images) >= 10:
                    st.warning("⚠️ Reached maximum limit of 10 photos. Some files were skipped.")
                    break
                try:
                    img = Image.open(f)
                    st.session_state.attendance_images.append(img)
                    added += 1
                except Exception:
                    st.error(f"Failed to read file: {f.name}")
            
            if added > 0:
                st.toast(f'{added} Photo(s) Uploaded Successfully')
                st.rerun()

    st.divider()
    if st.button('Done', type='primary', width='stretch'):
        st.rerun()