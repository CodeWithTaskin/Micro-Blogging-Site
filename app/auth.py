from src import *
from src.auth.signup import SignUp
from src.auth.login import Login

@app.route('/user/login', methods=['GET','POST'])
def login():
    DATA = request.json
    user_login = Login()
    return user_login.login(data=DATA)

@app.route('/user/signup', methods=['GET','POST'])
def signup():
    DATA = request.json
    user_signup = SignUp()
    return user_signup.signup(data=DATA)


if __name__ == "__main__":
    app.run(debug=True)