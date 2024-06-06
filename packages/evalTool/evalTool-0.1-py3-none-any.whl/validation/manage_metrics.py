import argparse
import json

def view_custom_metrics():
    with open("metrics.json", "r") as f:
        metrics = json.load(f)

    print("Custom Metrics:")
    for i, metric in enumerate(metrics):
        name = metric["name"]
        evaluation_criteria = metric["evaluation_criteria"]
        print(f"{i+1}. {name} - {evaluation_criteria}")

def delete_custom_metric(metric_name):
    with open("metrics.json", "r+") as f:
        metrics = json.load(f)
        for metric in metrics:
            if metric["name"] == metric_name:
                metrics.remove(metric)
                print(f"Deleted metric: {metric_name}")
                break
        else:
            print(f"Metric not found: {metric_name}")
        f.seek(0)
        json.dump(metrics, f)
        f.truncate()

def main():
    parser = argparse.ArgumentParser(description="Manage custom metrics")
    subparsers = parser.add_subparsers(dest="command")

    view_parser = subparsers.add_parser("view", help="View custom metrics")
    delete_parser = subparsers.add_parser("delete", help="Delete a custom metric")
    delete_parser.add_argument("metric_name", help="Name of the metric to delete")

    args = parser.parse_args()

    if args.command == "view":
        view_custom_metrics()
    elif args.command == "delete":
        delete_custom_metric(args.metric_name)

if __name__ == "__main__":
    main()