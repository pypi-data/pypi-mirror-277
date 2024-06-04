def parameterize(data) -> str:
    return ', '.join([f"{name}='{val}'" for name, val in data])
    
def query(table_name, option, data, order_by=False, limit=False):
    # *args: table_name, option
    # **kwargs: 'select': selectors_tuple, 'delete': ((where_names, serialized_data)) tuple of these, 'mod': {'set': ((set_names, serialized_data)), 'where': ((where_names, serialized_data))}         
    ### LATER: Make the instance the first and only arg
    match option:
        case 'select':
            statement = 'SELECT %s from %s' % (', '.join(data), table_name)
            
            if order_by:
                statement += f" ORDER BY " + ", ".join([f'{name} {direction}' for name, direction in order_by])
            if limit:
                statement += f' LIMIT {limit}'
                
            return statement + ';'
        case 'delete':
            return 'DELETE FROM %s WHERE %s;' % (table_name, parameterize(data))
        case _:
            return 'UPDATE %s SET %s WHERE %s;' % (table_name, parameterize(data[0]), parameterize(data[1]))
                

if __name__ == "__main__":
    print(query('rss', 'select', ('*')))
    print(query('rss', 'select', ('article', 'tags')))
    print(query('rss', 'select', ('article', 'tags'), order_by=(('tags', 'ASC'), ('article', 'DESC')), limit=10))
    
    print(query('rss', 'delete', (('name', 'db'), ('feed', 'realpython.com'))))
    
    print(query('rss', 'mod', ( (('name', 'db_1'), ('timestamp', '10020')), (('id', '10'),) )))
