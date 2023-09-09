import pickle 
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

if 'page' not in st.session_state:
    st.session_state['page'] = '/'
page_bg_img= """
<style>
[data-testid="stAppViewContainer"]{
  font-family:'Times New Roman', Times, serif;
     background-color:rgba(119, 182, 182, 0.822);
 background-size: cover;
}
[data-testid="stHeader"]{
 background-color:rgb(119, 182, 182);
 background-size: cover;
}
[data-testid="stSidebar"]{
    font-size:40px;
    background-color:rgb(119, 182, 182);
    font-family:'Times New Roman', Times, serif;
}
[data-testid="stSidebarNav"]{
    background-color:rgb(119, 182, 182);
    font-family:'Times New Roman', Times, serif;
    visibility:hidden;
  
 }
 [data-testid="stMarkdownContainer"]{
   color: rgba(31, 31, 41, 0.884);
  font-family:'Times New Roman', Times, serif;
  font-size:30px;
 }  
 [class="css-lrlib eczjsme9"]{
  icons=["house","card-text","envelope","heart-pulse-fill"]
 }
 [data-testid="collapsedControl"]{
 visibility: hidden;
 }



</style>
"""
font_style = """
    <style>
    body {
        "font-family":"'Times New Roman', Times, serif";
       font-size:30.5px;
    font-weight:40px;
        font-display:initial;
        font-style: italic;
    }
    </style>
"""
st.set_page_config(layout="wide", page_title="Diabetes Prediction System", initial_sidebar_state="expanded")
st.markdown(page_bg_img, unsafe_allow_html=True)
# use local css
def local_css(file_name):
    with open(file_name) as f :
       st.markdown(f"<style>{f.read()}<\style>", unsafe_allow_html=True)
local_css("style css/style.css") 

st.title('       ')
st.title('       ')

st.markdown(font_style, unsafe_allow_html=True)
# Define the page URLs
pages = {
    'Home': '/',
    'About': '/About',
    'Connect': '/Connect',
    'Prediction': '/prediction'
}

# Render the links
st.markdown(
    """
    <style>
    .link-list { 
        display: flex;
        list-style-type: none;
        padding: 5px;
        background-color: #f2f2f2;
        margin: 80px;
        border-radius: 25px;
        margin-lefte:80%;
        widht:100% ;
        height:40%;
        justify-content: center;
    }
    .link-list-item {
        display: flex;
       padding: 3px;
       overflow:hidden;
        text-align-last:center;
       font-style:oblique;
        font-size:50px;
       font-weight:50px;
        text-decoration:none;
       width:100%;
       justify-content:center;
       margin-right:50px;
        color:color:black;
         "font-family":"'Times New Roman', Times, serif";
    
    }
    .link-list-item:hover{
        background-color: rgb(111, 159, 223);
        color:rgba(226, 241, 247, 0.932);
        border-radius: 20px;
    
    </style>
    """,
    unsafe_allow_html=True
)

link_list = '<ul class="link-list">'
for page_name, page_url in pages.items():
    link_list += f'<li class="link-list-item"><a href="{page_url}">{page_name}</a></li> '
link_list += '</ul>'

st.markdown(link_list, unsafe_allow_html=True)

# Add your Streamlit application code for each page below

# Home Page
#if st.session_state["page"] == '/':
 #   st.title('Home Page')
    # Add your content for the home page here

# About Page
if st.session_state["page"] == '/about':
    st.title('About Page')
    # Add your content for the about page here

# Connect Page
if st.session_state["page"] == '/connect':
    st.title('Connect Page')
    # Add your content for the connect page here

# Prediction Page
if st.session_state["page"] == '/prediction':
    st.title('Prediction Page')
    # Add your content for the prediction page here

translations = {
    "English": {
        "title": "WELCOME TO DIABETES PREDICTION SYSTEM",
        "title1": "Diabetes is a blood suger disorder that affects how the body uses engergy.",
        "title2": "It occurs when the pancreas dose not produce enough of the hormone responsible for regulating blood sugar level (insulin)or when insulin is not used properly by the body.",
        "title3": "A persistently high blood sugar level can lead to serious health complications such as problems with the nerves, eyes, heart, and kidneys,",
        "Home": "Home",
        "About": "AboutUs",
        "Connect":"ContactUs",
        "Prediction":"Prediction"
    },
    "Arabic": {
        "title": "مرحبًا بكم في نظام التنبؤ بمرض السكري",
        "title1": "مرض السكري هو اضطراب مصاحب للدم يؤثر على كيفية استخدام الجسم للطاقة.",
        "title2": "يحدث عندما لا تنتج جرعة البنكرياس ما يكفي من الهرمون المسؤول عن تنظيم مستوى السكر في الدم (الأنسولين) أو عندما لا يستخدم الجسم الأنسولين بشكل صحيح.",
        "title3": "يمكن أن يؤدي ارتفاع مستوى السكر في الدم بشكل مستمر إلى مضاعفات صحية خطيرة مثل مشاكل الأعصاب والعينين والقلب والكلى ،)",
        "Home": "الرئيسية",
        "About": "معلومات عنا",
        "Connect":"اتصل بنا",
        "Prediction":"التنبؤ"
    }
}
language = st.sidebar.selectbox("", options=['English', 'Arabic'])

if language == 'Arabic':
    direction = 'rtl'
else:
    direction = 'ltr'


if language == 'Arabic':
    link_list = '<ul class="link-list" style="direction: rtl;">'
    for page_name, page_url in pages.items():
        translated_page_name = translations['Arabic'].get(page_name,page_name)
        link_list = f'<li class="link-list-item"><a href="{page_url}">{translated_page_name}</a></li> '
    link_list = '</ul>'
else:
    link_list = '<ul class="link-list" >'
    for page_name, page_url in pages.items():
        link_list = f'<li class="link-list-item"><a href="{page_url}">{page_name}</a></li> '
    link_list = '</ul>'


st.markdown(link_list, unsafe_allow_html=True)

# Add your Streamlit application code for each page below

# Home Page
#if st.session_state["page"] == '/':
 #   st.title('Home Page')
    # Add your content for the home page here

# About Page
if st.session_state["page"] == '/about':
    st.title('About Page')
    # Add your content for the about page here

# Connect Page
if st.session_state["page"] == '/connect':
    st.title('Connect Page')
    # Add your content for the connect page here

# Prediction Page
if st.session_state["page"] == '/prediction':
    st.title('Prediction Page')
    # Add your content for the prediction page here

st.markdown(f'<div style="direction: {direction}; font-size: 40px; ">{translations[language]["title"]}</div>', unsafe_allow_html=True)
st.image('https://modo3.com/thumbs/fit630x300/17290/1569497072/%D9%85%D8%A7_%D9%87%D9%8A_%D9%85%D8%B6%D8%A7%D8%B9%D9%81%D8%A7%D8%AA_%D9%85%D8%B1%D8%B6_%D8%A7%D9%84%D8%B3%D9%83%D8%B1%D9%8A.jpg', width=800)
st.markdown(f'<div style="direction: {direction}; font-size: 27px;">{translations[language]["title1"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="direction: {direction}; font-size: 27px;">{translations[language]["title2"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="direction: {direction}; font-size: 27px;">{translations[language]["title3"]}</div>', unsafe_allow_html=True)
    


