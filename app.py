from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller.user import User
from lib.check_password import check_user


template = Jinja2Templates(directory="./templates")

app = FastAPI()

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

    if verify:
        print("no mamaste")
        return template.TemplateResponse("user.html", {"request": req, "data_user": verify})
    print("mamaste")
    return RedirectResponse("/")

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
