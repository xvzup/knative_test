#FASTAPI imports
from fastapi import FastAPI, Request, File, UploadFile, Depends
from pydantic import BaseModel
import asyncio
import nats
import json
import sys

app = FastAPI()
class Options (BaseModel):
  FileName: str


#Using an asynchronous POST method for communication
@app.post("/send_notification")
async def get_data(request: Request,options: Options):
   
  #Waits for the request and converts into JSON
  result = await request.json()  
  result_encode_data = json.dumps(result, indent=2).encode('utf-8')

  # Create nats notification
  nc = await nats.connect('nats.nats.svc.cluster.local')
  js = nc.jetstream()
  await js.add_stream(name='notification', subjects=['bob'])
  ack = await js.publish('bob', result_encode_data)
  print("Notification send ", ack)
  # Close connection to nats broker
  await nc.drain()
  
  sys.exit()