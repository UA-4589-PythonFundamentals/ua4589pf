import email
from flask import Flask, request, render_template, redirect, url_for
from models import User, generate_random_users
user_app = Flask(__name__)

USER_LIST = generate_random_users(5)

@user_app.route('/')
def user_list():
    return render_template('user_list.html', users_list=USER_LIST)


@user_app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        password = request.form.get('password')
        if name and age and email and password:
            USER_LIST.append(User(name, int(age), email, password))
        return  redirect(url_for('user_list'))
    return render_template('add_user.html')



if __name__ == '__main__':
    user_app.run(debug=True, port=5000)  # Default port is 5000
    # my_app.run(debug=True, port=80)
    # my_app.run(debug=True, port=5001, host='
