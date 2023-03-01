from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_data_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from machines"))
    machines = []
    for row in result.all():
      machines.append(row._asdict())
    return machines


def load_machine_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM machines WHERE id = :val"),
                          {'val': id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


def app_request_to_db(machine_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO requests (machine_id, full_name, email, company, proj_description) VALUES (:machine_id, :full_name, :email, :company, :proj_description)"
    )
    conn.execute(
      query, {
        'machine_id': machine_id,
        'full_name': data['full_name'],
        'email': data['email'],
        'company': data['company'],
        'proj_description': data['proj_description']
      })
