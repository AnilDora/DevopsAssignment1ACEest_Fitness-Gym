from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for flash messages

# In-memory storage (like Tkinter version)
workouts = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_workout():
    if request.method == "POST":
        workout = request.form.get("workout")
        duration_str = request.form.get("duration")

        if not workout or not duration_str:
            flash("Please enter both workout and duration.", "error")
            return redirect(url_for("add_workout"))

        try:
            duration = int(duration_str)
            workouts.append({"workout": workout, "duration": duration})
            flash(f"'{workout}' added successfully!", "success")
            return redirect(url_for("view_workouts"))
        except ValueError:
            flash("Duration must be a number.", "error")
            return redirect(url_for("add_workout"))

    return render_template("add.html")

@app.route("/workouts")
def view_workouts():
    return render_template("workouts.html", workouts=workouts)

if __name__ == "__main__":
    app.run(debug=True)
