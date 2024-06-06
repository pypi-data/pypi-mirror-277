import json

import click
from flask import Flask, jsonify, render_template, request


@click.command()
@click.option("--file", "-f", help="File to annotate", required=True)
@click.option("--content", "-c", help="Content to annotate", required=True)
@click.option(
    "--classification", "-l", help="Classification label column", required=True
)
def main(file, content, classification):
    print(f"Annotating {file} with {classification} column")
    with open(file, "r") as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        data = [json.loads(x) for x in data]

    # get all classification column names
    classes = set()

    for record in data:
        cl = record.get(classification.strip(), None)
        classes.add(cl)

    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def label():
        if request.method == "POST":
            form_data = request.json

            idx = form_data["idx"]
            cl = form_data["classification"]

            record = data[int(idx)]
            record[cl] = cl

            if int(idx) % 10 == 0:
                with open(file, "w") as f:
                    for record in data:
                        f.write(json.dumps(record) + "\n")

            return jsonify({"success": True, "classification": cl})

        if request.args:
            idx = request.args.get("idx")
            record = data[int(idx)]
            record["idx"] = idx
            return jsonify({"data": record})

        record = data[0]

        return render_template(
            "index.html",
            title=record["title"] if "title" in record else None,
            content=record.get(content.strip(), None),
            classification=record.get(classification.strip(), None),
            classes=[{"name": x, "id": i} for i, x in enumerate(classes)],
            idx=0,
            record_count=len(data),
        )

    app.run()
