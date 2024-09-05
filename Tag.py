import Database as db

class Tag:
    def __init__(self, tag_name):
        self._id = None
        self._user_id = None
        self.tag_name = tag_name
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


    def get_tag(self):

        if not self.created_at:
            selected_tag = db.select_tags(id=self.get_id())[0]

            self.set_id(selected_tag[0])
            self.set_user_id(selected_tag[1])
            self.tag_name = selected_tag[3]
            self.updated_at = selected_tag[4]
            self.created_at = selected_tag[5]
            self.deleted_at = selected_tag[6]

        return self

    def insert_new_tag(self):

        db.insert_tag(
            user_id=self.get_user_id()
            , tag_name=self.tag_name
        )
            
    def update_tag(self, soft_delete=False):

        db.update_tag(
            id=self.get_id()
            , tag_name=self.tag_name
            , soft_delete=soft_delete
        )

    def delete_tag(self):
        db.delete_tags(id=self.get_id())


# CREATE TABLE tags(
# 	id SERIAL PRIMARY KEY,
# 	user_id INT,
# 	tag_name VARCHAR(255) NOT NULL,
# 	updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
#  	created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
#  	deleted_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
# 	CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id)
# );