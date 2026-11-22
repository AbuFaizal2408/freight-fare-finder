from flask import Flask, render_template, request

app = Flask(__name__)

# Sample transport provider rates
providers = {
    "Mini Truck": [
        {"name": "Provider A", "base": 200, "rate": 15},
        {"name": "Provider B", "base": 250, "rate": 13},
        {"name": "Provider C", "base": 180, "rate": 17},
    ],
    "Large Truck": [
        {"name": "Provider A", "base": 500, "rate": 30},
        {"name": "Provider B", "base": 450, "rate": 35},
        {"name": "Provider C", "base": 550, "rate": 28},
    ],
}


@app.route("/", methods=["GET", "POST"])
def home():

    results = []
    error = None

    form_data = {"pickup": "", "drop": "", "vehicle": "Mini Truck", "distance": ""}

    if request.method == "POST":

        pickup = request.form.get("pickup", "").strip()
        drop = request.form.get("drop", "").strip()
        vehicle = request.form.get("vehicle", "")
        distance_input = request.form.get("distance", "").strip()

        form_data = {
            "pickup": pickup,
            "drop": drop,
            "vehicle": vehicle,
            "distance": distance_input,
        }

        try:
            distance = float(distance_input)

            if not pickup or not drop:
                error = "Please enter both pickup and drop locations."

            elif distance <= 0:
                error = "Distance must be greater than 0."

            elif not distance < float("inf"):
                error = "Please enter a valid distance."

            elif vehicle not in providers:
                error = "Please select a valid vehicle."

            else:
                for provider in providers[vehicle]:

                    fare = provider["base"] + (distance * provider["rate"])

                    results.append(
                        {
                            "name": provider["name"],
                            "fare": round(fare, 2),
                            "pickup": pickup,
                            "drop": drop,
                        }
                    )

                results.sort(key=lambda x: x["fare"])

                cheapest_fare = results[0]["fare"]

                for provider in results:
                    provider["is_cheapest"] = provider["fare"] == cheapest_fare

        except ValueError:
            error = "Please enter a valid distance greater than 0."

    return render_template(
        "index.html",
        results=results,
        error=error,
        form_data=form_data,
        vehicle=form_data["vehicle"],
        distance=form_data["distance"],
    )


if __name__ == "__main__":
    app.run(debug=True)
