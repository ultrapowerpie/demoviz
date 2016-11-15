import calendar, time
from flask import Flask, Blueprint, render_template, redirect, \
                  url_for, session, escape, request
from app import db
from util.models import User

admin = Blueprint('admin', __name__)


################################################################################
#   Rendering templates                                                        #
################################################################################

admin_key = "ultrapowerpie"


EXPIRATION = 1800


expired_key = 'Your demo has expired.\n Please contact ' \
              'guanghao@princeton.edu to request another demo key, ' \
              'or click "About" to try again. '

invalid_key = 'You do not have a valid key.\n Please contact ' \
              'guanghao@princeton.edu to request a demo key, ' \
              'or click "About" to try again. ' \

demo = "Please enter your demo key for a 30 minute demo session."


demo_admin = "USER CREATION"


def check_session(default):
    if 'time' not in session:
        return render_template("invalid.html", mes = invalid_key, starttime=-1,
                                expire=EXPIRATION)

    if (calendar.timegm(time.gmtime())-session['time']) > EXPIRATION:
        return render_template("invalid.html", mes = expired_key, starttime=-1,
                                expire=EXPIRATION)

    return default

def quick_render(graphURL, main, side, side_desc):
    if 'time' not in session:
        session['time'] = -1

    return check_session(render_template("visualize.html",
                                        graphURL=graphURL,
                                        main=main,
                                        side=side,
                                        side_desc=side_desc,
                                        starttime=session['time'],
                                        expire=EXPIRATION))


################################################################################
#                                                                              #
#   Administrative Pages                                                       #
#                                                                              #
################################################################################


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if 'time' in session:
        if (calendar.timegm(time.gmtime()) - session['time']) < EXPIRATION:

            return check_session(render_template("about.html",
                                                  starttime=session['time'],
                                                  expire=EXPIRATION))

    if request.method == 'POST':
        u = User.query.filter(User.username ==
                                request.form['username']).first()
                                
        if request.form['username'] == admin_key:

            if u:
                db.session.delete(u)
                db.session.commit()

            new_u = User(username=admin_key, time=calendar.timegm(time.gmtime()))
            db.session.add(new_u)
            db.session.commit()

            session['username'] = admin_key
            session['time'] = new_u.time

            return redirect(url_for('admin.create'))

        else:
            if not u:
                return render_template("invalid.html", mes=invalid_key,
                                        starttime=-1, expire=EXPIRATION)

            session['username'] = u.username
            session['time'] = u.time
            if u.time < 0:
                new_u = User(username=u.username,
                             time=calendar.timegm(time.gmtime()))
                session['time'] = new_u.time
                db.session.delete(u)
                db.session.commit()
                db.session.add(new_u)
                db.session.commit()

        return check_session(render_template("about.html",
                                              starttime=session['time'],
                                              expire=EXPIRATION))

    return render_template("login.html",
                            demo_desc=demo,
                            starttime=-1,
                            expire=EXPIRATION)


@admin.route('/create', methods=['GET', 'POST'])
def create():
    if 'username' in session and session['username'] == admin_key:

        if request.method == 'POST':

            u = User.query.filter(User.username == request.form['username']).first()
            if u:
                db.session.delete(u)
                db.session.commit()

            new_u = User(username=request.form['username'], time=-1)
            db.session.add(new_u)
            db.session.commit()

        userlist=User.query.all()
        users = []
        for u in userlist:
            users.append([u.username, time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(u.time))])

        return render_template("create.html",
                            demo_desc=demo_admin,
                            starttime=session['time'],
                            expire=EXPIRATION,
                            users=users)

    return render_template("invalid.html", mes = invalid_key, starttime=-1,
                                expire=EXPIRATION)


@admin.route("/")
def index():
    return redirect(url_for('admin.login'))
