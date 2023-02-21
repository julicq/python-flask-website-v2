from flask import Flask, render_template, jsonify

app = Flask(__name__)

BRANDS = [{
  'id': 1,
  'title': 'Biesse Wood',
  'color': 'orange'
}, {
  'id': 2,
  'title': 'Biesse Glass',
  'color': 'blue'
}, {
  'id': 3,
  'title': 'Biesse Stone',
  'color': 'red'
}, {
  'id': 4,
  'title': 'Biesse Materia',
  'color': 'violet'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=BRANDS, 
                         company_name="Biesse")

@app.route("/api/brands")
def list_brands():
  return jsonify(BRANDS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
