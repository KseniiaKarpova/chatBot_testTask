import config
import pymysql.cursors
class DATABASE:
    def __init__(self):
        pass

    def get_connect(self):
        try:
            connection = pymysql.connect(user=config.user,
                                         password=config.password,
                                         host=config.host, db=config.database)
            return connection
        except Exception as e:
            return None


    def test_connect(self):
        #show_db_query = "SHOW DATABASES"
        #connection = self.get_connect()
        #with connection.cursor() as cursor:
        #    cursor.execute(show_db_query)
        #    for db in cursor:
        #        print(db)
        #cursor.close()
        #connection.close()
        connection = self.get_connect()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM messages;")

        rows = cursor.fetchall()

        for row in rows:
            print(row)



    def data2sqlstr(self,time):
        try:
            return time.strftime('%Y-%m-%d %H:%M:%S')
        except Exception:
            print(f'[INFO] {Exception}')


    def new_message(self,time,id_session,text,id_client):
        connection = self.get_connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO messages (`time`,`text`,`idsession`,`idclient`) VALUES (%s, %s,%s,%s)""",
                               (self.data2sqlstr(time),text,id_session,id_client))
                connection.commit()

        except Exception:
            print(f'[INFO] {self.data2sqlstr(time),text,id_session,id_client}')
        finally:
            cursor.close()
            connection.close()


    def new_session(self,session):
        connection = self.get_connect()
        try:
            with connection.cursor() as cursor:

                cursor.execute('INSERT INTO session (`idsession`, `startTime`) VALUES (%s, %s)',
                               (session.id,self.data2sqlstr(session.startTime)))

                connection.commit()

        except Exception:
            print(f'[INFO] {session.id,self.data2sqlstr(session.startTime)}')
        finally:
            cursor.close()
            connection.close()



    def end_session(self, session):
        connection = self.get_connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE session SET endTime=%s WHERE idsession=%s""",
                               (self.data2sqlstr(session.endTime),session.id))
                connection.commit()
        except Exception:
            print(f'[INFO] {self.data2sqlstr(session.endTime),session.id}')
        finally:
            cursor.close()
            connection.close()