from flask import Flask, request



my_app = Flask(__name__)

@my_app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def home():

    match request.method:
        case 'GET':
            return "Hello, GET!"
        case 'PUT':
            return "Hello, PUT!"
        case 'DELETE':
            return "Hello, DELETE!"
    return "Hello, Flask!"

@my_app.route('/about')
def about():
    return "About Page"

# @my_app.route('/hello/<name>/<int:age>/<int:year>')
# def hello(name, age, year): 
#     return f"Hello, {name}! You are {age} years old and the year is {year}."

@my_app.route('/hello/<name>')
@my_app.route('/hello/<name>/<int:age>')
@my_app.route('/hello/<name>/<int:age>/<int:year>')
def hello(name, age=15, year=2023): 
    return f"Hello, {name}! You are {age} years old and the year is {year}."

if __name__ == '__main__':
    my_app.run(debug=True, port=5000)  # Default port is 5000
    # my_app.run(debug=True, port=80)
    # my_app.run(debug=True, port=5001, host='0.0.0.0')  # Accessible externally on port 5001