# 🏦 Loan Approval Predictor - Credit Risk Analysis

## 📌 Overview
This project predicts **loan approval** and assesses **credit risk** using machine learning techniques. The dataset consists of customer loan application details, and the model predicts whether an applicant is likely to **default** or be **approved** based on financial and demographic features.

---

## 📂 Project Structure

📂 LOAN_APPROVAL_PREDICTOR
├── 📂 Data                 # Contains raw & processed datasets
│   ├── loan.csv            # Raw dataset
│   ├── processed_loan.csv   # Cleaned dataset
├── 📂 models               # Saved machine learning models
│   ├── lgbm_credit_risk.pkl # Trained LightGBM model
├── 📂 notebooks            # Jupyter notebooks for experimentation
│   ├── 01_data_exploration.ipynb  # Exploratory Data Analysis (EDA)
│   ├── 02_data_preprocessing.ipynb # Data preprocessing & feature engineering
│   ├── model_training.ipynb  # Model training & evaluation
├── 📂 src                  # Source code for deployment & utilities
│   ├── app.py              # Streamlit app for user interface
│   ├── utils.py            # Helper functions for data processing
├── 📜 .gitignore           # Files to exclude from Git tracking
├── 📜 README.md            # Project documentation
├── 📜 requirements.txt     # List of dependencies


---

## 📊 **Dataset & Features**
- **loan.csv**: Raw dataset with applicant details.
- **processed_loan.csv**: Preprocessed dataset used for training.
- **Key Features:**
  - **Applicant Income**
  - **Credit History**
  - **Loan Amount**
  - **Employment Status**
  - **Marital Status**
  - **Debt-to-Income Ratio**
  - **Previous Defaults**

---

## 🏗️ **Data Preprocessing**
✔ Handling missing values  
✔ Encoding categorical variables  
✔ Feature engineering  
✔ Handling class imbalance using **SMOTE**  

---

## 🏆 **Machine Learning Models**
The following models were tested for credit risk analysis:
✔ Logistic Regression    
✔ Decision Trees   
✔ Gradient Boosting    
✔ CatBoost     
✔ AdaBoost    
✔ XGBoost      
✔ LightGBM (Final Model)    

📌 **Evaluation Metrics**:
✔ Accuracy  
✔ Precision & Recall  
✔ ROC-AUC Curve  
✔ Confusion Matrix  

---

## 🚀 **Deployment**
The trained model is deployed using:  
- **Streamlit**: Interactive UI for users to input loan details.  
- **FastAPI** (optional): API for real-time predictions.  

---

## 📌 **Installation & Usage**
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ChiragDugar04/Loan-Approval-Predictor.git
cd Loan-Approval-Predictor



📜 Future Improvements

✔ Improve model accuracy with hyperparameter tuning
✔ Add explainability using SHAP
✔ Deploy as a web service using AWS/GCP
✔ Implement additional risk metrics

📜 License

This project is under the MIT License.
