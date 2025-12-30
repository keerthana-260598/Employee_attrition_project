# Employee_attrition_project
Employee Attrition Analysis and Prediction
WHY IS EMPLOYEE ATTRITION IMPORTANT? --- High attrition leads to increased hiring and training costs also affects workforce stability and overall productivity.
Predict employees likely to leave the company and identify key factors influencing attrition. 
Provide actionable insights to HR teams, Develop an interactive dashboard for real-time analysis and support data-driven HR decision-making.
Dataset includes Demographics,Performance Metrics,Job-Related features and Work-Life Balance Factors etc.
By using pandas library read the data that is safed as csv file and called in a varialbe of df.
Cleaned the data properly before preprocessing for correct accuracy by checking infomation, any duplicates , null values etc.
After this, by domain knowlegde Removed unnecessary columns which are not relaible to find the employee attrition.
Then EDA was done using seaborn, matplotlib both univariate and bivariate analysis has done by comparing with the target attrition.
Insights from EDA: *Employees with comparatively lower performance score had the highest attrition rates.
*Overtime workers had a higher tendency to leave compared to non-overtime employees. **Lower salary with increased attrition.
*Employees far from home were significantly more likely to resign.
*High-performance employees had lower attrition risk.
*Employees with higher job satisfaction had lower attrition rate
Target column was also visualised and encoded for preprocessing.
Following that other categorical columns were also encoded and scaled numerical features using StandardScaler for model compatibility and Handled outliers using Interquartile Range (IQR) method. Applied SMOTE (Synthetic Minority Over-sampling Technique) to balance class distribution.
Nextly, the completion of preprocess the features were selected and distributed as X as feature and Y as target column and after that train test split was done.
Trained the model, Used Random Forest Classifier as the primary model and Evaluated using Accuracy, Precision, Recall, F1-score, and AUC-ROC.
Model insights as The model accurately distinguishes employees at risk of leaving.
AUC-ROC score of 91% indicates strong classification performance.
Saved the model as a pickle file and then loaded in streamlit.
Technologies Used for dashboard implementation are Streamlit for frontend UI, Pandas, Seaborn, Matplotlib for data analysis & visualization, Scikit-Learn for machine learning model development.
Attrition Prediction: Enter employee details, get real-time attrition risk score.
Thankyou.




