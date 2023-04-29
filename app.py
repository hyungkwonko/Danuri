from flask import Flask, render_template, request, session
from quickchart import QuickChart
import static.data.chart_type as chart_type
import openai
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)


MODEL = "gpt-3.5-turbo"

# first_input = "I want to draw a chart to show the business profits per quarter for my company and the rival company."
# first_input = "I want to draw a picture of myself."

INSTRUCTION = (
    f"Recommend the most appropriate chart type for visualizing the given context among this list: {chart_type.CHART_TYPES}. "
    + "Use chart type starts with MULTIPLE_ when you need to compare or report data more than one."
    + "Also give the reason that you choose that chart type. "
    + "Answer with the following structure: CHART_TYPE-->reason."
    # + "Do not add any additional word, but answer as it is by choosing one as written in the list. "
)

with open("./api.txt", "r") as file:
    openai.api_key = file.readlines()[0]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_id = request.form.get("form_id")

        if form_id == "form1" or form_id == "form2":
            if form_id == "form1":
                print("[INFO] proceeding form 1....")

                session["first_input"] = request.form["first_input"]
                option = request.form["option"]
                session["second_input"] = request.form.get("second_input", "")

                messages = [
                    {
                        "role": "user",
                        "content": f"{session['first_input']}\n{INSTRUCTION}",
                    },
                ]

                response = openai.ChatCompletion.create(model=MODEL, messages=messages)
                response = response["choices"][0]["message"]["content"].strip()
                response = response.split("-->", maxsplit=1)

                # sometimes the output contains . or blank in the end
                session["c_type"] = response[0].strip().replace(".", "")
                session["reason"] = response[1].strip()

                print(f"[INFO] '{response[0]}' --> '{session['c_type']}'")

                if session["second_input"]:
                    session["chart_url"] = draw_chart(
                        session["c_type"], session["second_input"]
                    )
                else:
                    session["chart_url"] = draw_chart(session["c_type"])

            else:
                print("[INFO] proceeding form 2....")

            if session["second_input"]:
                return render_template(
                    "index.html",
                    first_input=session["first_input"],
                    second_input=session["second_input"],
                    c_type=session["c_type"],
                    reason=session["reason"],
                    chart_url=session["chart_url"],
                )
            else:
                return render_template(
                    "index.html",
                    first_input=session["first_input"],
                    c_type=session["c_type"],
                    reason=session["reason"],
                    chart_url=session["chart_url"],
                )
        else:
            return render_template("index.html")
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

    # You can get the chart URL
    return qc.get_url()


if __name__ == "__main__":
    app.run(debug=True, port=8002)
