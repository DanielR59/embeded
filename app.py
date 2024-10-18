from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from controller.user import User
from lib.check_password import check_user
from lib.generate_jwt import encode_user_data_to_jwt
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
dashboard_url = os.getenv("DASHBOARD_URL")

template = Jinja2Templates(directory="./templates")
current_file = Path(__file__)
current_file_dir = current_file.parent
app = FastAPI()
app.mount("/templates/static", StaticFiles(directory=f"{current_file_dir}/templates/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root(req : Request):
    return template.TemplateResponse("index.html", {"request": req}) 

@app.post("/", response_class=HTMLResponse)
def root(req : Request):
    return template.TemplateResponse("index.html", {"request": req}) 

@app.get("/signup", response_class=HTMLResponse)
def signup(req : Request):
    return template.TemplateResponse("signup.html", {"request": req})

@app.get("/user", response_class=HTMLResponse)
def user(req : Request):
    return RedirectResponse("/")

@app.post("/user", response_class=HTMLResponse)
def user(req : Request,username : str = Form(), password_user: str = Form()):
    verify = check_user(username,password_user)

    if not verify:
        return RedirectResponse("/")
    
    token = encode_user_data_to_jwt(verify)
    return template.TemplateResponse("user.html", {"request": req, "data_user": verify, "token" : token,"dashboard_url": dashboard_url})

@app.post("/data-processing")
def data_processing(firstname : str = Form(), lastname : str = Form(), email : str = Form(), password_user : str = Form()
):
    data_user = {
    "firstname": firstname, 
    "lastname": lastname, 
    "email": email,
    "passworduser": password_user}
    db = User(data_user=data_user)
    db.create_user()
    
    return RedirectResponse(url="/", status_code=303)
