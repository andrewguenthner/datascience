from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import csv
import glob
import psycopg2
import os

# db configuration
app = Flask(__name__)

app.config['DEBUG'] = False
DB_URL = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class HSP(db.Model):
    """Model for the countries table"""
    __tablename__ = 'hsp_all'

    id = db.Column(db.Integer, primary_key = True)
    nlm_num = db.Column(db.String())
    subst_name = db.Column(db.String())
    delta_d = db.Column(db.Float())
    delta_p = db.Column(db.Float())
    delta_h = db.Column(db.Float())
    mol_vol = db.Column(db.Float())
    src_id = db.Column(db.Integer)
    src_ref = db.Column(db.String())
    chem21_safety = db.Column(db.Integer)
    chem21_health = db.Column(db.Integer)
    chem21_env = db.Column(db.Integer)
    chem21_rank = db.Column(db.Integer)


def main():
    """Sets up Postgres database, imports a set of csv's from the Output_data file,
    then loads the data into the database based on how the data is arrayed in each csv"""
    db.create_table('hsp_all')
   
if __name__ == '__main__':
    main()