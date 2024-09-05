import Database as db
from Channel import Channel
from Tag import Tag
from JobVacancy import JobVacancy
import hashlib

class User:
    def __init__(self, first_name=None, last_name=None, email=None, password=None, username=None):
        self._id = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self._password = None
        self.username = username
        self.created_at = None
        self.updated_at = None

        self.set_password(password)


    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def _get_password(self):
        return self._password
    
    def set_password(self, password, encr=False):
        if encr:
            self._password=password
        else:
            self._password=hashlib.sha256(password.encode()).hexdigest()


    def get_user(self):
        if not self.created_at:
            if self.get_id():
                selected_user = db.select_user(id=self.get_id())
            else:
                selected_user =  db.select_user(email=self.email, username=self.username, password=self._get_password())
            
            self.set_id(selected_user[0])
            self.first_name=selected_user[1]
            self.last_name=selected_user[2]
            self.email=selected_user[3]
            self.set_password(selected_user[4], True)
            self.username=selected_user[5]
            self.updated_at=selected_user[6]
            self.created_at=selected_user[7]

        return self

    def insert_new_user(self):

        db.insert_user(
            first_name=self.first_name
            , last_name=self.last_name
            , email=self.email
            , password=self._get_password()
            , username=self.username
        )

    def update_user(self):

        db.update_user(
            id=self.get_id()
            , first_name=self.first_name
            , last_name=self.last_name
            , email=self.email
            , password=self._get_password()
            , username=self.username
        )
        

    def get_channels(self):
        channels_list = []
        selected_channels =  db.select_channels(user_id=self.get_id())
    
        for channel in selected_channels:
            temp_channel = Channel(channel[3])

            temp_channel.set_id(channel[0])
            temp_channel.set_user_id(channel[1])
            temp_channel.set_chat_identifier(channel[2])
            temp_channel.updated_at = channel[4]
            temp_channel.created_at = channel[5]
            temp_channel.deleted_at = channel[6]

            channels_list.append(temp_channel)

        return channels_list

    def delete_channels(self):
        db.delete_channels(user_id=self.get_id())


    def get_tags(self):
        tags_list = []
        selected_tags =  db.select_tags(user_id=self.get_id())
    
        for tag in selected_tags:
            temp_tag = Tag(tag[3])

            temp_tag.set_id(tag[0])
            temp_tag.set_user_id(tag[1])
            temp_tag.updated_at = tag[4]
            temp_tag.created_at = tag[5]
            temp_tag.deleted_at = tag[6]

            tags_list.append(temp_tag)

        return tags_list

    def delete_tags(self):
        db.delete_tags(user_id=self.get_id())


    def get_vacancies(self):
        vacancies_list = []
        selected_vacancies =  db.select_vacancies(user_id=self.get_id())
    
        for vacancy in selected_vacancies:
            temp_vacancy = JobVacancy(
                title = vacancy[2]
                , body = vacancy[3]
                , activities = vacancy[4]
                , requirements = vacancy[5]
                , benefits = vacancy[6]
                , workplace = vacancy[7]
                , contact = vacancy[8]
                , salary = vacancy[9]
            )

            temp_vacancy.set_id(vacancy[0])
            temp_vacancy.set_channel_id(vacancy[1])
            temp_vacancy.favorited = vacancy[10]
            temp_vacancy.viewed = vacancy[11]
            temp_vacancy.created_at = vacancy[12]

            vacancies_list.append(temp_vacancy)

        return vacancies_list


# CREATE TABLE users(
# 	id SERIAL PRIMARY KEY,
# 	firstname VARCHAR(255) NOT NULL,
# 	lastname VARCHAR(255),
# 	email VARCHAR(255) NOT NULL,
# 	password VARCHAR(255) NOT NULL,
# 	username VARCHAR(255),
# 	updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
# 	created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
# );