import streamlit as st
from streamlit_lottie import st_lottie
import requests

#

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

#
def loadanim():
    url = "https://lottie.host/1a04f98a-6794-4f0c-8693-44a3264c3923/hngSQ1VP2s.json"
    anim = requests.get(url)
    if anim.status_code != 200:
        return None
    return anim.json()
animjson = loadanim()

def about_page():
    st.title("About Us")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(
            """
            Welcome to our Streamlit app! This is the *About Us* page.
            
            We are a team of developers passionate about creating amazing applications. 
            This app is designed to showcase our skills and the power of Streamlit.
            
            *Features:*
            - Real-time data visualization
            - User-friendly interface
            - Interactive charts and graphs
            
            Feel free to explore the different pages of our app and discover the capabilities 
            of Streamlit!
            
            If you have any questions or feedback, please don't hesitate to [contact us](mailto:your-email@example.com).
            """
        )
    with right_column:
        st_lottie(animjson)


# Example usage
if __name__ == "__main__":
    about_page()