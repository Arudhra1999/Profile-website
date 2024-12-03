import streamlit as st

# Page Configurations
st.set_page_config(
    page_title="Arudhra Narasimhan Venkatachalam - Profile",
    page_icon=":star:",
    layout="wide"
)


# Profile Header with Picture
col1, col2 = st.columns([1, 3])

with col1:
    st.image("assets/profile-pic.png", width=150)  

with col2:
    st.title("Arudhra Narasimhan Venkatachalam")
    st.markdown("""
    📍 Daman, Daman & Diu, India | 📧 arudhralemonz@gmail.com | 📞 +91-9003492711, +91-6382289706 | 
    <a href="https://www.linkedin.com/in/arudhra-narasimhan-venkatachalam-719b63170/">LinkedIn Profile</a>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1,3])

with col2:
    st.write("Welcome to my #UnpolishedButPowerful Portfolio – a data scientist's zone where insights shine brighter than the UI!")

# About Section
st.header("Professional Summary")
st.write("""
An aspiring data scientist with expertise in predictive analytics and quality assurance automation, delivering operational efficiencies and business insights through machine learning models and automation tools. Skilled in leveraging Generative AI, fuzzy logic, and automation techniques to streamline processes and enhance business outcomes.
""")

# Work Experience Section
st.header("Work Experience")

st.subheader("Data Science Intern @ Shamal Holding, Dubai, United Arab Emirates")
st.write("June 2024 - August 2024")
st.write("""
 - Improved chatbot performance by 10% by analysing denormalized chat logs using Generative AI, driving better user insights and system interactions.
 - Implemented fuzzy logic to identify and unify similar customer records, enhancing database integrity and enabling consistent customer tracking across businesses.
 - Got engaged in predictive modelling for Dubai Real Estate time series data, applying advanced statistical techniques to forecast market trends and inform strategic decisions.
""")

st.subheader("Automation QA Engineer @ Tekion India Pvt Ltd, Chennai, Tamil Nadu, India")
st.write("November 2021 - September 2023")
st.write("""
 - Spearheaded automation initiatives, saving over 20% of manual testing time by automating regression test cases using Selenium, significantly improving testing efficiency.
 - Utilised Python (Pandas, Numpy) for data validation, improving report validation efficiency by 50%.
 - Led IoT-based Quality Assurance initiatives for a Vehicle Tracking System, reducing critical post-production issues by 45% through comprehensive test automation and monitoring solutions.
 - Conducted functional testing and created test cases for an in-house CRM and Product Master .
 - Drafted quality test cases for in-house eCommerce app ‘Tekion Store’ reducing post production issues by 70% and facilitating a smooth launch.
""")

st.subheader("Data Analytics Intern @ National University of Singapore, Singapore")
st.write("December 2019 - January 2020")
st.write("""
- Developed a CNN model for diabetic retinopathy prediction, achieving 82% accuracy.
- Created a web interface for model interaction to enhance user accessibility.
- Completed end-to-end ML pipeline processes.
""")

# Education Section
st.header("Education")
st.write("""
**Master of Science in Data Science**  
University of Birmingham, Dubai (2023-2024) | Class: Distinction  
- Chancellor’s Academic Scholarship Recipient
""") 
st.write("Course Curriculum -")

col1, col2, col3 = st.columns(3)

with col1:
    
    st.write("""
    - Visualization                         
    - Algorithms for Data Science           
    - Current topics in Data Science       
    """)

with col2:
    st.write("""
    - Storing and Managing Data
    - AI Lab
    - Data Science Group Project
    """)

with col3:
    st.write("""
    - Data Science Dissertation
    """)

st.write("""**B-Tech in Computer Science and Engineering**  
SASTRA Deemed University, Thanjavur (2017-2021) | GPA: 8.04/10 
- Graudated with First Class in Distinction
""")
st.write("Course Curriculum -")

col1, col2, col3 = st.columns(3)

with col1:
    
    st.write("""
    - Software Engineering                        
    - Compiler Engineering          
    - Artificial Intelligence
    - Cloud Computing
    - Parallel and Distributed Systems
    - Graph Theory     
    """)

with col2:
    st.write("""
    - Cryptography 
    - Operating Systems
    - Computer Networks
    - Human Computer Interaction
    - Discrete Mathematics
    - Network Administration Management and Tools
    """)

with col3:
    st.write("""
    - Microprocessor and Microcontroller (8085, 8086 and 8089)
    - Programming Languages (C, C++, Java, Python)
    """)

# Projects Section
st.header("Projects")
st.subheader(""" **1 - Real Estate Predictive Analytics**: """)
st.write("Project Description : ")
st.write("""
    - Part of my internship project at Shamal Holdings, Dubai. 
    - Dataset was gathered from REIDIN Dashboard, Dubai Pulse and Inflation data from World Bank Records. 
    - Panel data with Variable transformation like log transformations, data categorization was done for model fit.
    - Experimented with SARIMAX and ARIMAX models. Since the difference in model performance was negligible due to non-seasonality, we went ahead with ARIMAX model.
    - Correlation matrix along with forecasted results were presented to the business stakeholders.
    """)
st.write(""" Tech Stacks used :
    - Numpy, Pandas, Scikit-Learn, Matplotlib, StatsModel, Jupyter notebook, Microsoft Excel, Microsoft Powerpoint.
    """)

st.subheader(""" **2 - Speech Impediment detection using lightweight LLM and traditional ML methods**: """)
st.write("Project Description : ")
st.write("""
    - This project was the focus of my master's dissertation at the University of Birmingham. The end result is wheather the speaker in the uploaded audio is having speech stuttering or not.
    - Dataset was downloaded from Apple Machine Learning research library (Sep-28K) and Kaggle.
    - Feature engineering was implemented by converting the audio files into 16KHz mono wav audio and finally into MFCC and chroma features suing librosa library.
    - For Sep-28K dataset, I also used audio transcriptions using Open-ai whisper library.
    - DistilBert model was chosen for this project since its the lightweight version of BERT.
    - The model was trained on the encodings generated from the audio transcriptions.
    - A simple 3 layer feed forward neural network was created to generated emebeddings from MFCC and Chroma features.
    - The final output prediction is combinational output from DistilBert model and Neural Network model.
    """)
st.write(""" Tech Stacks used :
    - Transformer, Whisper, Librosa, Jupyter-notebook, Pytorch, Numpy , Pandas, Gitlab
    """)

st.subheader(""" **3 - Basketball Predictive Analytics - How Turnovers and Personal Fouls per game affect the Minutes Played conditioned on the Player's position in the game.**""")
st.write("Project Description : ")
st.write("""
    - Retrieved, transformed, and refined NBA datasets spanning 25 seasons (1997-98 to 2021-22).
    - Conducted exploratory data analysis (EDA) and generated visualizations to uncover insights and trends.
    - Utilized machine learning models (XGBoost, Random Forest, SVR) to predict player minutes based on key metrics, achieving 80% predictive accuracy. 
    - Authored the EDA report, documenting data insights , Visual Dashboard and preparatory steps for modeling.
     """)
st.write("Key Findings : ")
st.write("""
    - Confirmed turnovers and personal fouls significantly reduce playing time, with player positions influencing but not independently predictive.
    """)

st.markdown("Project Link - Coming Soon")

st.subheader(""" **4 - Video Summarization using LLM.** """)
st.write("Project Description: ")
st.write(" In Progress ........................." )
st.markdown("Project Link - Coming Soon")




# st.write("""
# - **Real Estate Predictive Analytics**: Implemented ARIMAX models for real estate forecasting in Dubai, achieving MAPE of 2-3%.
# - **Speech Impediment Detection**: Developed a multi-modal approach using LoRA fine-tuned DistilBERT and traditional ML classifiers.
# - **Flower Prediction App**: Created a web-based app using transfer learning and EfficientNet, achieving 96% accuracy.
# - **Basketball Predictive Modelling**: Used ML algorithms for player performance prediction, with EDA and hypothesis testing.
# """)

# Skills Section
st.header("Skills")
st.write("""
- **Programming & Tools**: Java, Python, Selenium, MySQL, AWS Sagemaker, Power BI, Matplolib,
Scitkit-Learn, Neural Networks, Transfer learning, Tensorflow, Pytorch, Langchain, Time Series analysis, Predictive analytics, ML
algorithms, Numpy, Pandas, Streamlit, Gradio, Seaborn, Hypothesis Testing, Statistical Analysis. .
- **Soft Skills**: Communication, Team Building, Leadership, Iterative Development.
""")

# Certifications Section
st.header("Certifications")
st.write("""
- Machine Learning by Andrew Ng (Coursera)
- Google Data Analytics Professional Certificate (Coursera)
- Practical Data Science on AWS (Coursera)
- Generative AI with Large Language Models (Coursera)
""")

st.header("Download My Resume")
with open("assets/Arudhra_Narasimhan_Venkatachalam.pdf", "rb") as file:
    resume_data = file.read()

st.download_button(
    label="📄 Download My Resume",
    data=resume_data,
    file_name="Arudhra_Narasimhan_Venkatachalam.pdf",
    mime="application/pdf"
)

# Footer
st.markdown(
    """
    <div style="position: fixed; bottom: 0; right: 0; text-align: right; color: gray;">
        🌟 Built with Streamlit | Last Updated: December 2024       
    </div>
    """,
    unsafe_allow_html=True
)