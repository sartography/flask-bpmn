from flask import Blueprint, render_template, abort, current_app
# from crc import session, ma
# from crc.models.user import UserModel, UserModelSchema
from sqlalchemy import select
from flask_marshmallow import Marshmallow
# from jinja2 import TemplateNotFound

test_blueprint = Blueprint('test_blueprint', __name__)
                        # template_folder='templates')

@test_blueprint.route('/test_blueprint1') #, defaults={'page': 'index'})
# @simple_page.route('/<page>')
def show():
    ma = Marshmallow(current_app)
    current_app.logger.error("THIS IS TEH LOGGER", exc_info=True)
    current_app.logger.error(ma, exc_info=True)
    print(current_app)
    return "HELLO6"
    # result = db.session.execute(select(UserModel).order_by(UserModel.id))
    # all_users = session.query(UserModel).all()
    # print(UserModelSchema(many=True).dump(all_users))
    # return UserModelSchema(many=True).dump(all_users)[0]

    # return "THIS OUR BLUEPRINT"
    # try:
    #     return render_template(f'pages/{page}.html')
    # except TemplateNotFound:
    #     abort(404)
