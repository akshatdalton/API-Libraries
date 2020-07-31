from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from langWebframe_database import g as graph
import langWebframe_database as db

class Data(BaseModel):
    vertex : str
    key : str

app = FastAPI()

templates = Jinja2Templates(directory='intership/Capstone/ Project/templates')

@app.get('/')
async def user1(request : Request):
    return templates.TemplateResponse('home.html', {
        'request' : request,
        'db' : db
    })

def db_update(vertex, key):
    v = graph.vertex_collection(f'{vertex}')

    doc = v.get(f'{key}')
    doc['likes'] += 1

    v.update(doc)

@app.post('/update')
async def update(data : Data, background_tasks : BackgroundTasks):

    background_tasks.add_task(db_update, data.vertex, data.key)

    return {
        'msg' : 'Code Sucess'
    }

@app.get("/{lan}")
async def read_item(lan, request : Request):

    db.get_db(lan)

    return templates.TemplateResponse('ind3.html', {
        'request' : request,
        'db' : db
    })

