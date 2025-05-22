from src import *
from src.auth.signup import SignUp

@app.route('/user/login')
def login():
    return make_response({'message':'Successfully login'})

@app.route('/user/signup', methods=['GET','POST'])
def signup():
    DATA = request.json
    user_signup = SignUp()
    return user_signup.signup(data=DATA)


if __name__ == "__main__":
    app.run(debug=True)