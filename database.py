from sqlalchemy import create_engine, text
import os

db_connection_string =  "mysql+pymysql://z4hk30xosasgf9f4c3s6:pscale_pw_ynNxOYaki0SohVzWcrSiDj8PU5C3cl1EvNkupfWDupK@us-east.connect.psdb.cloud/biessemachines?charset=utf8mb4"

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
                          val=id)
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])