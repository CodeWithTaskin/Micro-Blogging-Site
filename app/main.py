from src import *

@app.route('/')
@app.route('/home')
def home():
    return make_response({'message' : 'Successfully Run'}, 200)

@app.route('/new-content')
def new_content():
    return make_response({'message' : 'Successfully Created'}, 200)

@app.route('/edit-content')
def edit_content():
    return make_response({'message' : 'Successfully Edited'}, 200)

@app.route('/delete-content')
def delete_content():
    return make_response({'message' : 'Successfully Edited'}, 200)

@app.route('/profile/update')
def profile_update():
    return make_response({'message' : 'Successfully Edited'}, 200)

