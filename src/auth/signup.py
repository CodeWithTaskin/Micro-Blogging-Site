from src.constants import *
from src import *
import json
import sys
from src.exception import MyException
from src.configuration.db_config import create_app
from sqlalchemy import or_

db, Users = create_app(app)


class RegisterIntoDataBase:
    '''
    register_into_database function:-
    - register new user into the database.
    '''
    def register_into_database(self, data : json) -> None:
        try:
            self.name = data['name'] # Extracting user name from json file
            self.phone = data['phone'] # Extracting user phone from json file
            self.email = data['email'] # Extracting user email from json file
            self.password = data['password'] # Extracting password name from json file
            
            with app.app_context(): # adding new user into the database
                new_user = Users(
                    name=self.name,
                    phone=int(self.phone),
                    email=self.email, 
                    password=self.password
                )
                db.session.add(new_user)
                db.session.commit() # commiting new user into the database
                
        except Exception as e:
            raise MyException(e, sys)
            
            
class FindDuplicates:
    def duplicates(self, data : json) -> bool:
        try:
            self.name = data['name'] # Extracting user name from json file
            self.phone = data['phone'] # Extracting user phone from json file
            self.email = data['email'] # Extracting user email from json file
            self.password = data['password'] # Extracting password name from json file
            
            self.finding_user = Users.query.filter(
                                    or_(
                                        Users.email == self.email,
                                        Users.phone == self.phone
                                    )
                                ).all()
            if len(self.finding_user) > 0:
                return True
            else:
                return False
            
        except Exception as e:
            raise MyException(e, sys) from e
class SignUp:

    def signup(self, data : json) -> 201:
        try:
            find_duplicates : FindDuplicates = FindDuplicates()
            
            if find_duplicates.duplicates(data=data) == False:
                try:
                    register: RegisterIntoDataBase = RegisterIntoDataBase() # creating a obj of RegisterIntoDataBase class
                    register.register_into_database(data=data)
                    
                    return make_response({'message':'Successfully SignUp'}, 201)
                
                except Exception as e:
                    raise MyException(e, sys)
                
            else:
                return make_response({'message':'Duplicate email or phone'})
        
        except Exception as e:
            raise MyException(e, sys) from e