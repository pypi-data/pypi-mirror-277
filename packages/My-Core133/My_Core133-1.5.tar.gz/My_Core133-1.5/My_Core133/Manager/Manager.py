import os

from SerializerDeserializerModels.SerializerDeserializerModels import SerializerDeSerializerModels

from configs.default import ACTION, SENDER, DESTINATION, AVATARS_DIR


class GroupManager:
    def __init__(self, db):
        self.db = db


    def create_group(self, request):

        self.db.create_group(request['NAME'], request['ADMIN'])
        response = {

            ACTION: 'CREATE_GROUP',
            'CREATED': True,
            'GROUP' : request['NAME']
        }
        return response

    # request = {
    #     'TOKEN': self.token,
    #     ACTION: 'OPEN_GROUP',
    #     'USER': self.user['name'],
    #     'NAME': name
    # }

    def open_group(self, request):
        previous_messages = self.db.get_messages_in_group(request['NAME'])
        all_users = self.db.get_all_users()
        all_users_json = {user.id : user.name for user in all_users}
        messages_json = [SerializerDeSerializerModels.message_to_json(msg) for msg in previous_messages]
        for messages in messages_json:
            messages['FROM'] = all_users_json[messages['FROM']]
        responce = {
            ACTION: 'OPEN_GROUP',
            'GROUP': request['NAME'],
            'MESSAGES': messages_json,
        }

        is_owner = self.db.is_owner_in_group(request['USER'], request['NAME'])
        if is_owner:
            responce['STATUS'] = 'OWNER'
        else:
            is_admin = self.db.is_admin_in_group(request['USER'], request['NAME'])
            if is_admin:
                responce['STATUS'] = 'ADMIN'
            else:
                responce['STATUS'] = 'NOTHING'
        return responce

    # request = {
    #     'TOKEN': self.token,
    #     ACTION: 'GROUPS_BY_USER',
    #     'USER': self.user['name'],
    # }

    def groups_by_user(self, request):
        groups = self.db.get_groups_by_user(request['USER'])
        groups_json = [SerializerDeSerializerModels.group_to_json(group) for group in groups]
        responce = {
            ACTION: 'GROUPS_BY_USER',
            'GROUPS': groups_json,
        }
        return responce



    # request = {
    #     'TOKEN': self.token,
    #     ACTION: 'ADD_IN_GROUP',
    #     'USER': username,
    #     'GROUP': self.selected_group['NAME']
    # }

    # request = {
    #     ACTION: "GET_USERS_IN_GROUPS",
    #     "GROUP": self.selected_group,
    #     "USER": self.user['name'],
    #     'METHOD': method
    # }
    def add_in_group(self, request):
        self.db.add_user_in_group(username=request['USER'], groupname=request['GROUP'], is_admin=False)
        responce = {
            ACTION: 'ADD_IN_GROUP',
            'USER': request['USER'],
            'GROUP': request['GROUP'],
            'ADDED' : True
        }
        return responce

    def add_in_admin(self, request):
        self.db.add_user_in_admin(username=request['USER'], groupname=request['GROUP'])
        responce = {
            ACTION: 'ADD_IN_ADMIN',
            'USER': request['USER'],
            'GROUP': request['GROUP'],
            'ADDED' : True
        }
        return responce

    def delete_admin(self, request):
        self.db.delete_admin_from_group(username=request['USER'], groupname=request['GROUP'])
        responce = {
            ACTION: 'DELETE_ADMIN',
            'USER': request['USER'],
            'GROUP': request['GROUP'],
            'DELETED': True
        }
        return responce

    def delete_from_group(self, request):
        self.db.delete_from_group(username=request['USER'], groupname=request['GROUP'])
        responce = {
            ACTION: 'DELETE_FROM_GROUP',
            'USER': request['USER'],
            'GROUP': request['GROUP'],
            'DELETED': True
        }
        return responce

    def get_users_in_group(self, request):
        owner = self.db.get_owner(request['GROUP'])
        if request['METHOD'] == 'DELETE_ADMIN':
            users = self.db.get_user_in_group_only_admin(request['GROUP'])
            users_json = [SerializerDeSerializerModels.user_to_json(user) for user in users if user.id != owner.id]
        elif request['METHOD'] == 'ADD_IN_ADMIN':
            users = self.db.get_users_in_group_no_admin(request['GROUP'])
            users_json = [SerializerDeSerializerModels.user_to_json(user) for user in users if user.id != owner.id ]
        elif request['METHOD'] == 'DELETE_FROM_CHAT':
            users = self.db.get_users_in_group(request['GROUP'])
            users_json = [SerializerDeSerializerModels.user_to_json(user)  for user in users if user.id != owner.id and user.name != request['USER']]
        elif request['METHOD'] == 'VIEW_ALL_USERS':
            users = self.db.get_users_in_group(request['GROUP'])
            users_json = [SerializerDeSerializerModels.user_to_json(user) for user in users]  # if user.id != owner.id
        else:
            users = self.db.get_users_in_group(request['GROUP'])
            users_json = [SerializerDeSerializerModels.user_to_json(user) for user in users] # if user.id != owner.id



        responce = {
            ACTION: 'GET_USERS_IN_GROUP',
            'USERS': users_json,
            'METHOD': request['METHOD']
        }
        return responce

class UserManager:
    def __init__(self, db):
        self.db = db
    def get_friend(self, request):
        friends = self.db.get_friends(request['USER'])
        friends_json = [SerializerDeSerializerModels.user_to_json(friend) for friend in friends]
        response = {
            ACTION: 'GET_FRIEND_GROUP',
            'FRIENDS': friends_json
        }
        return response

    def get_user_by_name(self, request):
        users = self.db.find_users_by_name(request['NAME'])
        if request['METHOD'] == 'InAddGroup':
            users_in_group = self.db.get_users_in_group(request['GROUP'])
            for user in users:
                if user in users_in_group:
                    users.remove(user)
        users_json = [SerializerDeSerializerModels.user_to_json(user) for user in users if user.name != request['USERNAME']]
        response = {
            ACTION: 'GET_USER_BY_NAME',
            'USERS': users_json,
            'METHOD': request['METHOD'],
        }
        return response

    def friend_status(self, request):
        query_from = self.db.get_query(from_username=request[SENDER], to_username=request[DESTINATION])
        if query_from:
            return "SENTED_QUIRY"
        else:
            query_to = self.db.get_query(to_username=request[SENDER], from_username=request[DESTINATION])
            if query_to:
                return  "TO_HE_SENTED_QUIRY"
            else:
                friend = self.db.is_friend(username1=request[SENDER], username2=request[DESTINATION])
                if friend:
                    return "FRIEND"
                else:
                    return "NOTHING"

    def get_profile(self, request):
        groups = self.db.get_groups_by_user(username=request['USERNAME'])
        friends = self.db.get_friends(username=request['USERNAME'])
        user = self.db.get_user_by_name(username=request['USERNAME'])
        friends_json = [SerializerDeSerializerModels.user_to_json(friend) for friend in friends]
        groups_json = [SerializerDeSerializerModels.group_to_json(group) for group in groups]
        user_json = SerializerDeSerializerModels.user_to_json(user)
        image_file_name = f'{user.id}.png'
        image_path = os.path.join(AVATARS_DIR, image_file_name)
        try:
            with open(image_path, 'rb') as file:
                image_bytes = file.read()
        except:
            default_file_name = 'default.png'
            image_path = os.path.join(AVATARS_DIR, default_file_name)
            with open(image_path, 'rb') as file:
                image_bytes = file.read()
        user_json['AVATAR'] = image_bytes.decode('latin1')

        responce = {
            ACTION: 'VIEW_PROFILE',
            'FRIENDS': friends_json,
            'GROUPS': groups_json,
            'USER': user_json,
        }
        return responce
class QueryManager:
    def __init__(self, db):
        self.db =db


    def create_query(self, request):
        self.db.create_query(from_username=request['FROM_USERNAME'], to_username=request['TO_USERNAME'])
        response_from = {
            ACTION: 'CREATE_QUERY',
            'CREATED': True
        }

        response_to = {
            ACTION: 'DISPLAY_QUERY',
            'FROM_USERNAME': request['FROM_USERNAME']
        }
        return response_from,response_to

    def accept_query(self, request):
        self.db.create_friend(username1=request['FROM_USERNAME'], username2=request['TO_USERNAME'])
        self.db.delete_query(from_username=request['FROM_USERNAME'], to_username=request['TO_USERNAME'])
        response_from = {
            ACTION: 'ACCEPT_QUERY',
            'FRIEND': request['TO_USERNAME'],
        }
        response_to = {
            ACTION: 'ACCEPT_QUERY',
            'FRIEND': request['FROM_USERNAME']
        }
        return response_from, response_to

class MessageManager:
    def __init__(self, db):
        self.db = db
    def get_previous_messages(self, request):
        messages = self.db.get_messages_by_two_users(from_username=request[SENDER], to_username=request[DESTINATION])
        messages_json = [SerializerDeSerializerModels.message_to_json(msg) for msg in messages]
        response = {
            ACTION: PREVIOUS,
            SENDER: request[SENDER],
            DESTINATION: request[DESTINATION],
            'MESSAGE': messages_json
        }
        return response

    def create_message(self, request):
        msg = self.db.create_message(from_username=request[SENDER], to_username=request[DESTINATION],
                                content=request[MESSAGE_TEXT])
        msg_json = {
            SENDER: request[SENDER],
            DESTINATION: request[DESTINATION],
            MESSAGE_TEXT: request[MESSAGE_TEXT],
            "CREATE_AT": msg.created_at.strftime("%I:%M"),
            "ID": msg.id,
        }
        return msg_json

    def create_message_in_group(self, request):
        msg = self.db.create_message_in_group(from_username=request[SENDER], group=request['GROUP'],
                                content=request[MESSAGE_TEXT])
        responce = {
            ACTION: "MESSAGE_IN_GROUP",
            SENDER: request[SENDER],
            "GROUP" : request['GROUP'],
            MESSAGE_TEXT: msg.content,
            "CREATE_AT": msg.created_at.strftime("%I:%M"),
            "ID": msg.id,
        }
        users = self.db.get_users_in_group(groupname=request['GROUP'])
        return responce, users

    def delete_message(self, request):
        msg = self.db.delete_message(request["MESSAGE_ID"])
        to, group = None, None
        if msg.group:
            group = self.db.get_group_by_id(msg.group)
            users = [{'NAME': user.name} for user in self.db.get_users_in_group(group.name)]
        else:
            to = self.db.get_user_by_id(msg.to_user).name
            users = [{'NAME': to}, SerializerDeSerializerModels.user_to_json(self.db.get_user_by_id(msg.from_user))]
        responce = {
            ACTION: "DELETED_MESSAGE",
            "USERS": users,
            "DELETED": True,
            "MESSAGE_ID": msg.id,
            DESTINATION: to,
        }
        if group is None:
            responce['GROUP'] = None
        else:
            responce["GROUP"]= group.name
        return responce

    def update_message(self, request):
        to, group = None, None
        msg = self.db.update_message(request['MESSAGE_ID'], request['UPDATE_TEXT'])
        if msg.group:
            group = self.db.get_group_by_id(msg.group)
            users = [SerializerDeSerializerModels.user_to_json(user) for user in self.db.get_users_in_group(group.name)]
        else:
            to = self.db.get_user_by_id(msg.to_user).name
            users = [{'NAME': to}, SerializerDeSerializerModels.user_to_json(self.db.get_user_by_id(msg.from_user))]

        responce = {
            ACTION: "UPDATED_MESSAGE",
            "USERS": users,
            "UPDATED": True,
            "MESSAGE_ID": msg.id,
            SENDER: self.db.get_user_by_id(msg.from_user).name,
            "UPDATE_TEXT": request['UPDATE_TEXT'],
            DESTINATION: to,
        }
        if group is None:
            responce['GROUP'] = None
        else:
            responce["GROUP"]= group.name
        return responce



    def search_message(self, request):
        if request['GROUP']:
            msgs = self.db.search_message_in_group(search_text=request['SEARCH_TEXT'], groupname= request['GROUP'])
        else:
            msgs = self.db.search_message_in_chat(search_text=request['SEARCH_TEXT'], to_name= request['TO'])
        msgs_id = [msg.id for msg in msgs]

        responce = {
            ACTION: "SEARCH_MESSAGE",
            "MESSAGES_ID": msgs_id,
        }
        return responce
class Manager:
    def __init__(self, db):
        self.message_manager = MessageManager(db)
        self.quary_manager = QueryManager(db)
        self.user_manager = UserManager(db)
        self.group_manager = GroupManager(db)