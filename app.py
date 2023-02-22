from flask import Flask, render_template, jsonify
from database import load_data_from_db, load_machine_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  machines = load_data_from_db()
  return render_template('home.html', machines=machines)


@app.route("/api/machines")
def list_machines():
  machines = load_data_from_db()
  return jsonify(machines)


@app.route("/api/machine/<id>")
def show_machine_json(id):
  machine = load_machine_from_db(id)
  return jsonify(machine)


@app.route("/machine/<id>")
def show_job(id):
  machine = load_data_from_db(id)

  if not machine:
    return "Not Found", 404

  return render_template('machinepage.html', machine=machine)

  if not machine:
    return "Not Found", 404
  return render_template('jobpage.html', machine=machine)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
