import difflib
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.set_page_config('Python Webscraper', ':mag:', layout='wide')
st.title(':mag:' + " " + 'Python WebScraper')

tab1, tab2 = st.tabs(['WebScraper 1','WebScraper 2'])

with tab1:
    st.title('Sample Of WebScraper Application:')
    tag = st.selectbox('Choose a topic', ['love', 'humor','life','books','world','value'])
    generate = st.button('Create CSV File')
    url = f"https://quotes.toscrape.com/tag/{tag}/"
    st.write(url)
    res = requests.get(url)
    content = BeautifulSoup(res.content, 'html.parser')
    with st.expander('Click to view the html element:'):
        st.code(content)
    quotes = content.find_all('div', class_='quote')
    quote_file = []
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        link = quote.find('a')
        st.success(text)
        st.write(author)
        st.markdown(f"<a href=https://quotes.toscrape.com{link['href']}>{author}</a>", unsafe_allow_html=True)
        ##st.code(f"https://quotes.toscrape.com{link['href']}")
        quote_file.append([text,author,link['href']])

    if generate:
        try:
            df = pd.DataFrame(quote_file)
            df.to_csv('quotes.csv', index=False, 
            header=['Quote','Author','Link'],encoding='cp1252')
        
        except:
            st.write('Loading...')

with tab2:
    st.title('WebScraping A Website:')
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

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)