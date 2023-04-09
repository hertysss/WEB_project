import flask
from flask import jsonify

from . import db_session
from .offices import Office

blueprint = flask.Blueprint('offices', __name__, template_folder='templates')


@blueprint.route('/api/offices')
def get_offices():
    db_sess = db_session.create_session()
    offices = db_sess.query(Office).filter(Office.status == "свободен")
    return jsonify({'offices': [item.to_dict(only=('business_center.name',
                                                   'business_center.address',
                                                   'floor',
                                                   'area',
                                                   'bet')) for item in offices]})