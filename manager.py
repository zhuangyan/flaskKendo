from app import create_app,mongo
from flask_script import Manager,prompt, prompt_pass, Shell, Server
import sys
from com.utils import encrypt_password



application = create_app()
manager = Manager(application)

@manager.command
def createsuperuser():
    """
    Create a super user of the system, requiring Email and password.
    """

    db = mongo.db
    username = prompt('username')

    if len(username)<2:
        sys.exit('\nUserName must be at least two characters long')

    user = db.user.find_one({username:username})
    if  user:
        sys.exit('\nUserName already exists. Please select another one.')


    password = prompt_pass('User password')
    if len(password)<6 or len(password)>20:
        sys.exit('\nPassword length must be between 6 and 20.')
    password_confirm = prompt_pass('Confirmed password')

    if not password == password_confirm:
        sys.exit('\nCould not create user: Passwords did not match')

    db.user.insert_one({
        "username":username,
        "is_admin":1,
        "password":encrypt_password(password)
    })





manager.add_command("runserver", Server())

if __name__ == '__main__':
    manager.run()
