import pickle 
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
#background-image: url("https://modo3.com/thumbs/fit630x300/17290/1569497072/%D9%85%D8%A7_%D9%87%D9%8A_%D9%85%D8%B6%D8%A7%D8%B9%D9%81%D8%A7%D8%AA_%D9%85%D8%B1%D8%B6_%D8%A7%D9%84%D8%B3%D9%83%D8%B1%D9%8A.jpg");
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
[data-testid="stSidebarNav"]{
  background-color:rgb(119, 182, 182);
  font-family:'Times New Roman', Times, serif;
 }
 [data-testid="stMarkdownContainer"]{
   color: rgba(31, 31, 41, 0.884);
  font-family:'Times New Roman', Times, serif;
 } 
[data-baseweb="select"]{
 color: rgba(31, 31, 41, 0.884);
 font-family:'Times New Roman', Times, serif;
 width: 120px;
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
[class=" css-1r1r1bt ellz0s83"]{
    width: 200px;
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
#st.set_page_config(layout="wide", page_title="Diabetes Prediction System", initial_sidebar_state="expanded")

st.markdown(font_style, unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)
# use local css
def local_css(file_name):
    with open(file_name) as f :
       st.markdown(f"<style>{f.read()}<\style>", unsafe_allow_html=True)
local_css("style css/style.css") 
def get_translation(key, language):
    translations = {
        'home': {
            'English': 'Home',
            'Arabic': 'الرئيسية'
        },
        'about': {
            'English': 'AboutUs',
            'Arabic': 'معلومات عنا'
        },
        'contact': {
            'English': 'ContactUs',
            'Arabic': 'اتصل بنا'
        },
        'pred_page': {
            'English': 'Prediction',
            'Arabic': 'التنبؤ'
        },
        'title1': {
            'English': 'Diabetes Prediction',
            'Arabic': 'توقع مرض السكري'
        },
        'title2': {
            'English': 'Easy Application For Prediction Diabetes',
            'Arabic': 'تطبيق سهل للتنبؤ بالسكري'
        },
        'modeles': {
            'English': 'Choose a prediction model:',
            'Arabic': ':اختر نموذج التنبؤ'   
        },
        'model_names': {
            'English': ['SVM', 'Decision Tree', 'ANN'],
            'Arabic': [' دعم آلات المتجهات', ' شجرة القرار', ' الشبكة العصبية']
        },
        'yes_no_options': {
            'English': ['Yes', 'No'],
            'Arabic': ['نعم', 'لا']
        },
        'Age':{
            'English': 'age',
            'Arabic': 'العمر', 
        },
        'CurrentSmoker':{
            'English': 'Are you a current smoker?',
            'Arabic':  'هل أنت مدخن حاليًا؟',
        },
        'BPMeds': {
            'English': 'Are you on blood pressure medication? ',
            'Arabic':  ' هل تتناول أدوية ضغط الدم؟' ,
        },
        'PrevalentHyp':{
            'English': 'Do you have prevalent hypertension?' ,
            'Arabic':  ' هل تعاني من ارتفاع ضغط الدم المنتشر؟',
        },
        'SysBP': {
            'English': 'Systolic Blood Pressure ',
            'Arabic': ' ضغط الدم الانقباضي',
        },
        'DiaBP': {
            'English': 'Diastolic Blood Pressure',
            'Arabic': ' ضغط الدم الانبساطي', 
        },
        'BMI': {
            'English': 'Body Mass Index ',
            'Arabic': 'مؤشر كتلة الجسم ', 
        },
        'HeartRate': {
            'English': 'Heart Rate',
            'Arabic': 'معدل ضربات القلب', 
        },
        'Glucose': {
            'English': 'Glucose Level',
            'Arabic': 'مستوى الجلوكوز', 
        },
        'TenYearCHD' :{
            'English': 'Ten-Year Coronary Heart Disease Risk',
            'Arabic': 'مخاطر أمراض القلب التاجية على مدى عشر سنوات', 
        },
        'predict': {
            'English': 'Predict',
            'Arabic': 'تنبؤ', 
        },
        'prediction': {
            'English': 'You are in good health, keep it up',
            'Arabic': 'أنت بصحة جيدة ، استمر في ذلك',
        },
        'predi': {
            'English': 'You should consult a doctor as soon as possible',
            'Arabic': 'يجب عليك استشارة الطبيب في أسرع وقت ممكن',
             
        }
    }

    return translations.get(key, {}).get(language, f"No translation found for '{key}' in '{language}'")

# Choose the language
language = st.sidebar.selectbox("", options=['English', 'Arabic'])
if language == 'Arabic':
    direction = 'rtl'
else:
    direction = 'ltr'

home = get_translation('home', language)
about = get_translation('about', language)
contact = get_translation('contact', language)
pred_page = get_translation('pred_page', language)

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

title1 = get_translation('title1', language)
st.title(title1)
title2 = get_translation('title2', language)
st.write(title2)
st.title('       ')
# Get translated title
titles = get_translation('modeles', language)
st.sidebar.title(titles)

# Get translated model names'
model_names = get_translation('model_names', language)

# Display the models
selected_model = st.sidebar.selectbox("", options=model_names)
if selected_model == "SVM" or selected_model == " دعم آلات المتجهات":
    Data=pickle.load(open(r'C:\Users\HNEC5\diabetes_model1.sav', 'rb'))
elif selected_model == "Decision Tree" or selected_model == " شجرة القرار" :
    Data=pickle.load(open(r'C:\Users\HNEC5\diabetes_model2.sav', 'rb'))
elif selected_model == "ANN" or selected_model == " الشبكة العصبية" :
    Data=pickle.load(open(r'C:\Users\HNEC5\diabetes_model3.sav', 'rb'))
     
def convert_yes_no(value):
        if value.lower() == 'yes':
            return 1
        elif value.lower() == 'نعم':
            return 1
        elif value.lower() == 'no':
            return 0 
        elif value.lower() == 'لا':
            return 0
def user_data():
        st.markdown(f'<div style="direction:  font-size: 1px;">{get_translation("Age", language)}</div>', unsafe_allow_html=True)
        age = st.number_input(get_translation("Age", language), value=1, step=1)
        st.markdown(f'<div style="direction:  font-size: 5px;">{get_translation("CurrentSmoker", language)}</div>', unsafe_allow_html=True)
        currentSmoker = st.radio("CurrentSmoker",get_translation('yes_no_options', language))
        st.markdown(f'<div style="direction:  font-size: 5px;">{get_translation("BPMeds", language)}</div>', unsafe_allow_html=True)
        BPMeds = st.radio("BPMeds",get_translation('yes_no_options', language))
        st.markdown(f'<div style="direction:  font-size: 20px;">{get_translation("PrevalentHyp", language)}</div>', unsafe_allow_html=True)
        PrevalentHyp = st.radio("PrevalentHyp",get_translation('yes_no_options', language))
        st.markdown(f'<div style="direction:  font-size: 20px;">{get_translation("SysBP", language)}</div>', unsafe_allow_html=True)
        sysBP = st.number_input("SysBP",value=0.0, step=0.1)
        st.markdown(f'<div style="direction:  font-size: 20px;">{get_translation("DiaBP", language)}</div>', unsafe_allow_html=True)
        diaBP = st.number_input("DiaBP",value=0.0, step=0.1)
        st.markdown(f'<div style="direction:  font-size: 20px;">{get_translation("BMI", language)}</div>', unsafe_allow_html=True)
        BMI = st.number_input("BMI",value=0.0, step=0.1)
        st.markdown(f'<div style="direction:  font-size: 20px;">{get_translation("HeartRate", language)}</div>', unsafe_allow_html=True)
        heartRate = st.number_input("HeartRate",value=0.0, step=0.1)
        st.markdown(f'<div style="direction:  font-size: 20px;">{get_translation("Glucose", language)}</div>', unsafe_allow_html=True)
        glucose = st.number_input("Glucose",value=0.0, step=0.1)
        st.markdown(f'<div style="direction:  font-size: 20px;">{get_translation("TenYearCHD", language)}</div>', unsafe_allow_html=True)
        TenYearCHD = st.radio("TenYearCHD",(get_translation('yes_no_options', language)))
    
        currentSmoker= convert_yes_no(currentSmoker)
        PrevalentHyp= convert_yes_no( PrevalentHyp)
        BPMeds = convert_yes_no(BPMeds)
        TenYearCHD= convert_yes_no(TenYearCHD)
        df=pd.DataFrame({'age':[age],'currentSmoker':[currentSmoker],'BPMeds':[BPMeds],'PrevalentHyp':[PrevalentHyp],
                  'sysBP':[sysBP],'diaBP':[diaBP],'BMI':[BMI],
                  'heartRate':[heartRate],'glucose':[glucose],'TenYearCHD':[TenYearCHD]}, index=[0])
        return df

user = user_data()
st.write(user) 
predict = get_translation('predict', language)
predict=st.button(predict)
if predict:
    result=Data.predict(user)
    if result == 0: 
        st.title('       ')
        st.title('       ')
        pred = get_translation('prediction', language)
        st.write(pred)
        st.image('https://o.remove.bg/downloads/95e2e93e-5c2a-4d8a-8d95-6f285e98533a/lightbox-with-words-good-health-care-health-medical-concept-world-health-day_99432-5398-removebg-preview.png', width=250)
    else:
        st.title('       ')
        st.title('       ')
        predi = get_translation('predi', language)
        st.write(predi , font_size=90)
        st.image('https://assets.telegraphindia.com/telegraph/5e5b81e5-e60f-42d9-8f3f-d2e5f1a691e1.jpg', width=250)

