import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(layout="wide")


def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
      with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("/Users/kishl/Downloads/My Projects/Portfolio/Style/style.css")

lottie_profile = load_lottie("https://lottie.host/817ea266-9538-44a5-b84f-f7a2f573457a/en9bCF8TZm.json")
lottie_contact = load_lottie("https://lottie.host/56cb3b62-fd1b-46bd-b372-40b76789e182/5dVrec5D7A.json")
pbi = Image.open("/Users/kishl/Downloads/My Projects/Portfolio/Images/salepbi.png")
mlmodel = Image.open("/Users/kishl/Downloads/My Projects/Portfolio/Images/mlmodel.png")
visualize = Image.open("/Users/kishl/Downloads/My Projects/Portfolio/Images/visualize.png")
digit = Image.open("/Users/kishl/Downloads/My Projects/Portfolio/Images/digitrecognize.png")


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #440303;
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


with st.container():
        
    st.write("##")
    st.subheader("Hey there :wave:")
    st.title("Welcome to my portfolio")
    st.write("""Go through the profile to explore the beauty.
                Uncover the hidden secrets and insights from the projects.
                Reach me out for collaborations, better job oppurtunities and project ideas""")
    st.write("---")

with st.container():
        selected = option_menu(
            menu_title= None,
            options= ['About','Projects','Contact'],
            orientation='horizontal',
            icons=['person','code-slash','chat-left-text-fill']
        )
if selected == "About":
        with st.container():
             col1, col2 = st.columns(2)
             with col1:
                  st.write("##")
                  st.title("Kishlay Kumar")
                  st.subheader("""Graduate - Haldia Institute of Technology(Haldia)
                           Key Skills: Python, SQL, Machine Learning, Streamit, Deep Learning""")
                  st.write("##")
                  
             with col2:
                    st_lottie(lottie_profile, height=230)
            
        st.write("""
                  I am a Data Science & Machine Learning enthusiast who has deep interest in the fundamental concepts of AI & loves to uncover the hidden secrets and insights from messy data! 
                  I have completed my Bachelor's in Electrical Engineering. During my 3rd Semester I developed interest in Machine Learning and started learning it.
                  As it was quite fascinating to see a model predicting & learning from its own mistakes. I love to develop data-driven applications using Machine Learning, Deep Learning, Natural Language Processing and Computer Vision!
                  I'm working towards a role where I can engage with a group of like-minded people who dream to bring revolution in the world with data! 
                  It gives me immense pleasure to perform and analyze the data, covering some useful informations which can produce some great results.""")
        
        st.write("---")
        with st.container():
              col3, col4 = st.columns(2)
              with col3:
                    st.subheader("""
                    Education
                    - ***Haldia Institute of Technology***
                        - Bachelor of Technology - Electrical Engineering
                        - Grade: 8.41
                    - ***St Karen's High School***
                        - XIIth
                        - Percent: 75.6
                    - ***St Karen's High School***
                        - Xth
                        - Grade: 9.2
                    """)
              with col4:
                    st.subheader("Experience")
                    st.write("""
                    **Freelance ~ Part Time**
                    - Sept 2023 - Present
                    - India
                    """)
                    st.write("""
                    **Cognizant ~ Internship**
                    - Mar 2023 - Aug 2023
                    - Kolkata ~ On-site
                    """)
                    st.write("""
                    **Zummit Infolabs ~ Internship**
                    - May 2022 - Jun 2022
                    - India ~ Remote
                    """)


        st.write("---")
        st.write("##")

if selected == "Projects":
      with st.container():
            st.subheader("My Projects")
            st.write("##")
            col_l, col_r = st.columns((1,2))
            with col_l:
                  st.image(pbi)
            with col_r:
                  st.subheader("Sales Analysis with PowerBi")
                  st.write("""
                  Analysis of this sales data is done to understand the changing marketing standards.
                  Further, used different datasets, merged and created relationships to provide the performance of the particular company.
                  Forecasting 6 weeks sales with PowerBi is a perfect solution for newly established startups to raise their awareness and productivity.
                  """)
                  st.markdown("[Visit Github Repo >](https://github.com/kishlayaug15/Powerbi-Sales-Analysis)")

#            st.write("##")
#           col_l, col_r = st.columns((1,2))
#           with col_l:
#                 st.image(mlmodel)
#           with col_r:
#                 st.subheader("Sales Analysis and Modelling")
#                 st.write("""
#                 Analysis of this sales data is done to understand the changing marketing standards.
#                 Further, model is built upon machine learning algorithms to provide the performance of the particular company.
#                 This model is a perfect solution for newly established startups to raise their awareness and productivity.
#                 """)
#                 st.markdown("[Visit Github Repo >](https://github.com//kishlayaug15/Rossmann-Sales-Store)")

            st.write("##")
            col_l, col_r = st.columns((1,2))
            with col_l:
                  st.image(mlmodel)
            with col_r:
                  st.subheader("Telecom Churn Prediction")
                  st.write("""
                  End to end data visualization and storytelling performance. Build pipeline, performed hyperparameter tuning on machine learning models.
                  Further, model is built upon machine learning algorithms to provide the performance of the particular company.
                  Chose final model by comparing there f1 score and accuracy score. Build a web application to utilize the logistic regression model efficiently using Streamlit.
                  """)
                  st.markdown("[Visit Github Repo >](https://github.com/kishlayaug15/Telecom-Churn-Prediction-Streamlit-App-main)")

            st.write("##")
            col_l, col_r = st.columns((1,2))
            with col_l:
                  st.image(visualize)
            with col_r:
                  st.subheader("Data Analysis(Pandas, Matplotlib, Seaborn)")
                  st.write("""
                  This project is based on a company hiring data scientists among people who successfully pass some courses which conducted by the company. 
                  So, Company wants to know which employee will remain consistent.
                  In this project, I have prepared the dataset, visualized it using different plots such as barplot, subplots, etc.
                  I have also used Q/A to get insights for better understanding.
                  """)
                  st.markdown("[Visit Github Repo >](https://github.com/kishlayaug15/HR-Analytics-Job-Change-of-Data-Scientists)")

            st.write("##")
            col_l, col_r = st.columns((1,2))
            with col_l:
                  st.image(digit)
            with col_r:
                  st.subheader("Digit Recognizer")
                  st.write("""
                  Build a digit recognizer. This project is there to recognize digit from dataset using ML, DL 
                  """)
                  st.markdown("[Visit Github Repo >](https://github.com/kishlayaug15/SVM-Digit-Recognizer)")

if selected == "Contact":
      st.header("Get In Touch With Me!")
      st.write("##")
      st.write("##")

      contact_form = """
      <form action="https://formsubmit.co/kkishlay9142@gmail.com" method="POST">
      <input type = "hidden" name ="_captcha" value = "false">
      <input type="text" name="name" placeholder = "Your name" required>
      <input type="email" name="email" placeholder = "Your email" required>
      <textarea name = "message" placeholder = "Your message" required></textarea>
      <button type="submit">Send</button>
      </form>
    """
      left_col, right_col = st.columns((2,1))
      with left_col:
            st.markdown(contact_form, unsafe_allow_html= True)
      with right_col:
            st_lottie(lottie_contact,height=245,width=450)
