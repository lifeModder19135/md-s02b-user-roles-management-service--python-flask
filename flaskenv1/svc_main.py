from flask import Flask
from sqlalchemy import eventsession
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY-DATABASE-URI'] = 'sqlite:///data/test.db'
db = SQLAlchemy(app)

SVC_INFO = {
    'SVC_ID': 'MD_S03',
    'SVC_NAME': 'User Role Management Service',
    'VERSION': '0.0.1',
    'Environment': 'Development'
}


@app.route('/')
def return_info():
    return 'Hello World!'


@app.route('/')
def has_role():
    return


@app.route('/')
def create_new_user_role(user_id):
    # Check db for user_id, if none:
    #   open session:
    #   write new USER record
    #   write new EVENT record
    #   close session
    # if user_id already exists:
    #   raise userAlreadyExists exception
    return


@app.route('/getcurrentrolefor/<userid>')
def return_current_role():
    return 'Hello World!'


@app.route('/getrolehistoryfor/<userid>')
def return_previous_roles():
    return 'Hello World!'


@app.route('/getallpossibleroles')
def return_all_roles():
    return 'Hello World!'


def change_user_role(user_id, role):
    """service helper method: Change role for the user with user_id to the role provided, or else raise a
    'SpecifiedChangeNotPossible' exception."""

    if type(user_id) != int:
        raise TypeError("User ID must be of type int.")


class RoleChangeEvent:
    """This class represents any events that change the role of any user, such as a new user being assigned his or her
    first role, a user role changing for any reason, or a user being deleted. The role_prior property can be none only
    for new-user-created events, and the role_resulting can be none only for user-deleted-events.
    """
    ALL_TYPES = ('USER_CREATED', 'USER_DELETED', 'USER_ROLE_UPDATED')
    Switch_type = {
        'USER_CREATED': '',
        'USER_DELETED': '',
        'USER_ROLE_UPDATED': ''
    }
    event_id = db.Column(db.Integer, primary_key=True)
    creation_datetime = db.Column(db.datetime, defualt=datetime.utcnow())
    event_type = db.Column(db.String(17))
    user_id = db.Column(db.String(10))
    role_before = db.Column(db.String(10))
    role_after = db.Column(db.String(10))


class User:
    """Extremely simplified version of the user aggregate in the User-Account service. Only contains a few fields about
    the user's role. Due to the role-based-event event store above, this class is technically not needed. the data herein
    is stored within that store. It is just included as a sort of index, for lookup-speed.
    """
    user_id = db.Column(db.Integer, primary_key=True)
    user_role = db.Column(db.String(10))
    datetime_set = db.Column(db.datetime, defualt=datetime.utcnow())

    __init__() =


if __name__ == '__main__':
    app.run()

