import streamlit as st
import json


def view_custom_metrics():
    with open("metrics.json", "r") as f:
        metrics = json.load(f)

    st.title("Custom Metrics")

    counter = 0
    for metric in metrics:
        name = metric["name"]
        evaluation_criteria = metric["evaluation_criteria"]
        
        # Create a container for each metric
        container = st.container()

        # Write the metric information inside the container
        container.markdown(f"**Metric:** {name}")
        container.markdown(f"**Criteria:** {evaluation_criteria}")
        delete_button = container.button(f"Delete", key=f"delete_{name}_{counter}")

        if delete_button:
            metrics.remove(metric)
            with open("metrics.json", "w") as f:
                json.dump(metrics, f)
            st.experimental_rerun()