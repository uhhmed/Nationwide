from app.utils import requires_login, request_wants_json
from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort
from app.database import mongo, User

mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('/')
def index():
    # if request_wants_json():
    #     return jsonify(releases=[r.to_json() for r in releases])
    print('retrieving users from mongo')
    users = mongo.db.users.find()
    lu = [u for u in users]
    return render_template(
        'users/index.html',
        users=lu
        # latest_release=releases[-1],
        # pdf link does not redirect, needs version
        # docs version only includes major.minor
        # docs_pdf_version='.'.join(releases[-1].version.split('.', 2)[:2])
    )

@mod.route('/add', methods=['POST'])
def add_user():
    user = mongo.db.users
    obj = request.get_json()
    print(obj)
    print(obj['name'])
    name = obj['name']
    score = obj['score']
    avg_speed = obj['avg_speed']
    avg_accel = obj['avg_accel']
    user_id = user.insert({
        'name': name,
        'score': score,
        'avg_speed': avg_speed,
        'avg_accel' : avg_accel,
        })
    new_user = user.find_one({'_id': user_id })
    print(user)
    output = {
        'name': new_user['name'],
        'score': new_user['score'],
        'avg_speed': new_user['avg_speed'],
        'avg_accel' : new_user['avg_accel'],
    }
    return jsonify({'result' : output})