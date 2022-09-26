import difflib
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.set_page_config('Python Webscraper', ':mag:', layout='wide')
st.title(':mag:' + " " + 'Python WebScraper')

url = st.text_input('Please insert url:', key=1)
st.write('Website:', url)
with st.expander('Click to view:'):
    if url:
        res = requests.get(url)
        content = BeautifulSoup(res.content, 'html.parser')
        st.code(content)
    else:
        st.write('Loading...')

htmlElement = st.text_input('Please insert filter element:', key=2)

with st.expander('Click to view:'):
    if htmlElement:
            print = content.find_all({htmlElement})
            st.code(print)
    else:
        st.write('Loading...')

##quotes = content.find_all('div', class_='quote')
##quote_file = []
##for quote in quotes:
    ##text = quote.find('span', class_='text').text
    ##author = quote.find('small', class_='author').text
    ##link = quote.find('a')
    ##st.success(text)
    ##st.write(author)
    ##st.markdown(f"<a href=https://quotes.toscrape.com{link['href']}>{author}</a>", unsafe_allow_html=True)
    ##st.code(f"https://quotes.toscrape.com{link['href']}")
    ##quote_file.append([text,author,link['href']])

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)