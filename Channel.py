import Database as db

class Channel:
    def __init__(self, name):
        self._id = None
        self._user_id = None
        self._chat_identifier = None
        self.channel_name = name
        self.created_at = None
        self.updated_at = None
        self.deleted_at = None


    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def get_user_id(self):
        return self._user_id
    
    def set_user_id(self, user_id):
        self._user_id = user_id

    def get_chat_identifier(self):
        return self._chat_identifier
    
    def set_chat_identifier(self, chat_identifier):
        self._chat_identifier = chat_identifier

    
    def get_channel(self):

        if not self.created_at:
            selected_channel = db.select_channels(id=self.get_id())[0]

            self.set_id(selected_channel[0])
            self.set_user_id(selected_channel[1])
            self.set_chat_identifier(selected_channel[2])
            self.channel_name = selected_channel[3]
            self.updated_at = selected_channel[4]
            self.created_at = selected_channel[5]
            self.deleted_at = selected_channel[6]

        return self

    def insert_new_channel(self):

        db.insert_channel(
            user_id=self.get_user_id()
            , chat_identifier=self.get_chat_identifier()
            , channel_name=self.channel_name
        )
            
    def update_channel(self, soft_delete=False):

        db.update_channel(
            id=self.get_id()
            , channel_name=self.channel_name
            , soft_delete=soft_delete
        )

    def delete_channel(self):
        db.delete_channels(id=self.get_id())

# CREATE TABLE channels(
# 	id SERIAL PRIMARY KEY,
# 	user_id INT,
# 	chat_identifier VARCHAR(255) NOT NULL,
# 	channel_name VARCHAR(255) NOT NULL,
# 	updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
# 	created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
# 	deleted_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
# 	CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id)
# );