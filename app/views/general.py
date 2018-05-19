from app.utils import requires_login, request_wants_json
from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort

mod = Blueprint('general', __name__)


@mod.route('/')
def index():
    # if request_wants_json():
    #     return jsonify(releases=[r.to_json() for r in releases])
    print('test')
    return render_template(
        'general/index.html'#,
        # latest_release=releases[-1],
        # pdf link does not redirect, needs version
        # docs version only includes major.minor
        # docs_pdf_version='.'.join(releases[-1].version.split('.', 2)[:2])
    )
