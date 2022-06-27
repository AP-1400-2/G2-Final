import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.IUserPaymentRepository import IUserPaymentRepository

class UserPaymentRepository(IUserPaymentRepository):
    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        pass
    
    def GetByID(self,id):
        return self.db.getData(f"SELECT * FROM usersPayment WHERE id = {id}")
    
    def GetByUserID(self,userID):
        return self.db.getData(f"SELECT * FROM usersPayment WHERE userID = {userID}")
    
    def Create(self,userPayment):
        self.db.runQuery("INSERT INTO usersPayment VALUES (NULL, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?);", userPayment.values())
        
    def Update(self,userPayment,id):
        pass
    
    def Delete(self,id):
        pass
    
    def Save(self):
        return self.db.commit()