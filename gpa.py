import streamlit as st

st.title("🎓 GPA & CGPA Calculator")

st.write("Enter your marks (out of 100) for each subject:")

# Number of subjects
num_subjects = st.number_input("How many subjects do you have?", min_value=1, max_value=20, value=5, step=1)

marks = []
for i in range(num_subjects):
    mark = st.number_input(f"Enter marks for Subject {i+1}", min_value=0.0, max_value=100.0, step=0.1)
    marks.append(mark)

# Function to convert marks to GPA (on a 4.0 scale)
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

if st.button("Calculate GPA & CGPA"):
    gpas = [marks_to_gpa(m) for m in marks]
    gpa = sum(gpas) / len(gpas)
    # For simplicity, assume CGPA = average GPA (you can extend it to multiple semesters)
    cgpa = gpa  

    st.success(f"📘 GPA for this semester: **{gpa:.2f}**")
    st.info(f"🏆 Estimated CGPA: **{cgpa:.2f}**")

    # Optional: Show grade points table
    st.write("---")
    st.write("### GPA Scale")
    st.table({
        "Marks Range": ["85-100", "80-84", "75-79", "70-74", "65-69", "60-64", "55-59", "50-54", "<50"],
        "GPA": [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 0.0]
    })
