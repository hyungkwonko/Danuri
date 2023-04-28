from flask import Flask, render_template, request
from quickchart import QuickChart
import static.data.chart_type as chart_type
import openai

app = Flask(__name__)


MODEL = "gpt-3.5-turbo"

with open("./api.txt", "r") as file:
    openai.api_key = file.readlines()[0]

# first_input = "I want to draw a chart to show the business profits per quarter for my company and the rival company."
# first_input = "I want to draw a picture of myself."

original = (
    f"Recommend the most appropriate chart type for visualizing the given context among this list: {chart_type.CHART_TYPES}. "
    + "Also give the reason that you choose that chart type. "
    + "Answer with the following structure: CHART_TYPE-->reason."
    # + "Do not add any additional word, but answer as it is by choosing one as written in the list. "
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_input = request.form["first_input"]
        option = request.form["option"]
        second_input = request.form.get("second_input", "")

        messages = [
            {
                "role": "user",
                "content": f"{first_input}\n{original}",
            },
        ]

        response = openai.ChatCompletion.create(model=MODEL, messages=messages)
        response = response["choices"][0]["message"]["content"].strip()
        response = response.split("-->", maxsplit=1)

        if second_input:
            chart_url = draw_chart(response[0], second_input)

            return render_template(
                "index.html",
                c_type=response[0],
                reason=response[1],
                chart_url=chart_url,
            )
        else:
            chart_url = draw_chart(response[0])
            return render_template(
                "index.html",
                c_type=response[0],
                reason=response[1],
                chart_url=chart_url,
            )
    else:
        return render_template("index.html")


def draw_chart(c_type, detail=None):
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.version = "2"

    if detail:
        messages = [
            {
                "role": "user",
                "content": f"Refer to the given information and generate a data by replacing FAKEs of the given format:\n"
                + f"information: {detail}.\n"
                + f"format: {chart_type.CHART_DICT[c_type]}.",
            },
        ]
    else:
        messages = [
            {
                "role": "user",
                "content": f"Please generate a dummy data by replacing FAKEs from the below format: {chart_type.CHART_DICT[c_type]}",
            },
        ]

    response = openai.ChatCompletion.create(model=MODEL, messages=messages)

    # Config can be set as a string or as a nested dict
    qc.config = response["choices"][0]["message"]["content"].strip()

    # You can get the chart URL...
    return qc.get_url()


if __name__ == "__main__":
    app.run(debug=True, port=8002)
