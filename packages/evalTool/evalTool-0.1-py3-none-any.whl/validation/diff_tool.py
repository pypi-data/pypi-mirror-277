import streamlit as st
import difflib

def show_diff(before_prompt, after_prompt):
    st.text_area("Before Prompt", value=before_prompt, height=200, key="text_field_1")
    st.text_area("After Prompt", value=after_prompt, height=200, key="text_field_2")
    st.write("Button clicked! Text fields updated.")

    diff = difflib.ndiff(before_prompt.splitlines(), after_prompt.splitlines())
    print(diff)

    diff_text = ""
    for line in diff:
        if line.startswith('+ '):
            diff_text += f"<span style='color:green'>{line[2:]}</span><br>"
        else:
            diff_text += line + "<br>"

    st.markdown(diff_text, unsafe_allow_html=True)