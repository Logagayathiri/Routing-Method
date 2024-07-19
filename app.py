# #IMport Flask for this project
# from flask import Flask

# #constructor
# app = Flask(__name__)

# #routing
# @app.route('/')

# #methods
# def hello_world():
#     return "Hello World!!!"
# #Routing2,#Method2
# @app.route('/helllo')
# def hello():
#     return "Hello Welcome to the Training!!!"


# #Routing3,Method3with value
# @app.route('/login/<username>')
# def login(username):
#     return f'The Username is {username}'
# #Routing4,Method 4 with values ID
# @app.route('/login/<int:id>')
# def login_id(id):
#     return f'this is the User id {id}'

# #Run
# if __name__=='__main__':
#     app.run(debug=True)


from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
@app.route('/login')
def login():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)













    