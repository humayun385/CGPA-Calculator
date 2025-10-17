import streamlit as st

st.title("🎓 GPA & CGPA Calculator with Credit Hours")
st.write("Calculate your semester-wise GPA and overall CGPA based on your marks and credit hours.")

# Ask number of semesters
num_semesters = st.number_input("Enter total number of semesters (including current):", min_value=1, max_value=12, value=1, step=1)

semester_gpas = []
semester_credit_totals = []

# Function to convert marks to GPA (on 4.0 scale)
def marks_to_gpa(mark):
    if mark >= 85:
        return 4.0
    elif mark >= 80:
        return 3.7
    elif mark >= 75:
        return 3.3
    elif mark >= 70:
        return 3.0
    elif mark >= 65:
        return 2.7
    elif mark >= 60:
        return 2.3
    elif mark >= 55:
        return 2.0
    elif mark >= 50:
        return 1.7
    else:
        return 0.0

# Loop through semesters
for sem in range(num_semesters):
    st.write(f"### 📚 Semester {sem+1}")

    num_subjects = st.number_input(f"How many subjects in Semester {sem+1}?", min_value=1, max_value=20, value=5, step=1, key=f"subjects_{sem}")

    total_points = 0
    total_credits = 0

    # Collect marks and credit hours for each subject
    for i in range(num_subjects):
        col1, col2 = st.columns(2)
        with col1:
            mark = st.number_input(f"Marks for Subject {i+1} (Semester {sem+1})", min_value=0.0, max_value=100.0, step=0.1, key=f"mark_{sem}_{i}")
        with col2:
            credit = st.number_input(f"Credit Hours for Subject {i+1}", min_value=1.0, max_value=5.0, step=0.5, key=f"credit_{sem}_{i}")

        gpa = marks_to_gpa(mark)
        total_points += gpa * credit
        total_credits += credit

    # Calculate semester GPA
    if total_credits > 0:
        semester_gpa = total_points / total_credits
        semester_gpas.append(semester_gpa)
        semester_credit_totals.append(total_credits)
        st.success(f"🎯 GPA for Semester {sem+1}: **{semester_gpa:.2f}**")

# Calculate overall CGPA
if st.button("Calculate Overall CGPA"):
    if len(semester_gpas) > 0:
        weighted_sum = sum(g * c for g, c in zip(semester_gpas, semester_credit_totals))
        total_credits_all = sum(semester_credit_totals)
        overall_cgpa = weighted_sum / total_credits_all
        st.balloons()
        st.info(f"🏆 Your Overall CGPA after {num_semesters} semesters is: **{overall_cgpa:.2f}**")
    else:
        st.warning("Please enter marks and credit hours for at least one semester.")

# GPA scale table
st.write("---")
st.write("### 📏 GPA Conversion Scale")
st.table({
    "Marks Range": ["85-100", "80-84", "75-79", "70-74", "65-69", "60-64", "55-59", "50-54", "<50"],
    "GPA": [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 0.0]
})
