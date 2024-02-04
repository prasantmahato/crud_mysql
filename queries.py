'''
Helper class to store queries to that can be executed
'''
class Queries:
    drop = "DROP TABLE IF EXISTS register"
    
    create = "CREATE TABLE register ( \
        ID INT PRIMARY KEY AUTO_INCREMENT, \
        Name VARCHAR(255) NOT NULL, \
        Email VARCHAR(255) NOT NULL, \
        dob DATE \
    );"
    
    insert = "INSERT INTO register(name, email, dob) VALUES(%s, %s, %s)"
    
    update = "UPDATE register SET name=%s WHERE email=%s"
    
    delete = "DELETE FROM register WHERE email=%s"
    
    select = "SELECT * FROM register"