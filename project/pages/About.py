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
st.markdown(font_style, unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)
# use local css
def local_css(file_name):
    with open(file_name) as f :
       st.markdown(f"<style>{f.read()}<\style>", unsafe_allow_html=True)
local_css("style css/style.css") 
translations = {
    "English": {
        "title": "ABOUT US",
        "title1": "On our diabetes prediction site, we utilize various machine learning algorithms to predict the likelihood of diabetes based on the user's input. The algorithms we employ include:",
        "title2":"1.Decision Tree Classifier: This algorithm constructs a decision tree model by recursively partitioning the data based on different features. It makes predictions by following the learned tree structure, which consists of decision nodes and leaf nodes",
        "title3":"2.Support Vector Machines (SVM): SVM is a powerful algorithm for both classification and regression tasks. It works by finding the optimal hyperplane that separates the data points into different classes while maximizing the margin between them.",
        "title4":"3.Artificial Neural Network (ANN) with Backpropagation: ANNs are inspired by the structure and functioning of biological neural networks، It involves propagating the errors backward through the network to adjust the weights and biases, optimizing the network's performance.",
        "title5":"These algorithms collectively offer a diverse set of approaches to diabetes prediction. By leveraging their unique characteristics, we aim to provide accurate and reliable predictions to our users",
        "home": "Home",
        "about": "AboutUs",
        "contact":"ContactUs",
        "pred_page":"Prediction"       
    },
    "Arabic": {
        "title": "معلومات عنا",
        "title1": "في موقعنا للتنبؤ بمرض السكري، نستخدم خوارزميات مختلفة للتعلم الآلي للتنبؤ باحتمالية الإصابة بمرض السكري بناءً على مدخلات المستخدم. تشمل الخوارزميات التي نستخدمها ما يلي :",
        "title2":"1.مصنف شجرة القرار: تقوم هذه الخوارزمية ببناء نموذج شجرة القرار عن طريق تقسيم البيانات بشكل متكرر بناءً على ميزات مختلفة. فهو يقوم بالتنبؤات باتباع بنية الشجرة المستفادة، والتي تتكون من عقد القرار والعقد الورقية",
        "title3":" 2.Support Vector Machines (SVM): SVM هي خوارزمية قوية لكل من مهام التصنيف والانحدار. إنه يعمل من خلال إيجاد المستوى التشعبي الأمثل الذي يفصل نقاط البيانات إلى فئات مختلفة مع زيادة الهامش بينها. ",
        "title4":"3.الشبكة العصبية الاصطناعية (ANN) مع الانتشار العكسي: الشبكات العصبية الاصطناعية مستوحاة من بنية وعمل الشبكات العصبية البيولوجية، وتتضمن نشر الأخطاء إلى الخلف عبر الشبكة لضبط الأوزان والتحيزات، وتحسين أداء الشبكة. ",
        "title5":"تقدم هذه الخوارزميات مجتمعة مجموعة متنوعة من الأساليب للتنبؤ بمرض السكري. ومن خلال الاستفادة من خصائصها الفريدة، نهدف إلى تقديم تنبؤات دقيقة وموثوقة لمستخدمينا",
        "home": "الرئيسية",
        "about": "معلومات عنا",
        "contact":"اتصل بنا",
        "pred_page":"التنبؤ"
    }
}
language = st.sidebar.selectbox("", options=['English', 'Arabic'])
if language == 'Arabic':
    direction = 'rtl'
else:
    direction = 'ltr'

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

st.markdown(f'<div style="direction: {direction}; font-size: 40px; ">{translations[language]["title"]}</div>', unsafe_allow_html=True)
st.write("---")     
st.image("https://www.annahar.com/ContentFiles/230839Image1.jpg?version=3105757",width=600 )   
st.title('       ')
st.markdown(f'<div style="direction: {direction}; font-size: 24px; ">{translations[language]["title1"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="direction: {direction}; font-size: 24px; ">{translations[language]["title2"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="direction: {direction}; font-size: 24px; ">{translations[language]["title3"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="direction: {direction}; font-size: 24px; ">{translations[language]["title4"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="direction: {direction}; font-size: 24px; ">{translations[language]["title5"]}</div>', unsafe_allow_html=True)
