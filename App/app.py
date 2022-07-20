#FASTAPI imports
from fastapi import FastAPI, Request, File, UploadFile, Depends
from pydantic import BaseModel
#APP defination
app = FastAPI()
#Base model
class Options (BaseModel):
  FileName: str
  FileDesc: str = 'Upload for demonstration'
  #FileType: Optional[str]


#Using an asynchronous POST method for communication
@app.post("/acceptdata")
async def get_data(request: Request,options: Options):
   
  #Waits for the request and converts into JSON
  result = await request.json()  
  
  #Prints result in cmd – verification purpose
  print(result)
  return result