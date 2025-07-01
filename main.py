import streamlit as st
from difflib import unified_diff  # Compares two texts and shows the differences line by line (like in Git)
import autopep8

st.title("🛠️ Auto Report Validator and Formatter")
st.markdown("1. Compare two reports (template vs student report)\n\n2. Auto-format Python code as per PEP8")

# --------- Report Comparison Section ---------
st.header("📄 Report Comparison")

template_file = st.file_uploader("Upload Template File", type=["txt"], key="template")
report_file = st.file_uploader("Upload Report File", type=["txt"], key="report")

def compare_reports(template, report):
    template_lines = template.splitlines()
    report_lines = report.splitlines()
    diff = unified_diff(template_lines, report_lines, lineterm='')
    return list(diff)

if template_file and report_file:
    template_text = template_file.read().decode("utf-8")
    report_text = report_file.read().decode("utf-8")

    differences = compare_reports(template_text, report_text)

    if differences:
        st.subheader("🔍 Differences Found:")
        for line in differences:
            st.text(line)
    else:
        st.success("✅ Report matches the template exactly!")

# --------- Python Code Auto Formatter Section ---------
st.header("💡 Python Code Formatter")

uploaded_file = st.file_uploader("📤 Upload your Python (.py) file", type=["py"], key="python")

if uploaded_file:
    raw_code = uploaded_file.read().decode("utf-8")
    
    st.subheader("📜 Original Code")
    st.code(raw_code, language='python')

    formatted_code = autopep8.fix_code(raw_code)

    st.subheader("✅ Formatted Code (PEP8)")
    st.code(formatted_code, language='python')

    st.download_button("⬇️ Download Formatted Code", data=formatted_code, file_name="formatted_code.py", mime="text/plain")


