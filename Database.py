from Connection import Connection
from datetime import datetime
import pytz

timezone = pytz.timezone('America/Sao_Paulo')

conn = Connection()


def select_user(id=-1, email=None, username=None, password=None):
    query = f'''SELECT * FROM users WHERE ((id={id}) OR ((password='{password}') AND (email='{email}' OR username='{username}')))'''
    cursor = conn.get_cursor()

    cursor.execute(query)
    selected_user = cursor.fetchall()[0]

    return selected_user

def insert_user(first_name, last_name, email, password, username):
    query = '''INSERT INTO users 
        (first_name, last_name, email, password, username)
        VALUES (%s, %s, %s, %s, %s);
    '''
    
    new_user = (first_name, last_name, email, password, username)
    
    cursor = conn.get_cursor()

    cursor.execute(query,new_user)
    conn.force_commit()

def update_user(id, first_name, last_name, email, password, username):
    query = f''' UPDATE users
        SET first_name='{first_name}', last_name='{last_name}', email='{email}', password='{password}', username='{username}'
        WHERE id={id};
    '''

    cursor = conn.get_cursor()

    cursor.execute(query)
    conn.force_commit()



def select_channels(id=-1, user_id=-1):
    query = f'''SELECT * FROM channels WHERE id={id} OR user_id={user_id}'''
    cursor = conn.get_cursor()

    cursor.execute(query)
    selected_channels = cursor.fetchall()

    return selected_channels

def insert_channel(user_id, chat_identifier, channel_name):
    query = f'''INSERT INTO channels(
        user_id, chat_identifier, channel_name)
        VALUES ({user_id}, '{chat_identifier}', '{channel_name}');
    '''
    
    cursor = conn.get_cursor()

    cursor.execute(query)
    conn.force_commit()

def update_channel(id, channel_name, soft_delete=False):
    if soft_delete:
        deleted_at = datetime.now(timezone)
        query = f''' UPDATE channels
            SET channel_name='{channel_name}', deleted_at='{deleted_at}'
            WHERE id={id};
        '''
    else:
        query = f''' UPDATE channels
            SET channel_name='{channel_name}'
            WHERE id={id};
        '''

    cursor = conn.get_cursor()

    cursor.execute(query)
    conn.force_commit()

def delete_channels(id=-1, user_id=-1):
    query = f''' DELETE FROM channels
	    WHERE id={id} OR user_id={user_id};
    '''

    cursor = conn.get_cursor()

    cursor.execute(query)
    conn.force_commit()



def select_tags(id=-1, user_id=-1):
    query = f'''SELECT * FROM tags WHERE id={id} OR user_id={user_id}'''
    cursor = conn.get_cursor()

    cursor.execute(query)
    selected_tags = cursor.fetchall()

    return selected_tags

def insert_tag(user_id, tag_name):
    query = f'''INSERT INTO tags(
        user_id, tag_name)
        VALUES ({user_id}, '{tag_name}');
    '''
    
    cursor = conn.get_cursor()

    cursor.execute(query)
    conn.force_commit()

def update_tag(id, tag_name, soft_delete=False):
    if soft_delete:
        deleted_at = datetime.now(timezone)
        query = f''' UPDATE tags
            SET tag_name='{tag_name}', deleted_at='{deleted_at}'
            WHERE id={id};
        '''
    else:
        query = f''' UPDATE tags
            SET tag_name='{tag_name}'
            WHERE id={id};
        '''

    cursor = conn.get_cursor()

    cursor.execute(query)
    conn.force_commit()

def delete_tags(id=-1, user_id=-1):
    query = f''' DELETE FROM tags
	    WHERE id={id} OR user_id={user_id};
    '''

    cursor = conn.get_cursor()

    cursor.execute(query)
    conn.force_commit()



def select_vacancies(id=-1, channel_id=-1, user_id=-1):
    channel_ids_list = [channel_id]

    if user_id>0:
        selected_channels = select_channels(user_id=user_id)
        
        for channel in selected_channels:
            channel_ids_list.append(channel[0]) 

       
    query = f'''SELECT * FROM jobvacancies WHERE id={id} OR channel_id IN {channel_ids_list}'''
    cursor = conn.get_cursor()

    cursor.execute(query)
    selected_vacancies = cursor.fetchall()

    return selected_vacancies

def insert_vacancy(channel_id, title, body, activities, requirements, benefits, workplace, contact, salary):
    query = f'''INSERT INTO jobvacancies(
        channel_id, title, body, activities, requirements, benefits, workplace, contact, salary)
        VALUES ({channel_id}, '{title}', '{body}', '{activities}', '{requirements}', '{benefits}', '{workplace}', '{contact}', '{salary}');
    '''
    
    cursor = conn.get_cursor()

    cursor.execute(query)
    conn.force_commit()

def update_vacancy(id, favorited, viewed):
    query = f''' UPDATE jobvacancies
        SET favorited='{favorited}', viewed='{viewed}'
        WHERE id={id};
    '''

    cursor = conn.get_cursor()

    cursor.execute(query)
    conn.force_commit()

