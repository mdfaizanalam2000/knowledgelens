from server import connect_to_server
from fastapi import FastAPI,Body

app=FastAPI()

cursor=connect_to_server()

@app.post("/addTask")
def addTask(task=Body()):
   try:
    query=f"insert into task_manager values({task['task_id']},{task['user_id']},'{task['title']}','{task['description']}','{task['due_date']}','{task['status']}');"

    print(query)
    cursor.execute(query).commit()
    return {"message":"success, task created!"}
   except Exception as e:
       return {"message":str(e)}

@app.get("/getAllTasks")
def getAllTasks():
    try:
        query="select * from task_manager;"
        tasks=cursor.execute(query).fetchall()
        cname= [column[0] for column in cursor.description]
        result=[dict(zip(cname,result)) for result in tasks]
        return result
    except Exception as e:
       return {"message":str(e)}
    
@app.get("/getTask")
def getTask(task_id:int):
    try:
        query=f"select * from task_manager where task_id={task_id};"
        data=cursor.execute(query).fetchone()
        cname= [column[0] for column in cursor.description]
        result=[dict(zip(cname,data))]
        return result
    except Exception as e:
       return {"message":str(e)}
   
@app.put("/updateTask")
def updateTask(task_id:int,updated_task=Body()):
   try:          
    query=f"update task_manager set title='{updated_task['title']}',description='{updated_task['description']}',due_date='{updated_task['due_date']}',status='{updated_task['status']}' where task_id={task_id};"

    cursor.execute(query).commit()
    return {"message":"success, task updated!"}
   except Exception as e:
       return {"message":str(e)}
   
@app.delete("/deleteTask")
def deleteTask(task_id:int):
   try:
    query=f"delete from task_manager where task_id={task_id};"
    cursor.execute(query).commit()
    return {"message":"task deleted successfully!"}
   except Exception as e:
       return {"message":str(e)}

# ---------------USER API ROUTES---------------

@app.post("/addUser")
def addUser(user=Body()):
   try:
    query=f"insert into user_data values({user['user_id']},'{user['name']}','{user['designation']}');"

    cursor.execute(query).commit()
    return {"message":"success, user created!"}
   except Exception as e:
       return {"message":str(e)}
   
@app.get("/getUser")
def getUser(user_id:int):
    try:
        query=f"select * from user_data where user_id={user_id};"
        data=cursor.execute(query).fetchone()
        cname= [column[0] for column in cursor.description]
        result=[dict(zip(cname,data))]
        return result
    except Exception as e:
       return {"message":str(e)}
    
@app.get("/getAllUsers")
def getAllUsers():
    try:
        query="select * from user_data;"
        users=cursor.execute(query).fetchall()
        cname= [column[0] for column in cursor.description]
        result=[dict(zip(cname,result)) for result in users]
        return result
    except Exception as e:
       return {"message":str(e)}
    
@app.put("/updateUser")
def updateUser(user_id:int,updated_user=Body()):
   try:          
    query=f"update user_data set name='{updated_user['name']}',designation='{updated_user['designation']}' where user_id={user_id};"

    cursor.execute(query).commit()
    return {"message":"success, user updated!"}
   except Exception as e:
       return {"message":str(e)}
    
# API ROUTE TO FIND ALL TASKS OF A PARTICULAR USER
@app.get("/getAllTasksByUser")
def getAllTasksByUser(user_id:int):
    try:
        query=f"select * from task_manager t join user_data u on t.user_id=u.user_id where t.user_id={user_id};"
        
        tasks=cursor.execute(query).fetchall()
        cname= [column[0] for column in cursor.description]
        result=[dict(zip(cname,result)) for result in tasks]
        return {"tasks":result}
    except Exception as e:
       return {"message":str(e)}

@app.on_event("shutdown")
def close_connection():
   cursor.close()
   print("connection closed")