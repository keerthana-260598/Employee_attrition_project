import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle



st.set_page_config(page_title="Employee Attrition Analysis and Prediction", layout="wide")


st.sidebar.title("📍 Navigation")

page = st.sidebar.radio("Go to", ["🔰 Project Introduction", "📊 Data Visualization EDA","🔎 Attrition Prediction" ,"👩🏻Creator Info"])


#page 4

if page == "👩🏻Creator Info":

    st.title("👩‍💻 Creator of this Project")
    st.write("""
       **Developed by:** Keerthana A  
       **Skills:** Data Preprocessing and Cleaning, Exploratory Data Analysis (EDA), Feature Engineering, Machine Learning Model Development, Model Evaluation, Streamlit Application Development 
       """)
    

    st.markdown("<h1 style='text-align: center;'>Thank You!</h1>", unsafe_allow_html=True)


elif page == "🔰 Project Introduction":

    st.title("📂 Employee Attrition Analysis and Prediction")
    st.subheader("➡️Dataset Overview")
    @st.cache_data
    def load_data():
      return pd.read_csv(r"C:\Users\ACER\Downloads\Employee-Attrition - Employee-Attrition.csv")  # same file used in notebook

    df_clean = load_data()
    st.dataframe(df_clean.head())


    st.subheader(" ➡️WHY IS EMPLOYEE ATTRITION IMPORTANT?")

    st.write("""
              ✔️High attrition leads to increased hiring and training costs.
              ✔️Affects workforce stability and overall productivity.
              ✔️Understanding key factors can help reduce turnover.
              ✔️Data-driven strategies improve employee retention.
              """)

    st.subheader("➡️BUSINESS OBJECTIVES")             

    st.write("""
             ✔️Predict employees likely to leave the company. 
             ✔️Identify key factors influencing attrition. 
             ✔️Provide actionable insights to HR teams. 
             ✔️Develop an interactive dashboard for real-time analysis. 
             ✔️Support data-driven HR decision-making.
             """)






#page 2

elif page == "📊 Data Visualization EDA" :

    df_clean = pd.read_csv(r"C:\Users\ACER\Downloads\Employee-Attrition - Employee-Attrition.csv")
    cat_cols = ['BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus','OverTime']
    


    st.subheader(" 📊 Bivariate analysis for categorical columns")

    fig = plt.figure(figsize=(15, 20))

    for i, col in enumerate(cat_cols, 1):
      plt.subplot(6, 3, i)
      sns.countplot(data=df_clean, x=col, hue="Attrition")
      plt.title(f"Attrition by {col}")
      plt.xticks(rotation=45)

    plt.tight_layout()

    st.pyplot(fig) 



    
    num_cols = ['Age','DistanceFromHome','EnvironmentSatisfaction','JobInvolvement','JobLevel','JobSatisfaction','MonthlyIncome','PerformanceRating','StockOptionLevel','WorkLifeBalance','TotalWorkingYears','YearsAtCompany']
    
    st.subheader(" 📊 Bivariate analysis for numeric columns")

    fig = plt.figure(figsize=(15, 20))

    for i, col in enumerate(num_cols, 1):
      plt.subplot(6, 3, i)
      sns.barplot(data=df_clean, x="Attrition", y=col)  # numeric on y, attrition as x
      plt.title(f"Attrition vs {col}")
      plt.xticks(rotation=45)

    plt.tight_layout()

    st.pyplot(fig)


elif page == "🔎 Attrition Prediction":
        st.subheader("Predict Employee Attrition Risk")

# loading pickle file

with open("attrition_model.pkl", "rb") as f:
    artifacts = pickle.load(f)

model = artifacts["model"]
feature_columns = artifacts["feature_columns"]


age = st.number_input("Age", min_value=18, max_value=70, value=30)

business_travel = st.selectbox("Business Travel",["Travel_Rarely", "Travel_Frequently", "Non-Travel"])

dept = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])

distance = st.number_input("Distance From Home", min_value=1, max_value=50, value=10)

education = st.selectbox("Education (1–5)", [1, 2, 3, 4, 5])

education_field = st.selectbox("Education Field", ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Other"])

env_satisfaction = st.selectbox("Environment Satisfaction (1–4)", [1, 2, 3, 4])

gender = st.selectbox("Gender", ["Male", "Female"])

job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])

job_role = st.selectbox("Job Role",["Sales Executive", "Research Scientist", "Laboratory Technician","Manufacturing Director","Healthcare Representative","Manager", "Sales Representative", "Research Director", "Human Resources"])

job_satisfaction = st.selectbox("Job Satisfaction (1–4)", [1, 2, 3, 4])

marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])

monthly_income = st.number_input("Monthly Income", min_value=0,value=5000)

monthly_rate = st.number_input("Monthly Rate", min_value=1000,value=15000)

num_companies = st.number_input("Number of Companies Worked", min_value=0, max_value=10,value=1)

overtime = st.selectbox("OverTime", ["Yes", "No"])

performance_rating = st.selectbox("Performance Rating", [1, 2, 3, 4])

relationship_satisfaction = st.selectbox("Relationship Satisfaction (1–4)", [1, 2, 3, 4])

total_work_years = st.number_input("Total Working Years", min_value=0,max_value=40,value=8)

work_life = st.selectbox("Work Life Balance (1–4)", [1, 2, 3, 4])

years_at_company = st.number_input("Years at Company", min_value=0,max_value=40,value=3)

years_in_role = st.number_input("Years in Current Role", min_value=0,max_value=20,value=2)

years_since_promo = st.number_input("Years Since Last Promotion",  min_value=0,max_value=15,value=1)

if st.button("Predict Attrition"):
  input_data = {
        "Age": [age],
        "BusinessTravel": ["Travel_Rarely"],      # default
        "Department": [dept],
        "DistanceFromHome": [10],                  # default
        "Education": [3],                          # default
        "EducationField": ["Life Sciences"],       # default
        "EnvironmentSatisfaction": [3],            # default
        "Gender": ["Male"],                        # default
        "JobLevel": [2],                           # default
        "JobRole": ["Sales Executive"],             # default
        "JobSatisfaction": [job_satisfaction],
        "MaritalStatus": [marital_status],
        "MonthlyIncome": [monthly_income],
        "MonthlyRate": [15000],                    # default
        "NumCompaniesWorked": [1],                 # default
        "OverTime": [overtime],
        "PerformanceRating": [3],                  # default
        "RelationshipSatisfaction": [3],           # default
        "TotalWorkingYears": [8],                  # default
        "WorkLifeBalance": [work_life],
        "YearsAtCompany": [years_at_company],
        "YearsInCurrentRole": [2],                 # default
        "YearsSinceLastPromotion": [1]             # default
    }



  input_df = pd.DataFrame(input_data)

# manual encoding (SAME as notebook)
# label 
input_df["OverTime"] = input_df["OverTime"].map({"Yes": 1, "No": 0})
input_df["MaritalStatus"] = input_df["MaritalStatus"].map({
    "Single": 0,
    "Married": 1,
    "Divorced": 2
})
input_df["Gender"] = input_df["Gender"].map({"Female": 1, "Male": 0})


#onehot
input_df = input_df.join(
    pd.get_dummies(input_df["BusinessTravel"])
).drop("BusinessTravel", axis=1)

input_df = input_df.join(
    pd.get_dummies(input_df["Department"], prefix="Department")
).drop("Department", axis=1)

input_df = input_df.join(
    pd.get_dummies(input_df["EducationField"], prefix="Education")
).drop("EducationField", axis=1)

input_df = input_df.join(
    pd.get_dummies(input_df["JobRole"], prefix="Role")
).drop("JobRole", axis=1)


input_df = input_df.reindex(columns=feature_columns, fill_value=0)

proba = model.predict_proba(input_df)[0, 1]   # probability of Attrition = 1
prediction = model.predict(input_df)[0]      # 0 or 1

label = "Yes" if prediction == 1 else "No"

st.subheader("Prediction Result")

st.write(f"Attrition: *{label} ({prediction})*")
st.write(f"Confidence: *{proba:.2%}*")

if prediction == 1:
    st.error("Employee is likely to leave")
else:
    st.success("Employee is likely to stay")

st.write(f"Predicted attrition probability: {proba:.2%}")

if proba >= 0.7:
    st.error("High risk of attrition")
elif proba >= 0.4:
    st.warning("Medium risk of attrition")
else:
    st.success("Low risk of attrition")
                                            



                                            






