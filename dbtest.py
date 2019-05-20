from util import database as db

db.init()
print(db.registerUser("a","a"))
print(db.verifyUser("a","b"))
print(db.verifyUser("a","a"))

print(db.saveImage("a","pic0","cap0",False))
print(db.removeImage("a", "pic0"))

print("_________________________")
print(db.getPictures("a"))
print(db.removeImage("a", "pic0"))
