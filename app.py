from flask import Flask, render_template, request, jsonify
from database import get_connection
from hostel import save_entry
from face import scan_person
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templetes"),
    static_folder=str(BASE_DIR / "static")
)


@app.route("/")
def home():
    return render_template("hs.html")


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data["name"]
    room = data["room"]

    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO students(name, room) VALUES(%s, %s)"
    values = (name, room)

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Student Registered Successfully"})


@app.route("/entry", methods=["POST"])
def entry():

    data = request.get_json()

    name = data["name"]

    save_entry(name)

    return jsonify({"message": "Entry Saved Successfully"})


@app.route("/students")
def students():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(students)


@app.route("/scan")
def scan():

    scan_person()

    return jsonify({"message": "Scanning Completed"})


if __name__ == "__main__":
    print("Project Folder :", BASE_DIR)
    print("Template Folder :", app.template_folder)
    print("Static Folder :", app.static_folder)

    app.run(debug=True)