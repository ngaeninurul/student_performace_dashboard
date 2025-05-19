import streamlit as st
import pandas as pd
import joblib
import xgboost

# Load model dan fitur
model = joblib.load('xgb_model.pkl')
feature_list = joblib.load('feature_list.pkl')

st.markdown("<h1 style='text-align: center;'>🎓 Student Dropout Prediction 🎓</h1>", unsafe_allow_html=True)
st.subheader(" ")

# ============================
# 🧑‍🎓 Personal Information
# ============================
st.header("🧑‍🎓 Personal Information")

col1, col2, col3 = st.columns(3)
with col1:
    gender_options = {
        "Select":0,
        "Male": 1,
        "Female": 0
    }
    selected_gender_label = st.selectbox("Gender", list(gender_options.keys()))
    Gender = gender_options[selected_gender_label]

with col2:
    Age_at_enrollment = st.number_input("Age at Enrollment", 0)
    
with col3:
    displaced_options = {
        "Select":0,
        "No": 0,
        "Yes": 1
    }
    selected_displaced_label = st.selectbox("Displaced", list(displaced_options.keys()))
    Displaced = displaced_options[selected_displaced_label]

col4, col5, col6 = st.columns(3)
with col4:
    educational_special_needs_options = {
        "Select":0,
        "No": 0,
        "Yes)": 1
    }
    selected_edu_needs_label = st.selectbox("Educational Special Needs", list(educational_special_needs_options.keys()))
    Educational_special_needs = educational_special_needs_options[selected_edu_needs_label]
    
with col5:
    debtor_options = {
        "Select":0,
        "No": 0,
        "Yes": 1
    }
    selected_debtor_label = st.selectbox("Debtor", list(debtor_options.keys()))
    Debtor = debtor_options[selected_debtor_label]
    
with col6:
    tuition_options = {
        "Select":0,
        "No": 0,
        "Yes": 1
    }
    selected_tuition_label = st.selectbox("Tuition Fees Up to Date", list(tuition_options.keys()))
    Tuition_fees_up_to_date = tuition_options[selected_tuition_label]

col7, col8 = st.columns(2)
with col7:
    scholarship_options = {
        "Select":0,
        "No": 0,
        "Yes": 1
    }
    selected_scholarship_label = st.selectbox("Scholarship Holder", list(scholarship_options.keys()))
    Scholarship_holder = scholarship_options[selected_scholarship_label]

with col8:
    international_options = {
        "Select":0,
        "No": 0,
        "Yes": 1
        }
    selected_international_label = st.selectbox("International", list(international_options.keys()))
    International = international_options[selected_international_label]
 
# ============================
# 📘 Academic Information
# ============================
st.header("📘 Academic Information")

col9, col10, col11 = st.columns(3)
with col9:
    application_mode_options = {
        0: "Select",
        1: "1st phase - general contingent",
        2: "Ordinance No. 612/93",
        5: "1st phase - special contingent (Azores Island)",
        7: "Holders of other higher courses",
        10: "Ordinance No. 854-B/99",
        15: "International student (bachelor)",
        16: "1st phase - special contingent (Madeira Island)",
        17: "2nd phase - general contingent",
        18: "3rd phase - general contingent",
        26: "Ordinance No. 533-A/99, item b2) (Different Plan)",
        27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
        39: "Over 23 years old",
        42: "Transfer",
        43: "Change of course",
        44: "Technological specialization diploma holders",
        51: "Change of institution/course",
        53: "Short cycle diploma holders",
        57: "Change of institution/course (International)"
        }
    selected_label = st.selectbox("Application Mode", list(application_mode_options.values()))
    Application_mode = [k for k, v in application_mode_options.items() if v == selected_label][0]
    
with col10:
    course_options = {
        "Select":0,
        "Biofuel Production Technologies": 33,
        "Animation and Multimedia Design": 171,
        "Social Service (evening attendance)": 8014,
        "Agronomy": 9003,
        "Communication Design": 9070,
        "Veterinary Nursing": 9085,
        "Informatics Engineering": 9119,
        "Equinculture": 9130,
        "Management": 9147,
        "Social Service": 9238,
        "Tourism": 9254,
        "Nursing": 9500,
        "Oral Hygiene": 9556,
        "Advertising and Marketing Management": 9670,
        "Journalism and Communication": 9773,
        "Basic Education": 9853,
        "Management (evening attendance)": 9991
        }
    selected_course_label = st.selectbox("Course", list(course_options.keys()))
    Course = course_options[selected_course_label]
    
with col11:
    Previous_qualification_grade = st.number_input("Previous Qualification Grade", min_value=0.0, max_value=2000.0, step=0.1)

col12, col13, col14 = st.columns(3)
with col12:
    Admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=2000.0, step=0.1)

with col13:
    Curricular_units_1st_sem_enrolled = st.number_input("1st Semester - Enrolled Units", 0)

with col14:
    Curricular_units_1st_sem_approved = st.number_input("1st Semester - Approved Units", 0)

col15, col16, col17 = st.columns(3)
with col15:
    Curricular_units_1st_sem_grade = st.number_input("1st Semester - Grade", 0.0)
    
with col16:
    Curricular_units_1st_sem_without_evaluation = st.number_input("1st Semester - Without Evaluation", 0)
    
with col17:
    Curricular_units_2nd_sem_enrolled = st.number_input("2nd Semester - Enrolled Units", 0)

col18, col19, col20 = st.columns(3)
with col18:
    Curricular_units_2nd_sem_approved = st.number_input("2nd Semester - Approved Units", 0)
    
with col19:
    Curricular_units_2nd_sem_grade = st.number_input("2nd Semester - Grade", 0.0)
    
with col20:
    Curricular_units_2nd_sem_without_evaluation = st.number_input("2nd Semester - Without Evaluation", 0)

# ============================
# 🌍 Demographic Information
# ============================
st.header("🌍 Demographic Information")

col1, col2, col3 = st.columns(3)
with col1:
    marital_status_options = {
        "Select":0,
        "Single": 1,
        "Married": 2,
        "Widower": 3,
        "Divorced": 4,
        "Facto Union": 5,
        "Legally Separated": 6
    }
    selected_marital_status_label = st.selectbox("Marital Status", list(marital_status_options.keys()))
    Marital_status = marital_status_options[selected_marital_status_label]

with col2:
    nationality_options = {
        "Select":0,
        "Portuguese": 1,
        "German": 2,
        "Spanish": 6,
        "Italian": 11,
        "Dutch": 13,
        "English": 14,
        "Lithuanian": 17,
        "Angolan": 21,
        "Cape Verdean": 22,
        "Guinean)": 24,
        "Mozambican": 25,
        "Santomean": 26,
        "Turkish": 32,
        "Brazilian": 41,
        "Romanian": 62,
        "Moldova (Republic of)": 100,
        "Mexican": 101,
        "Ukraine": 103,
        "Russian": 105,
        "Cuban": 108,
        "Colombian": 109
    }
    selected_nationality_label = st.selectbox("Nationality", list(nationality_options.keys()))
    Nacionality = nationality_options[selected_nationality_label]
    
with col3:
    mother_qualification_options = {
        "Select":0,
        "Secondary Education - 12th Year or Eq.": 1,
        "Higher Education - Bachelor's Degree": 2,
        "Higher Education - Degree": 3,
        "Higher Education - Master's": 4,
        "Higher Education - Doctorate": 5,
        "Frequency of Higher Education": 6,
        "12th Year - Not Completed": 9,
        "11th Year - Not Completed": 10,
        "10th Year of Schooling": 14,
        "Basic Education 3rd Cycle (9th/10th/11th) or Eq.": 19
    }
    selected_mother_qualification_label = st.selectbox("Mother Qualification", list(mother_qualification_options.keys()))
    Mother_qualification = mother_qualification_options[selected_mother_qualification_label]

col4, col5, col6 = st.columns(3)
with col4:
    father_qualification_options = {
        "Select": 0,
        "Secondary Education - 12th Year or Eq.": 1,
        "Higher Education - Bachelor's Degree": 2,
        "Higher Education - Degree": 3,
        "Higher Education - Master's": 4,
        "Higher Education - Doctorate": 5,
        "Frequency of Higher Education": 6,
        "12th Year - Not Completed": 9,
        "11th Year - Not Completed": 10,
        "10th Year of Schooling": 14,
        "Basic Education 3rd Cycle (9th/10th/11th) or Eq.": 19
    }
    selected_father_qualification_label = st.selectbox("Father Qualification", list(father_qualification_options.keys()))
    Father_qualification = father_qualification_options[selected_father_qualification_label]

with col5:
    mother_occupation_options = {
        
        "Select": 0,
        "Student": 0,
        "Legislative/Executive/Directors/Managers": 1,
        "Intellectual and Scientific Specialists": 2,
        "Intermediate Technicians and Professions": 3,
        "Administrative Staff": 4,
        "Services/Security/Sellers": 5,
        "Agriculture/Fisheries/Forestry Skilled Workers": 6,
        "Industry/Construction/Craftsmen Skilled Workers": 7,
        "Machine Operators and Assemblers": 8,
        "Unskilled Workers": 9,
        "Armed Forces": 10,
        "Other Situation": 90,
        "(blank)": 99,
        "Health Professionals": 122,
        "Teachers": 123,
        "ICT Specialists": 125,
        "Science/Engineering Technicians": 131,
        "Health Technicians": 132,
        "Legal/Social/Cultural Technicians": 134,
        "Office Workers/Secretaries/Data Entry": 141,
        "Finance/Stats/Registry Operators": 143,
        "Other Admin Support Staff": 144,
        "Personal Service Workers": 151,
        "Sellers": 152,
        "Personal Care Workers": 153,
        "Construction Workers (except electricians)": 171,
        "Craftsmen/Precision/Jewelers": 173,
        "Food/Clothing/Wood Industry Workers": 175,
        "Cleaning Workers": 191,
        "Unskilled Agriculture/Fisheries Workers": 192,
        "Unskilled Industry/Construction/Transport Workers": 193,
        "Meal Preparation Assistants": 194
    }
    selected_mother_occupation_label = st.selectbox("Mother Occupation", list(mother_occupation_options.keys()))
    Mother_occupation = mother_occupation_options[selected_mother_occupation_label]

with col6:
    father_occupation_options = {
        "Select": 0,
        "Student": 0,
        "Legislative/Executive/Directors/Managers": 1,
        "Intellectual and Scientific Specialists": 2,
        "Intermediate Technicians and Professions": 3,
        "Administrative Staff": 4,
        "Services/Security/Sellers": 5,
        "Agriculture/Fisheries/Forestry Skilled Workers": 6,
        "Industry/Construction/Craftsmen Skilled Workers": 7,
        "Machine Operators and Assemblers": 8,
        "Unskilled Workers": 9,
        "Armed Forces Professions": 10,
        "Other Situation": 90,
        "(blank)": 99,
        "Armed Forces Officers)": 101,
        "Armed Forces Sergeants": 102,
        "Other Armed Forces Personnel": 103,
        "Administrative/Commercial Services Directors": 112,
        "Hospitality/Trade/Services Directors": 114,
        "Physical Science/Engineering Specialists": 121,
        "Health Professionals": 122,
        "Teachers": 123,
        "Finance/Admin/Relations Specialists": 124,
        "Science/Engineering Technicians": 131,
        "Health Technicians": 132,
        "Legal/Social/Cultural Technicians": 134,
        "ICT Technicians": 135,
        "Office Workers/Secretaries/Data Entry": 141,
        "Finance/Stats/Registry Operators": 143,
        "Other Admin Support Staff": 144,
        "Personal Service Workers": 151,
        "Sellers": 152,
        "Personal Care Workers": 153,
        "Security Services Personnel": 154,
        "Market-Oriented Farmers": 161,
        "Subsistence Farmers/Fishermen/Hunters": 163,
        "Construction Workers (except electricians)": 171,
        "Metalworking Skilled Workers": 172,
        "Electricians/Electronics Skilled Workers": 174,
        "Food/Wood/Clothing Industry Workers": 175,
        "Fixed Plant/Machine Operators": 181,
        "Assembly Workers": 182,
        "Vehicle Drivers/Equipment Operators": 183,
        "Unskilled Agriculture/Fisheries Workers": 192,
        "Unskilled Industry/Construction/Transport Workers": 193,
        "Meal Preparation Assistants": 194,
        "Street Vendors/Service Providers": 195
    }
    selected_father_occupation_label = st.selectbox("Father Occupation", list(father_occupation_options.keys()))
    Father_occupation = father_occupation_options[selected_father_occupation_label]

# ============================
# Gabungkan ke DataFrame
# ============================
df = pd.DataFrame([{
    'Select':0,
    'Application_mode': Application_mode,
    'Course': Course,
    'Previous_qualification_grade': Previous_qualification_grade,
    'Admission_grade': Admission_grade,
    'Displaced': Displaced,
    'Educational_special_needs': Educational_special_needs,
    'Debtor': Debtor,
    'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
    'Scholarship_holder': Scholarship_holder,
    'International': International,
    'Age_at_enrollment': Age_at_enrollment,
    'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
    'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
    'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
    'Curricular_units_1st_sem_without_evaluation': Curricular_units_1st_sem_without_evaluation,
    'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
    'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
    'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
    'Curricular_units_2nd_sem_without_evaluation': Curricular_units_2nd_sem_without_evaluation,
    'Gender': Gender,
    'Marital_status': Marital_status,
    'Nacionality': Nacionality,
    'Mother_qualification': Mother_qualification,
    'Father_qualification': Father_qualification,
    'Mother_occupation': Mother_occupation,
    'Father_occupation': Father_occupation
}])

# ============================
# Fitur turunan
# ============================
df['total_enrolled_units'] = df['Curricular_units_1st_sem_enrolled'] + df['Curricular_units_2nd_sem_enrolled']
df['total_approved_units'] = df['Curricular_units_1st_sem_approved'] + df['Curricular_units_2nd_sem_approved']
df['total_grade'] = df['Curricular_units_1st_sem_grade'] + df['Curricular_units_2nd_sem_grade']
df['total_without_evaluation'] = df['Curricular_units_1st_sem_without_evaluation'] + df['Curricular_units_2nd_sem_without_evaluation']
df['approval_ratio'] = df['total_approved_units'] / df['total_enrolled_units'].replace(0, 1)
df['average_grade'] = df['total_grade'] / df['total_enrolled_units'].replace(0, 1)

# One-hot encoding dan sesuaikan dengan fitur model
df = pd.get_dummies(df)
df = df.reindex(columns=feature_list, fill_value=0)

# Prediksi
st.subheader("")
if st.button("🔍 Predict Student Status"):
    prediction = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]

    if prediction == 1:
        st.markdown(
            f"""<br>
            <div style='
                background-color:#ffe6e6;
                padding:20px;
                border-radius:10px;
                border-left:10px solid #ff4d4d;
                font-size:22px'>
                ⚠️ <strong style='color:#cc0000; font-size:26px;'>Potential Dropout Risk</strong><br>
                📉 <span style='color:#4d0000; font-size:18px;'>Probability:</span> <strong style='color:#4d0000; font-size:18px;'>{proba * 100:.2f}%</strong>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""<br>
            <div style='
                background-color:#e6ffe6;
                padding:20px;
                border-radius:10px;
                border-left:10px solid #33cc33;
                font-size:22px'>
                ✅ <strong style='color:#006600; font-size:26px;'>No Dropout Risk</strong><br>
                📈 <span style='color:#004d00; font-size:18px;'>Probability:</span> <strong style='color:#004d00; font-size:18px;'>{proba * 100:.2f}%</strong>
            </div>
            """,
            unsafe_allow_html=True
        )