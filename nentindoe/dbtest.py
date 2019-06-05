from util import database as db

db.init()
# print(db.registerUser("a","a"))
# print(db.registerUser("b","b"))
# print(db.registerUser("c","c"))
# print(db.verifyUser("a","b"))
# print(db.verifyUser("a","a"))

# print(db.saveImage("a","pic1","cap1",False))
# print(db.saveImage("b","pic1","cap1",False))
#
# print(db.getPictures("b"))
# print("_________________________")
# print(db.getImageId("b", "pic1"))

# print(db.createGroup("a","groupa"))
# print(db.createGroup("a","groupa"))

# print(db.requestGroup("b","groupa"))
# print(db.requestGroup("c","groupa"))
#
# print(db.evalRequest("groupa", "a", "b", 1))
# print(db.evalRequest("groupa", "a", "c", 0))
#
# print(db.requestGroup("b","groupa"))
#
# print(db.requestGroup("b","groupa"))
# print(db.evalRequest("groupa", "a", "b", 1))
#
# print(db.getMembers("groupa"))
# print(db.getAdmins("groupa"))
# print(db.getBanned("groupa"))
#
# print(db.banMember("groupa", "b"))
#
# print(db.getMembers("groupa"))
# print(db.getAdmins("groupa"))
# print(db.getBanned("groupa"))
#
# print(db.unbanMember("groupa", "b"))
#
# print(db.getMembers("groupa"))
# print(db.getAdmins("groupa"))
# print(db.getBanned("groupa"))
#
# print(db.promoteMember("groupa", "b"))
#
# print(db.getMembers("groupa"))
# print(db.getAdmins("groupa"))
# print(db.getBanned("groupa"))
#
# print(db.demoteMember("groupa", "a"))
# 
# print(db.getMembers("groupa"))
# print(db.getAdmins("groupa"))
# print(db.getBanned("groupa"))

print(db.addGroupPic('a', 'pic1', "groupa"))
