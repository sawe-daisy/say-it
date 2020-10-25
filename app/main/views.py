from flask import render_template,request,redirect,url_for,abort, flash, abort
from . import main
from .. import db, photos
from flask_login import login_required, current_user
from ..models import User, Pitch
from .forms import AddPitch, UpdateProfile
from flask.views import View, MethodView

@main.route('/', methods=['GET', 'post'])
def index():
   pitch = Pitch.query.filter_by().first()
   promotion = Pitch.query,filter_by(category='promotion')
   interview = Pitch.query,filter_by(category='interview')
   product = Pitch.query,filter_by(category='product')
   pickuplines =Pitch.query.filter_by(category='pickuplines')
   title = 'Pitch Here'

   return render_template('index.html', title=title, promotion=promotion, product= product, interview=interview, pickuplines=pickuplines)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username= uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))
    return render_template('profile/update.html', form=form)

@main.route('user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user= User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))