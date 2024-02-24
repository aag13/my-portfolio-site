import streamlit as st


def set_session_var(var_name, var_val, dont_overwrite=False):
    if dont_overwrite and var_name in st.session_state:
        return

    st.session_state[var_name] = var_val


def get_session_var(var_name):
    if var_name in st.session_state:
        return st.session_state[var_name]

    return None


def remove_session_var(var_name):
    if var_name in st.session_state:
        del st.session_state[var_name]


def initialize_page_config(page_title=None, page_icon=None, global_css=None, bg_image=None):
    if page_title is None:
        page_title = "Home"
    if page_icon is None:
        page_icon = "👋"
    if global_css is None:
        global_css = "assets/styles.css"

    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout="wide",
    )
    load_asset(global_css)
    load_background_image(bg_image)


def load_asset(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_background_image(image_url=None):
    should_load_img = st.secrets["params"]["load_bg"]
    if should_load_img:
        background_image = image_url or st.secrets["params"]["bg_img_url"]
        # https://images.unsplash.com/photo-1551554781-c46200ea959d
        # https://images.unsplash.com/photo-1531685250784-7569952593d2
        # https://images.unsplash.com/photo-1568738351265-c7065f5d4293

        page_bg_img = f"""
        <style>
            .stApp {{
                background-image: url("{background_image}");
                background-size: cover;
            }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)


def set_page_header(page_header):
    st.markdown(f"<h1 class='page-header'>{page_header}</h1>", unsafe_allow_html=True)
