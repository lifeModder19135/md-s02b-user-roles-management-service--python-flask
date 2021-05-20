from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY-DATABASE-URI'] = 'sqlite:///data/test.db'


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


@app.route('/getcurrentrolefor/<userid>')
def return_current_role():
    return 'Hello World!'


@app.route('/getrolehistoryfor/<userid>')
def return_previous_roles():
    return 'Hello World!'


@app.route('/getallpossibleroles')
def return_all_roles():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


class role_change_event:
    """This class represents any events that change the role of any user, such as a new user being assigned his or her
    first role, a user role changing for any reason, or a user being deleted. The role_prior property can be none only
    for new-user-created events, and the role_resulting can be none only for user-deleted-events. """


