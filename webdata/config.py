
class Config():
    def __init__(self):
        self.DB_PLATFORM = 'mysql+pymysql'
        self.DB_HOST = 'localhost'
        self.DB_USERNAME = 'root'
        self.DB_PASSWORD = ''
        self.DB_PORT = '3306'
        self.DB_NAME = 'geckoair'
        
        self.DB_URL = f'{self.DB_PLATFORM}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        self.SECRET_KEY = 'This is a secret key'
        # mysql://root:root@localhost:3306/geckoair 
        # select * from users