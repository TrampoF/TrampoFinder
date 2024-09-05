import Database as db

class JobVacancy:

    def __init__(self, title, body, activities, requirements, benefits, workplace, contact, salary):
        self._id = None
        self._channel_id = None
        self.title = title
        self.body = body
        self.activities = activities
        self.requirements = requirements
        self.benefits = benefits
        self.workplace = workplace
        self.contact = contact
        self.salary = salary
        self.favorited = False
        self.viewed = False
        self.created_at = None


    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def get_channel_id(self):
        return self._channel_id
    
    def set_channel_id(self, channel_id):
        self._channel_id = channel_id


    def get_vacancy(self):

        if not self.created_at:
            selected_vacancy = db.select_vacancies(id=self.get_id())[0]

            self.set_id(selected_vacancy[0])
            self.set_channel_id(selected_vacancy[1])
            self.title = selected_vacancy[2]
            self.body = selected_vacancy[3]
            self.activities = selected_vacancy[4]
            self.requirements = selected_vacancy[5]
            self.benefits = selected_vacancy[6]
            self.workplace = selected_vacancy[7]
            self.contact = selected_vacancy[8]
            self.salary = selected_vacancy[9]
            self.favorited = selected_vacancy[10]
            self.viewed = selected_vacancy[11]
            self.created_at = selected_vacancy[12]

        return self

    def insert_new_vacancy(self):

        db.insert_vacancy(
            channel_id = self.get_channel_id()
            , title = self.title
            , body = self.body
            , activities = self.activities
            , requirements = self.requirements
            , benefits = self.benefits
            , workplace = self.workplace
            , contact = self.contact
            , salary = self.salary
        )
            
    def update_vacancy(self):

        db.update_vacancy(
            id=self.get_id()
            , favorited=self.favorited
            , viewed=self.viewed
        )



# CREATE TABLE jobvacancies(
# 	id SERIAL PRIMARY KEY,
# 	channel_id INT,
# 	title VARCHAR(255),
# 	body VARCHAR(255),
# 	activities VARCHAR(255),
# 	requirements VARCHAR(255),
# 	benefits VARCHAR(255),
# 	workplace VARCHAR(255),
# 	contact VARCHAR(255),
# 	salary VARCHAR(255),
# 	favorited BOOL,
# 	viewed BOOL,
# 	created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
# 	CONSTRAINT fk_channel_id FOREIGN KEY (channel_id) REFERENCES channels(id)
# );
