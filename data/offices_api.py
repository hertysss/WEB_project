from flask import jsonify
import flask
import sqlalchemy.orm as orm
from db_session import create_session
from __all_models import Office

blueprint = flask.Blueprint(
    'offices_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/offices')
def get_offices():
    session = create_session()

    office = session.query(Office).filter(Office.status == False).options(
        orm.joinedload(Office.business_center)).all()

    res = []
    for office in office:
        office_dict = {
            'Площадь': office.area,
            'Этаж': office.floor,
            'Ставка': office.bet,
            'Название бизнес центра': office.business_center.name,
            'Адресс бизнес центра': office.business_center.address
        }
        res.append(office_dict)

    session.close()

    return jsonify(res)