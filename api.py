from server import Server
from fastapi import FastAPI,Body,Depends,HTTPException,status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated

app=FastAPI()
security = HTTPBasic()

server=Server()
server.connect_to_server()

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "john"
    correct_password = "test123"
 
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
 
    return "authentic"

# ------------API ROUTES FOR HANDLING TASKS----------

@app.post("/addTask")
def root(task=Body()):
   res=server.addTask(task)
   return res

@app.get("/getAllTasks")
def root(credentials: Annotated[HTTPBasicCredentials, Depends(authenticate_user)]):
    res=server.getAllTasks()
    return res
    
@app.get("/getTask")
def root(task_id:int):
    res=server.getTaskByID(task_id)
    return res
   
@app.put("/updateTask")
def root(task_id:int,updated_task=Body()):
   res=server.updateTaskByID(task_id,updated_task)
   return res
   
@app.delete("/deleteTask")
def root(task_id:int):
   res=server.deleteTaskByID(task_id)
   return res

# ---------------API ROUTES FOR HANDLING USERS---------------

@app.post("/addUser")
def root(user=Body()):
   res=server.addUser(user)
   return res
   
@app.get("/getUser")
def root(user_id:int):
    res=server.getUserByID(user_id)
    return res
    
@app.get("/getAllUsers")
def root():
    res=server.getAllUsers()
    return res
    
@app.put("/updateUser")
def root(user_id:int,updated_user=Body()):
   res=server.updateUserByID(user_id,updated_user)
   return res
    
# API ROUTE TO FIND ALL TASKS OF A PARTICULAR USER
@app.get("/getAllTasksByUser")
def root(user_id:int):
    res=server.getAllTasksByUserID(user_id)
    return res

# TERMINATING CONNECTION ON SHUTDOWN
@app.on_event("shutdown")
def close_connection():
   server.cursor.close()
   print("connection closed")