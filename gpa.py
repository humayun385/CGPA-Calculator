import streamlit as st

st.title("🎓 GPA & CGPA Calculator") 
st.write("Easily calculate your GPA for each semester and overall CGPA.")

# Ask for total semesters
num_semesters = st.number_input("Enter number of semesters completed (including current):", min_value=1, max_value=12, value=1, step=1)

semester_gpas = []

# GPA conversion function
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

    marks = []
    for i in range(num_subjects):
        mark = st.number_input(f"Enter marks for Subject {i+1} (Semester {sem+1})", min_value=0.0, max_value=100.0, step=0.1, key=f"mark_{sem}_{i}")
        marks.append(mark)

    if len(marks) > 0:
        gpas = [marks_to_gpa(m) for m in marks]
        semester_gpa = sum(gpas) / len(gpas)
        semester_gpas.append(semester_gpa)
        st.success(f"GPA for Semester {sem+1}: **{semester_gpa:.2f}**")

# Calculate overall CGPA
if st.button("Calculate Overall CGPA"):
    if len(semester_gpas) > 0:
        overall_cgpa = sum(semester_gpas) / len(semester_gpas)
        st.balloons()
        st.info(f"🏆 Your Overall CGPA after {num_semesters} semesters is: **{overall_cgpa:.2f}**")
    else:
        st.warning("Please enter marks for at least one semester.")

# Optional: Show GPA scale
st.write("---")
st.write("### 📏 GPA Scale")
st.table({
    "Marks Range": ["85-100", "80-84", "75-79", "70-74", "65-69", "60-64", "55-59", "50-54", "<50"],
    "GPA": [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 0.0]
})
