# 🏦 Loan Approval Predictor - Credit Risk Analysis

## 📌 Overview
This project predicts **loan approval** and assesses **credit risk** using machine learning techniques. The dataset consists of customer loan application details, and the model predicts whether an applicant is likely to **default** or be **approved** based on financial and demographic features.

---

## 📂 Project Structure
# 💂️ Project Structure
```
PNEUMONIA_DETECTION_PROJECT/
│
│
├── Data/
│   └── loan.csv
│   └── processed_loan.csv 
│
├── models/
│   ├── lgbm_credit_risk.pkl
│   ├── training_feature.npy
│
├── Notebooks/
│   ├── 01_data_exploration.ipynb  # Exploratory Data Analysis (EDA)
│   ├── 02_data_preprocessing.ipynb # Data preprocessing & feature engineering
│   ├── model_training and testing.ipynb 
│
├── 📂 src                  # Source code for deployment & utilities
│   ├── app.py              # Streamlit app for user interface
│   ├── utils.py
|
├── .gitignore
├── README.md
└── requirements.txt

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

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ChiragDugar04/Loan-Approval-Predictor.git
cd Loan-Approval-Predictor



## 🤖 Future Improvements
- ✨ Implement Grad-CAM to visualize CNN attention on the images.
- ✨ Train on a larger dataset for more generalizable predictions.
- ✨ Create a REST API for model inference.

---

## 📝 License
This project is open-source and available under the **MIT License**.
