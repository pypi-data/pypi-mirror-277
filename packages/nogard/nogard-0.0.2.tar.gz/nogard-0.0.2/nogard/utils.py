# from database_utils import Database # Get this from the database-utils module
# for now
class Database:
    pass
    
from coders_utils import get_timestamp, get_bare_type ## IMPORTANT... need to update the coders-utils package

import datetime
import re
import tomli

base_types = ('str', 'int', 'float', 'bytes', 'bool')

def modifications(instance):
    annotations = []
    
    for var, _type in instance.__annotations__.items():
        # print(var, _type, getattr(instance, var))
        _t = get_bare_type(_type)

        if _t and not re.search('__main__.*', str(_t)):
            annotations.append([var, _t])
        else:
            base = getattr(instance, var)
            # Only one-layer of indirect for now
            # Remember tuples can have multiple type parameters
            ## Important to note it doesn't support unions
            if (res := get_bare_type(type(base))) not in base_types and base:
                #print(res, base)
                match res:
                    case 'tuple':
                        types = []
                        
                        for item in base:
                            types.append(get_bare_type(type(item)))
                        #print(f'{var} is of type {res} {types}')
                        
                        annotations.append([var, f'tuple[{",".join(types)}]'])
                    case re.search('__main__.*', str(res)):
                        raise Exception(f'Cant deal with user-defined objects yet: {res}')
                    case _:
                        #print(f'{var} is of type {res} {type(base[0])}')#, var.__type_params__) 
                        annotations.append([var, f'{type(base)}[{type(base[0])}]'])
            elif var != 'decoded':
                annotations.append([var, res if res != 'NoneType' else 'bool'])
    
    return annotations
        
def get_config_data(config_location = './config.toml'):
    with open(config_location, mode='rb') as fp:
        return tomli.load(fp)
        
# Only sqlite right now
def establish_connection():
    pass
    
def make_database_obj(config_dict):
    return Database(database_path = config_dict['url'] + config_dict['name'])
    
# Parametrize the query before submitting
def db_query(db, query: str, data = None, _return: bool = False):
    if data != None:
        res = db.execute(query, data)
    else:
        res = db.execute(query)
    
    if _return:
        return res       
        
def to_db_insert(instance, table_name: str, option: str = 'build_table'):
    annotations = instance.__repr__()
    count = 0
    length = len(annotations)
    values = []
    
    match option:
        case 'build_table':
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
            length -= 2
        case 'insert':
            query = f'INSERT OR IGNORE INTO {table_name} ('

    for var, _type in annotations:
        # print(f'{var} {_type} {getattr(instance, var)}')
        match option:
            case 'build_table':
                if var not in ('_id', 'decoded'):
                    # FIX HERE
                    match _type:
                        case 'str':
                            query += f'{var} TEXT NOT NULL'
                        case 'int':
                            query += f'{var} INTEGER'
                        case 'float':
                            query += f'{var} FLOAT'
                        case _:
                            # CODEC here much later!!!
                            query += f'{var} TEXT NOT NULL'
                            
                    if count != length:
                        query += ', '
                    else:
                        query += ', id INTEGER PRIMARY KEY, decoded TEXT NOT NULL, timestamp TIMESTAMP);'
            case 'insert':
                query += var
                values.append(getattr(instance, var))
                
                if count != length - 1:
                    query += ', '
                else:
                    query += f", decoded, timestamp) VALUES ({','.join(['?' for _ in range(len(values) + 2)])})"
                    
        count += 1
                
    values = values + [annotations]
    values.append(get_timestamp())
    
    return query, values
