import streamlit as st
import json
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams

def create_custom_metric():
    try:
        with open('metrics.json', 'r') as f:
            metrics = json.load(f)
    except FileNotFoundError:
        metrics = []

    st.title("Add your metric")
    with st.form("user_input_form"):
        name = st.text_input("Enter metric name")
        evaluation_criteria_input = st.text_input("Enter evaluation criteria")

        if st.form_submit_button("Submit"):
            # Append the new metric to the list
            metrics.append({"name": name, "evaluation_criteria": evaluation_criteria_input})
            # Write the updated list to the JSON file
            with open('metrics.json', 'w') as f:
                json.dump(metrics, f, indent=4)

            st.success("Metric added successfully!")
    