from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)


def generate_plots(csv_filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_filename)

    # Create plots using Plotly Express
    length_of_road = df["X-coordinate"].max() - df["X-coordinate"].min()
    total_potholes = len(df)
    low_potholes = len(df[df["Area_Classification"] == "Low"])
    moderate_potholes = len(df[df["Area_Classification"] == "Medium"])
    high_potholes = len(df[df["Area_Classification"] == "High"])
    highest_depth = df["Actual_Depth"].max()
    severity = df["Depth_Classification"].value_counts()

    fig_length_of_road = px.bar(df, x="Area_Classification", title="Area Severity")
    fig_length_of_road.update_layout(height=400)
    fig_length_of_road.update_layout(
        title=dict(text="Area Severity", font=dict(color="maroon"))
    )

    fig_severity = px.pie(
        severity, values=severity.values, names=severity.index, title="Depth Severity"
    )
    # Add more plots as needed
    fig_severity.update_layout(height=400)
    fig_severity.update_layout(
        title=dict(text="Depth Severity", font=dict(color="maroon"))
    )

    fig_additional_1 = px.scatter(
        df,
        x="X-coordinate",
        y="Y-coordinate",
        title="Geographical Distribution of Potholes",
    )
    # Add additional plots as needed
    fig_additional_1.update_layout(height=300)
    fig_additional_1.update_layout(
        title=dict(
            text="Geographical Distribution of Potholes", font=dict(color="maroon")
        )
    )

    return (
        fig_length_of_road,
        total_potholes,
        low_potholes,
        moderate_potholes,
        high_potholes,
        highest_depth,
        fig_severity,
        fig_additional_1,
    )


@app.route("/")
def index():
    # Specify the CSV file name
    csv_filename = "./templates/pothole_data.csv"

    # Generate plots and retrieve information
    (
        fig_length_of_road,
        total_potholes,
        low_potholes,
        moderate_potholes,
        high_potholes,
        highest_depth,
        fig_severity,
        fig_additional_1,
    ) = generate_plots(csv_filename)

    # Read the first Pothole ID from the CSV file
    pothole_id = pd.read_csv(csv_filename)["Pothole ID"].iloc[0]

    return render_template(
        "dashboard.html",
        fig_length_of_road=fig_length_of_road.to_html(),
        total_potholes=total_potholes,
        low_potholes=low_potholes,
        moderate_potholes=moderate_potholes,
        high_potholes=high_potholes,
        highest_depth=highest_depth,
        fig_severity=fig_severity.to_html(),
        fig_additional_1=fig_additional_1.to_html(),
        pothole_id=pothole_id,
    )


if __name__ == "__main__":
    app.run(debug=True)
