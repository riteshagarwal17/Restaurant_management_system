import pymysql

class Connection:
    __con = None
    def __init__(self):
        self.errormessage = ""
        if Connection.__con is None:
            Connection.__con = pymysql.connect("localhost","root","mrtsdr06","restaurant")

    def closeConnection(self):
        if Connection.__con is not None:
            Connection.__con.close()
        Connection.__con = None

    def getErrorMessage(self):
        return self.errormessage

    def insertQuery(self,query):
        try:
            if Connection.__con is not None:
                cursor = Connection.__con.cursor()
                cursor.execute(query)
                Connection.__con.commit()
                return True
            else:
                self.errormessage = " Connection Failure "
                return False
        except BaseException as ex:
            self.errormessage = ex.args[1]
            return False

    def createInsertQuery(self,table_name,column_values):
        query = "insert into " + table_name + "(";
        count = 0
        for key in column_values:
            count += 1
            query += key
            if len(column_values) != count:
                query += ","
        query += ") values("
        count = 0
        for key in column_values:
            count += 1
            value = column_values[key]
            if isinstance(value,int) or isinstance(value,float):
                query += str(value)
            else:
                query += "'" + value + "'"
            if len(column_values) != count:
                query += ","
        query += ")"
        return query

    def createUpdateQuery(self,table_name,column_values,primary_values):
        query = "update " + table_name + " set ";
        count = 0
        for key in column_values:
            count += 1
            query += key + " = "
            value = column_values[key]
            if isinstance(value,int) or isinstance(value,float):
                query += str(value)
            else:
                query += "'" + value + "'"
            if len(column_values) != count:
                query += ","
        query += " where "
        count = 0
        for key in primary_values:
            count += 1
            query += key + " = "
            value = primary_values[key]
            if isinstance(value, int) or isinstance(value, float):
                query += str(value)
            else:
                query += "'" + value + "'"
            if len(primary_values) != count:
                query += " and "
        return query

    def createDeleteQuery(self,table_name,primary_values):
        query = "delete from " + table_name + " where ";
        count = 0
        for key in primary_values:
            count += 1
            query += key + " = "
            value = primary_values[key]
            if isinstance(value, int) or isinstance(value, float):
                query += str(value)
            else:
                query += "'" + value + "'"
            if len(primary_values) != count:
                query += " and "
        return query

    def executeQuery(self,query):
        records = None
        try:
            if Connection.__con is not None:
                cursor = Connection.__con.cursor()
                cursor.execute(query)
                records = cursor.fetchall()
            else:
                self.errormessage = " Connection Failure "
        except BaseException as ex:
            self.errormessage = ex.args[1]
        return records

