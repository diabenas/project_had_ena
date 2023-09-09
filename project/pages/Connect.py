import json
import requests 
import pickle 
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
page_bg_img= """
<style>
[data-testid="stAppViewContainer"]{

     background-color:rgba(119, 182, 182, 0.822);

 background-size: cover;
}
[data-testid="stHeader"]{
 background-color:rgb(119, 182, 182);
 background-size: cover;
}
[data-testid="stcss-10trblm.eqr7zpz0"] {
    position: relative;
    flex: 1 1 0%;
    color:rgb(255, 255, 255);
    margin-left: calc(3rem);}
[data-testid="stp"] {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-size:25px;
    font-family:'Times New Roman', Times, serif;
}
 [data-testid="stSidebarNav"]{
font-family:'Times New Roman', Times, serif;
  background-color:rgb(119, 182, 182);
 }
  [data-testid="stMarkdownContainer"]{
   color: rgba(31, 31, 41, 0.884);
  font-family:'Times New Roman', Times, serif;
 }  
[data-baseweb="select"]{
 color: rgba(31, 31, 41, 0.884);
 font-family:'Times New Roman', Times, serif;
}
[data-testid="stDataFrameResizable"]{
 font-family:'Times New Roman', Times, serif;
}
[role="slider"]{
  background-color: rgba(31, 31, 41, 0.884);
}
[class="st-dl st-dm st-dn st-do st-dy st-dq st-b8 st-dr st-ds"]
{
 background-color: rgba(31, 31, 41, 0.884);
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
translations = {
    "English": {
        "title": "WELCOME TO contactus",
        "title1": "Get In Touch With Me!",
        "name":"your Name",
        "email":"your Email",
        "message":"your message",
        "send":"Send",
        "home": "Home",
        "about": "AboutUs",
        "contact":"ContactUs",
        "pred_page":"Prediction"
        
    },
    "Arabic": {
        "title": "مرحبا بكم في الاتصال بنا",
        "title1": "الحصول على اتصال معي!",
        "name":"اسمك",
        "email":"بريدك الالكتروني ",
        "message":"رسالتك ",
        "send":"ارسال",
        "home": "الرئيسية",
        "about": "معلومات عنا",
        "contact":"اتصل بنا",
        "pred_page":"التنبؤ"
    }
}
language = st.sidebar.selectbox("", options=['English', 'Arabic'])
# Set the page title using the browser tab title
if language == 'Arabic':
    direction = 'rtl'
else:
    direction = 'ltr'
def load_lottieurl(url):
    r = requests.get( url)
    if r.status_code != 200:
      return None
    return r.json()

# ---load asses ------
lottie_connect = load_lottieurl("https://lottie.host/01404331-19f6-4efc-8b35-a50e4c7c5844/T0xhGWF7rj.json")


st.markdown(font_style, unsafe_allow_html=True)

home =translations[language]["home"]
about = translations[language]["about"]
contact = translations[language]["contact"]
pred_page = translations[language]["pred_page"]

selected = option_menu (
    menu_title=None ,
    options=[home, about, contact, pred_page ],
    icons=["house","card-text","envelope","heart-pulse-fill"],
    default_index=0,
    orientation="horizontal",
    styles= {
         "container":{"padding":"0!important"," background-color":" #f2f2f2"},
         "icon":{"color":"blue","font-size":"15.5px"},
         "nav-link":{
            "font-size":"15.5px",
            "text-align":"left",
            "margin":"0px",
            "--hover-color":"rgb(111, 159, 223)",
        },
        "nav-link-selected":{" background-color":"skyblue"}
    }
)
st.markdown(page_bg_img, unsafe_allow_html=True)
#Upload Data

#Data=pickle.load(open(r'C:\Users\GISlaptop2\diabetes_model.sav', 'rb'))
st.title('       ')
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
    
def load_lottieurl(url):
    r = requests.get( url)
    if r.status_code != 200:
      return None
    return r.json()
st.markdown(f'<div style="direction: {direction}; font-size: 40px; ">{translations[language]["title"]}</div>', unsafe_allow_html=True)

# use local css
def local_css(file_name):
    with open(file_name) as f :
       st.markdown(f"<style>{f.read()}<\style>", unsafe_allow_html=True)
local_css("style css/style.css") 

with st.container():
    st.write("---")
    left_column ,right_column ,cl3= st.columns ([2,1,2])
    with left_column:
        st_lottie(lottie_connect,height=300 , key="connect")
     
    with right_column:
        st.title('       ')
        st.markdown("""
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="40" fill="currentColor" class="bi bi-envelope-at-fill" viewBox="0 0 16 16">
        <path d="M2 2A2 2 0 0 0 .05 3.555L8 8.414l7.95-4.859A2 2 0 0 0 14 2H2Zm-2 9.8V4.698l5.803 3.546L0 11.801Zm6.761-2.97-6.57 4.026A2 2 0 0 0 2 14h6.256A4.493 4.493 0 0 1 8 12.5a4.49 4.49 0 0 1 1.606-3.446l-.367-.225L8 9.586l-1.239-.757ZM16 9.671V4.697l-5.803 3.546.338.208A4.482 4.482 0 0 1 12.5 8c1.414 0 2.675.652 3.5 1.671Z"/>
        <path d="M15.834 12.244c0 1.168-.577 2.025-1.587 2.025-.503 0-1.002-.228-1.12-.648h-.043c-.118.416-.543.643-1.015.643-.77 0-1.259-.542-1.259-1.434v-.529c0-.844.481-1.4 1.26-1.4.585 0 .87.333.953.63h.03v-.568h.905v2.19c0 .272.18.42.411.42.315 0 .639-.415.639-1.39v-.118c0-1.277-.95-2.326-2.484-2.326h-.04c-1.582 0-2.64 1.067-2.64 2.724v.157c0 1.867 1.237 2.654 2.57 2.654h.045c.507 0 .935-.07 1.18-.18v.731c-.219.1-.643.175-1.237.175h-.044C10.438 16 9 14.82 9 12.646v-.214C9 10.36 10.421 9 12.485 9h.035c2.12 0 3.314 1.43 3.314 3.034v.21Zm-4.04.21v.227c0 .586.227.8.581.8.31 0 .564-.17.564-.743v-.367c0-.516-.275-.708-.572-.708-.346 0-.573.245-.573.791Z"/>
       </svg>
       """,unsafe_allow_html=True) 
        st.title('       ')
       
        st.markdown("""
          <svg xmlns="http://www.w3.org/2000/svg" width="30" height="50" fill="currentColor" class="bi bi-telephone-fill" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M1.885.511a1.745 1.745 0 0 1 2.61.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/>
          </svg>""",unsafe_allow_html=True)
     
    with cl3:
       st.title('       ')
       st.write("nosa19diab99@gmail.com","nosa19diab99@gmail.com") 
       st.title('       ')

       st.write("218944878771")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.markdown(f'<div style="direction: {direction}; font-size: 40px; ">{translations[language]["title1"]}</div>', unsafe_allow_html=True)
    st.write("##")
    #--- format----

    contact_form = """
        
       <form action="https://formsubmit.co/codingisfun.hadielaboudieb@gmail.com" method="POST">
           <input type="hidden" name ="_captcha" value="false">
           <label>{}</label>
           <input type="text" name="name" planceholder="{}" required>
           <labal>{}</labal>
           <input type="email" name="email"  planceholder="{}" required>
           <labal>{}</labal>
           <textarea name ="message"  planceholder="{}" required></textarea>
           <button type="submit">{}</button>
       </form>
    """.format(
        translations[language]["name"],
        translations[language]["name"],
        translations[language]["email"],
        translations[language]["email"],
        translations[language]["message"],
        translations[language]["message"],
        translations[language]["send"]
    )
    left_column,right_column = st.columns(2)
    with left_column:
       st.markdown(contact_form, unsafe_allow_html=True )
    with right_column:
        st.empty()

