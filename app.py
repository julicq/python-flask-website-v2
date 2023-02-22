from flask import Flask, render_template, jsonify

app = Flask(__name__)

BRANDS = [{
  'id': 1,
  'title': 'Biesse Wood',
  'machines': 'Rover, Selco, Opera, Skipper, Akron'
}, {
  'id': 2,
  'title': 'Biesse Glass',
  'machines': 'Master, Vertmax, Busetti, Genius'
}, {
  'id': 3,
  'title': 'Biesse Stone',
  'machines': 'Smart, Master, Movetro, Luna'
}, {
  'id': 4,
  'title': 'Biesse Materia',
  'machines': 'Rover Plast, Terma, Materia'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=BRANDS, company_name="Biesse")


@app.route("/api/brands")
def list_brands():
  return jsonify(BRANDS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
