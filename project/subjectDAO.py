import mysql.connector
class SubjectDAO:

    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="datarepresentation"
        )
        
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into subject (subject, term, lecturer, credits) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from subject"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from subject where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update subject set subject= %s, term=%s, lecturer=%s, credits=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from subject where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")
        
    def convertToDictionary(self, result):
        colnames=['id','subject','term','lecturer','credits']
        item = {}

        if result:

            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return(item)

subjectDAO = SubjectDAO()