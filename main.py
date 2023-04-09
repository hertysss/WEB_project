from flask import Flask, render_template, redirect, request, abort, make_response, jsonify
from data import db_session
from data import offices_api

from data.business_centers import Business_center
from data.offices import Office
from data.users import User

from forms.business_center import Business_centerForm
from forms.office import OfficeForm
from forms.user import RegisterForm, LoginForm

from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pupupu'
app.config['JSON_AS_ASCII'] = False
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    business_centers = db_sess.query(Business_center).all()
    return render_template("index.html",
                           current_user=current_user,
                           title="Аренда коммерческой недвижимости в Москве",
                           business_centers=business_centers)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('forms/reg.html',
                                   title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('forms/reg.html',
                                   title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            role=form.role.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('forms/reg.html',
                           title='Регистрация',
                           form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        return render_template('forms/auth.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('forms/auth.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/add_business_center',  methods=['GET', 'POST'])
@login_required
def add_business_center():
    print(f"Запрос на cоздание бизнес-центра")
    form = Business_centerForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        bc = Business_center()
        bc.name = form.name.data
        bc.address = form.address.data
        bc.building = form.building.data
        bc.district = form.district.data
        bc.metro = form.metro.data
        bc.total_area = form.total_area.data
        bc.klass = form.klass.data
        bc.floors = form.floors.data
        bc.lift = form.lift.data
        bc.parking = form.parking.data
        bc.contact = form.contact.data
        current_user.business_centers.append(bc)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('forms/business_center.html',
                           title='Добавление бизнес-центра',
                           form=form)


@app.route('/edit_business_center/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_business_center(id):
    print(f"Запрос на редактирование бизнес-центра с id:{id}")
    form = Business_centerForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        bc = db_sess.query(Business_center).filter(Business_center.id == id,
                                                   Business_center.user == current_user).first()
        print(bc)
        if bc:
            form.name.data = bc.name
            form.address.data = bc.address
            form.building.data = bc.building
            form.district.data = bc.district
            form.metro.data = bc.metro
            form.total_area.data = bc.total_area
            form.klass.data = bc.klass
            form.floors.data = bc.floors
            form.lift.data = bc.lift
            form.parking.data = bc.parking
            form.contact.data = bc.contact
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        bc = db_sess.query(Business_center).filter(Business_center.id == id,
                                                   Business_center.user == current_user).first()
        if bc:
            bc.name = form.name.data
            bc.address = form.address.data
            bc.building = form.building.data
            bc.district = form.district.data
            bc.metro = form.metro.data
            bc.total_area = form.total_area.data
            bc.klass = form.klass.data
            bc.floors = form.floors.data
            bc.lift = form.lift.data
            bc.parking = form.parking.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('forms/business_center.html',
                           title='Редактирование характеристик бизнес-центра',
                           form=form)


@app.route('/del_business_center/<int:id>', methods=['GET', 'POST'])
@login_required
def del_business_center(id):
    print(f"Запрос на удаление бизнес-центра с id:{id}")
    db_sess = db_session.create_session()
    bc = db_sess.query(Business_center).filter(Business_center.id == id,
                                               Business_center.user == current_user).first()
    if bc:
        print(bc)
        ofs = db_sess.query(Office).filter(Office.business_center_id == id).all()
        for of in ofs:
            db_sess.delete(of)
        db_sess.delete(bc)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route("/card_business_center/<int:id>")
@login_required
def card_business_center(id):
    db_sess = db_session.create_session()
    business_center = db_sess.query(Business_center).filter(Business_center.id == id).first()
    return render_template("cards/business_center.html",
                           current_user=current_user,
                           title="Характеристики бизнес-центра",
                           business_center=business_center)


@app.route('/bc<int:bc_id>/add_office',  methods=['GET', 'POST'])
@login_required
def add_office(bc_id):
    print(f"Запрос на cоздание офиса")
    form = OfficeForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        of = Office()
        of.area = form.area.data
        of.floor = form.floor.data
        of.bet = form.bet.data
        of.status = form.status.data
        of.business_center_id = bc_id
        current_user.offices.append(of)

        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('forms/office.html',
                           title='Добавление офиса',
                           form=form)


@app.route('/edit_office/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_office(id):
    print(f"Запрос на редактирование офиса с id:{id}")
    form = OfficeForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        of = db_sess.query(Office).filter(Office.id == id,
                                          Office.user == current_user).first()
        print(of)
        if of:
            form.area.data = of.area
            form.floor.data = of.floor
            form.bet.data = of.bet
            form.status.data = of.status
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        of = db_sess.query(Office).filter(Office.id == id,
                                          Office.user == current_user).first()
        if of:
            of.area = form.area.data
            of.floor = form.floor.data
            of.bet = form.bet.data
            of.status = form.status.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('forms/office.html',
                           title='Редактирование характеристик офиса',
                           form=form)


@app.route('/del_office/<int:id>', methods=['GET', 'POST'])
@login_required
def del_office(id):
    print(f"Запрос на удаление офиса с id:{id}")
    db_sess = db_session.create_session()
    of = db_sess.query(Office).filter(Office.id == id,
                                      Office.user == current_user).first()
    if of:
        print(of)
        #db_sess.delete(of)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')

@app.route("/card_office/<int:id>")
@login_required
def card_office(id):
    db_sess = db_session.create_session()
    office = db_sess.query(Office).filter(Office.id == id).first()
    return render_template("cards/office.html",
                           current_user=current_user,
                           title="Характеристики офиса",
                           office=office)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(offices_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()