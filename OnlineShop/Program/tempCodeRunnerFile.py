import sys,os
sys.path.append('../onlineShop')
from DataLayer.Context.UnitOfWork import context

db = context()


print(db.userRepository.GetUserNameByID(20))

