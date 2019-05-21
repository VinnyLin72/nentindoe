from util import database as db

db.init()
# print(db.registerUser("a","a"))
# print(db.verifyUser("a","b"))
# print(db.verifyUser("a","a"))

# print(db.saveImage("a","pic1","cap1",False))
print(db.saveImage("b","pic1","cap1",False))

print(db.getPictures("b"))
print("_________________________")
print(db.getImageId("b", "pic1"))
