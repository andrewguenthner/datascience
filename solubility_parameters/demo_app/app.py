import os
import math
import numpy as np
import pandas as pd
import datetime as dt
import re
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, desc

from flask import (
    Flask,
    render_template,
    jsonify,
    redirect)

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/hsp.sqlite"

db = SQLAlchemy(app)

class Solvents(db.Model):
    __tablename__= 'solvents'

    solvent_id = db.Column(db.Text, primary_key=True)
    nlm_num = db.Column(db.String())
    subst_short_name = db.Column(db.String())
    subst_display_name = db.Column(db.String())
    subst_category = db.Column(db.String())
    delta_d = db.Column(db.Float())
    delta_p = db.Column(db.Float())
    delta_h = db.Column(db.Float())
    mol_vol = db.Column(db.Float())
    src_id = db.Column(db.Integer)
    src_ref = db.Column(db.String())
    boil_pt = db.Column(db.Float())
    flash_pt = db.Column(db.Float())
    chem21_safety = db.Column(db.Integer)
    chem21_health = db.Column(db.Integer)
    chem21_env = db.Column(db.Integer)
    chem21_rank = db.Column(db.Integer)
    prop_src_id = db.Column(db.Integer())

    def __repr__(self):
        return '<Solvent %r>' % (self.subst_display_name)

class Polymers(db.Model):
    __tablename__= 'polymers'

    polymer_id = db.Column(db.Text, primary_key=True)
    subst_short_name = db.Column(db.String())
    subst_display_name = db.Column(db.String())
    delta_d = db.Column(db.Float())
    delta_p = db.Column(db.Float())
    delta_h = db.Column(db.Float())
    R0 = db.Column(db.Float())
    src_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Polymer %r>' % (self.subst_display_name)

class Substances(db.Model):
    __tablename__= 'substances'

    substance_id = db.Column(db.Text, primary_key=True)
    nlm_num = db.Column(db.String())
    subst_display_name = db.Column(db.String())
    subst_category = db.Column(db.String())
    delta_d = db.Column(db.Float())
    delta_p = db.Column(db.Float())
    delta_h = db.Column(db.Float())
    mol_vol = db.Column(db.Float())
    src_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Substance %r>' % (self.subst_display_name)

class Substance_names(db.Model):
    __tablename__= 'substancenames'

    substancename_id = db.Column(db.Text, primary_key=True)
    nlm_num = db.Column(db.String())
    subst_short_name = db.Column(db.String())

    def __repr__(self):
        return '<Substance_name %r>' % (self.subst_short_name)

@app.before_first_request
def setup():
    print("set up")
    db.create_all()
    

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("base.html")

@app.route("/estimate/<substance>")
def estimate_hsp(substance):
    """Look up substance and return delta_d, delta_p, delta_h as JSON dict, with
    added data of substance display name, molecular volume, and source info"""
    #Check input to make sure only allowed characters are included
    substance_check_pattern = re.compile('[\W_]+', re.UNICODE)
    substance_check = substance_check_pattern.sub('',substance,count=-1)
    if substance_check != substance:  #Will happen only if input has been corrupted
        return jsonify({'valid':False})
    
    # SELECT *
    # FROM Substance_Names INNER JOIN Substances ON mln_num
    # WHERE Substance_Names.subst_short_name == substance 
    hsp_result = db.session.query(Substances).\
        select_from(Substance_names).\
        join(Substances,Substance_names.nlm_num == Substances.nlm_num).\
        filter(Substance_names.subst_short_name == substance).first()
    
    output_dict = {}
    if hsp_result:
        output_dict['valid'] = True
        output_dict['display_name'] = hsp_result.subst_display_name
        output_dict['delta_d'] = hsp_result.delta_d
        output_dict['delta_p'] = hsp_result.delta_p
        output_dict['delta_h'] = hsp_result.delta_h
        output_dict['mol_vol'] = hsp_result.mol_vol
        output_dict['src_id'] = hsp_result.src_id
    else:
        output_dict['valid'] = False

    return jsonify(output_dict)



if __name__ == '__main__':
    app.run(debug=True)

