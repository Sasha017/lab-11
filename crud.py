from flask import Flask, request, jsonify, abort
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
# from main.model.matherial_type import MaterialType
from main.model.disponsable_table_ware import DisponsableTableWare
import copy
import json
import os

with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class GoodDisponsableTableWare(DisponsableTableWare, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacture = db.Column(db.String(20), unique=False)
    price = db.Column(db.Integer, unique=False)
    fire_resistance = db.Column(db.Integer, unique=False)
    date_of_manufacture = db.Column(db.Integer, unique=False)
    matherial = db.Column(db.Integer, unique=False)
    connection_protocol = db.Column(db.String(32), unique=False)
    data_transfer_amount = db.Column(db.Float, unique=False)

    def __init__(self, manufacture=0, price=0,
                 fire_resistance=0, date_of_manufacture=0,
                 matherial=0,
                 connection_protocol='telnet', data_transfer_amount=0.0):
        super().__init__(manufacture, price, fire_resistance, date_of_manufacture, matherial)
        self.connection_protocol = connection_protocol
        self.data_transfer_amount = data_transfer_amount


class GoodDisponsableTableWareSchema(ma.Schema):
    class Meta:
        fields = ('manufacture', 'price',
                  'fire_resistance', 'date_of_manufacture',
                  'matherial',
                  'connection_protocol', 'data_transfer_amount')


good_disponsable_table_ware_package_schema = GoodDisponsableTableWareSchema()
good_disponsable_table_ware_packages_schema = GoodDisponsableTableWareSchema(many=True)


@app.route("/good_disponsable_table_ware", methods=["POST"])
def add_good_disponsable_table_ware():
    manufacture = request.json['manufacture']
    price = request.json['price']
    fire_resistance = request.json['fire_resistance']
    date_of_manufacture = request.json['date_of_manufacture']
    matherial = request.json['matherial']
    connection_protocol = request.json['connection_protocol']
    data_transfer_amount = request.json['data_transfer_amount']
    good_disponsable_table_ware = GoodDisponsableTableWare(manufacture, price, fire_resistance, date_of_manufacture,
                                                           matherial, connection_protocol, data_transfer_amount)
    db.session.add(good_disponsable_table_ware)
    db.session.commit()
    return good_disponsable_table_ware_package_schema.jsonify(good_disponsable_table_ware)


@app.route("/good_disponsable_table_ware", methods=["GET"])
def get_good_disponsable_table_ware():
    all_good_disponsable_table_ware = GoodDisponsableTableWare.query.all()
    result = good_disponsable_table_ware_packages_schema.dump(all_good_disponsable_table_ware)
    return jsonify({'good_disponsable_table_ware': result})


@app.route("/good_disponsable_table_ware/<id>", methods=["GET"])
def good_disponsable_table_ware_detail(id):
    good_disponsable_table_ware = GoodDisponsableTableWare.query.get(id)
    if not good_disponsable_table_ware:
        abort(404)
    return good_disponsable_table_ware_package_schema.jsonify(good_disponsable_table_ware)


@app.route("/good_disponsable_table_ware/<id>", methods=["PUT"])
def good_disponsable_table_ware_update(id):
    good_disponsable_table_ware = GoodDisponsableTableWare.query.get(id)
    if not good_disponsable_table_ware:
        abort(404)
    old_good_disponsable_table_ware = copy.deepcopy(good_disponsable_table_ware)
    good_disponsable_table_ware.manufacture = request.json['manufacture']
    good_disponsable_table_ware.price = request.json['price']
    good_disponsable_table_ware.fire_resistance = request.json['fire_resistance']
    good_disponsable_table_ware.date_of_manufacture = request.json['date_of_manufacture']
    good_disponsable_table_ware.mathetial = request.json['mathetial']
    good_disponsable_table_ware.connection_protocol = request.json['connection_protocol']
    good_disponsable_table_ware.data_transfer_amount = request.json['data_transfer_amount']
    db.session.commit()
    return good_disponsable_table_ware_package_schema.jsonify(old_good_disponsable_table_ware)


@app.route("/good_disponsable_table_ware/<id>", methods=["DELETE"])
def good_disponsable_table_ware_delete(id):
    good_disponsable_table_ware = GoodDisponsableTableWare.query.get(id)
    if not good_disponsable_table_ware:
        abort(404)
    db.session.delete(good_disponsable_table_ware)
    db.session.commit()
    return good_disponsable_table_ware_package_schema.jsonify(good_disponsable_table_ware)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
