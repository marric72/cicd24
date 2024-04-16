"""
    Easy Azure Streamlit Demo
    Author: Wolf Paulus (wolf@paulus.com)
    some modifications by Heather M

    snowflake like effect from YouTube: https://youtu.be/8SLiFCnFOEo?si=kZh25qA7n4tr-Nh2

from random import randint
import streamlit as st
from log import logger

# Page Settings
favicon = "🏆"
st.set_page_config(page_title="Congrats on end of Semester", page_icon=favicon)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def ui(items: [int]) -> None: # type: ignore

    st.title("Heather's Streamlit Demo v0.4")
    st.subheader(".. on Azure")
   
    local_css("./style/style.css")
    st.markdown(
        "<h2 style='text-align: center;'>Enjoy your summer break.</h2>", unsafe_allow_html=True
    )
    st.write("")

    # Load Animation
    animation_symbol = "🌸"

   

    st.line_chart(items)
    



if __name__ == "__main__":
    data = [randint(0, 10) for _ in range(25)]
    logger.info(f"Created a list with {len(data)} items.")
    ui(data)
"""


from random import randint
import streamlit as st
from log import logger


def ui(items: [int]) -> None:

    st.title("Streamlit Demo v0.4")
    st.subheader(".. on Azure")
    st.line_chart(items)


if __name__ == "__main__":
    data = [randint(0, 10) for _ in range(25)]
    logger.info(f"Created a list with {len(data)} items.")
    ui(data)
    