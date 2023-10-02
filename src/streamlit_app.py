import streamlit as st
import streamlit_analytics
import display
import validator_helper


page_title = '[Fill in your title]'
firestore_collection_name = 'test'

validator_helper.parse_firestore_toml_to_json()
st.set_page_config(page_title)


with streamlit_analytics.track(
        unsafe_password=st.secrets.tracking.pw,
        firestore_key_file=".streamlit/fs_key.json",
        firestore_collection_name=firestore_collection_name,
):
    try:
        display.write_welcome()
        st.sidebar.write("## Settings :gear:")

        # <------
        #
        #
        # YOUR APP
        #
        #
        # ------->

        display.render_follow_me()
        st.divider()
        display.render_subscribe_button()
        display.render_more_apps()
    except Exception as e:
        raise
