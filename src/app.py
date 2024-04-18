"""
    Easy Azure Streamlit Demo
    Author: Wolf Paulus (wolf@paulus.com)
    some modifications by Heather M

    snowflake like effect from YouTube: https://youtu.be/8SLiFCnFOEo?si=kZh25qA7n4tr-Nh2

    Run this on local machine  with: python3 -m streamlit run src/app.py 
"""
from random import randint
import streamlit as st
from log import logger

# Page Setting
favicon = "🏆"
st.set_page_config(page_title="Congrats on end of Semester", page_icon=favicon)

# Use local CSS


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def ui(items: [int]) -> None:
    st.title("Heather's Streamlit Demo v0.4")
    st.subheader(".. on Azure")

    local_css("./style/style.css")
    st.markdown(
        "<h2 style='text-align: center;'>Enjoy your summer break.</h2>",
        unsafe_allow_html=True
    )
    st.write("")

    # Load Animation
    animation_symbol = "🌸"

    st.markdown(
        f"""
        <div class="snowflake">{animation_symbol}</div>
        <div class="snowflake">{animation_symbol}</div>
        <div class="snowflake">{animation_symbol}</div>
        <div class="snowflake">{animation_symbol}</div>
        <div class="snowflake">{animation_symbol}</div>
        <div class="snowflake">{animation_symbol}</div>
        <div class="snowflake">{animation_symbol}</div>
        <div class="snowflake">{animation_symbol}</div>
        <div class="snowflake">{animation_symbol}</div>
        """,
        unsafe_allow_html=True
    )

    st.line_chart(items)


if __name__ == "__main__":
    data = [randint(0, 10) for _ in range(25)]
    logger.info(f"Created a list with {len(data)} items.")
    ui(data)
