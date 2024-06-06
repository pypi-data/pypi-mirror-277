import argparse
import json

def add_custom_metric():
    parser = argparse.ArgumentParser(description="Add a custom metric")
    parser.add_argument("name", help="Metric name")
    parser.add_argument("evaluation_criteria", help="Evaluation criteria")
    args = parser.parse_args()

    try:
        with open('metrics.json', 'r') as f:
            metrics = json.load(f)
    except FileNotFoundError:
        metrics = []

    metrics.append({"name": args.name, "evaluation_criteria": args.evaluation_criteria})
    with open('metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)

    print("Metric added successfully!")

if __name__ == "__main__":
    add_custom_metric()