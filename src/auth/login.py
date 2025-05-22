from src.exception import MyException
from src.constants import *
from src.configuration.db_config import create_app
from src import *
import sys
from sqlalchemy import and_
db, Users = create_app(app)

class UserAuthentication:
    def finding_user_into_database(self, data : json) -> bool:
        try: 
            self.username = data['email']
            self.finding_user = Users.query.filter(Users.email == self.username).all()
            
            if len(self.finding_user) > 0:
                return True
            else:
                return False
            
        except Exception as e:
            raise MyException(e, sys) from e
    
    def login_data_verify(self, data : json) -> bool:
        try:
            self.username = data['email']
            self.password = data['password']
            self.data_verify = Users.query.filter(
                                    and_(
                                        Users.email == self.username,
                                        Users.password == self.password
                                    )
                                ).all()
            if len(self.data_verify) > 0:
                return True
            else:
                return False
        
        except Exception as e:
            raise MyException(e, sys) from e
    
class Login:
    def login(self, data):
        try:
            user_auth : UserAuthentication = UserAuthentication()
            
            if user_auth.finding_user_into_database(data=data) == False:
                return make_response({'message':'User not found'})
            else:
                if user_auth.login_data_verify(data=data) == False:
                    return make_response({'message':'Invalid username or password'})
                else:
                    return make_response({'message':'Successfully login'})
        
        except Exception as e:
            raise MyException(e, sys) from e
