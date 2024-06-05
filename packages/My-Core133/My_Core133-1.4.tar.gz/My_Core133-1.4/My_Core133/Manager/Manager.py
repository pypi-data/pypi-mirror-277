from MessageManager import MessageManager
from QueryManager import QueryManager
from UserManager import UserManager
from GroupManager import GroupManager

class Manager:
    def __init__(self, db):
        self.message_manager = MessageManager(db)
        self.quary_manager = QueryManager(db)
        self.user_manager = UserManager(db)
        self.group_manager = GroupManager(db)