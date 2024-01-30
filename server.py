import pyodbc

class Server:
    server = 'KLBLRLP1868\SQLEXPRESS'
    database = 'master'
    username = 'sa'
    password = 'root@123'

    # METHOD TO CONNECT TO SQL SERVER
    def connect_to_server(self):
        try:
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                                SERVER='+self.server+';\
                                DATABASE='+self.database+';\
                                UID='+self.username+';\
                                PWD='+ self.password)
            self.cursor = cnxn.cursor()
            print("Connection to database is successful!")
        except:
            print("Problem while connecting to database!")

    # METHOD TO EXECUTE QUERY
    # def execute_query(self,query):
    #     try:
    #         self.cursor.execute(query)
    #     except Exception as e:
    #         return {"message":str(e)}


    # def addTask(self,task):
    #     try:
    #         query=f"exec AddTask @task_id={task['task_id']},@user_id={task['user_id']},@title ='{task['title']}',@description ='{task['description']}',@due_date='{task['due_date']}',@status='{task['status']}'"

    #         result=self.execute_query(query)
    #         self.cursor.commit()
    #         return {"message":str(result)}
    #         # return {"message":"success, task created!"}
    #     except Exception as e:
    #         return {"message":str(e)}
        
    # METHODS TO PERFORM CRUD OPERATIONS ON TASKS
            
    def addTask(self,task):
        try:
            self.connect_to_server()
            query=f"insert into task_manager values task_id={task['task_id']},user_id={task['user_id']},title ='{task['title']}',description ='{task['description']}',due_date='{task['due_date']}',status='{task['status']}'"

            self.cursor.execute(query)
            return {"message":"success, task created!"}
        except Exception as e:
            return {"message":str(e)}
        finally:
            self.cursor.close()
            print("Connection closed securely!")
        
    def getAllTasks(self):
        try:
            self.connect_to_server()
            query="select * from task_manager"

            tasks=self.cursor.execute(query).fetchall()
            cname= [column[0] for column in self.cursor.description]
            result=[dict(zip(cname,result)) for result in tasks]
            return result
        except Exception as e:
            return {"message":str(e)}
        finally:
            self.cursor.close()
            print("Connection closed securely!")
        
    def getTaskByID(self,task_id):
        try:
            self.connect_to_server()
            query=f"select * from task_manager where task_id={task_id}"

            data=self.cursor.execute(query).fetchone()
            cname= [column[0] for column in self.cursor.description]
            result=[dict(zip(cname,data))]
            return result
        except Exception as e:
            return {"message":str(e)}
        finally:
            self.cursor.close()
            print("Connection closed securely!")
        
    def updateTaskByID(self,task_id,updated_task):
        try:     
            self.connect_to_server()     
            query=f"update task_manager set title='{updated_task['title']}',description='{updated_task['description']}',due_date='{updated_task['due_date']}',status='{updated_task['status']}' where task_id={task_id}"

            self.cursor.execute(query).commit()
            return {"message":"success, task updated!"}
        except Exception as e:
            return {"message":str(e)}
        finally:
            self.cursor.close()
            print("Connection closed securely!")
        
    def deleteTaskByID(self,task_id):
        try:
            self.connect_to_server()
            query=f"delete from task_manager where task_id={task_id}"

            self.cursor.execute(query).commit()
            return {"message":"task deleted successfully!"}
        except Exception as e:
            return {"message":str(e)}
        finally:
            self.cursor.close()
            print("Connection closed securely!")
        
    # METHODS TO PERFORM CRUD OPERATIONS ON USERS
    
    def addUser(self,user):
        try:
            self.connect_to_server()
            query=f"insert into user_data values({user['user_id']},'{user['name']}','{user['designation']}')"

            self.cursor.execute(query).commit()
            return {"message":"success, user created!"}
        except Exception as e:
            return {"message":str(e)}
        finally:
            self.cursor.close()
            print("Connection closed securely!")
        
    def getUserByID(self,user_id):
        try:
            self.connect_to_server()
            query=f"select * from user_data where user_id={user_id}"

            data=self.cursor.execute(query).fetchone()
            cname= [column[0] for column in self.cursor.description]
            result=[dict(zip(cname,data))]
            return result
        except Exception as e:
            return {"message":str(e)}
        finally:
            self.cursor.close()
            print("Connection closed securely!")
        
    def getAllUsers(self):
        try:
            self.connect_to_server()
            query="select * from user_data"

            users=self.cursor.execute(query).fetchall()
            cname= [column[0] for column in self.cursor.description]
            result=[dict(zip(cname,result)) for result in users]
            return result
        except Exception as e:
            return {"message":str(e)}
        finally:
            self.cursor.close()
            print("Connection closed securely!")
        
    def updateUserByID(self,user_id,updated_user):
        try:          
            self.connect_to_server()
            query=f"update user_data set name='{updated_user['name']}',designation='{updated_user['designation']}' where user_id={user_id}"

            self.cursor.execute(query).commit()
            return {"message":"success, user updated!"}
        except Exception as e:
            return {"message":str(e)}
        finally:
            self.cursor.close()
            print("Connection closed securely!")
        
    def getAllTasksByUserID(self,user_id):
        try:
            self.connect_to_server()
            query=f"select * from task_manager t join user_data u on t.user_id=u.user_id where t.user_id={user_id}"
            
            tasks=self.cursor.execute(query).fetchall()
            cname= [column[0] for column in self.cursor.description]
            result=[dict(zip(cname,result)) for result in tasks]
            return {"tasks":result}
        except Exception as e:
            return {"message":str(e)}
        finally:
            self.cursor.close()
            print("Connection closed securely!")