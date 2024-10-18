# Tableau embeded connected app

Simple app for show Tableau embeded as connected app using JWT

## Requirements

```
pip install -r requirements.txt
```

## How to run

 - Install python requirements
 - Create postgres database and add database, schema and table shown in [this file](./database_scripts/create_db.sql)
 - Set the connected app into your Tableau Server/Cloud environment and get the following into a __.env__ file

 
```env 

POSTGRES_USER=user
POSTGRES_PASSWORD=passw
POSTGRES_PORT=5432
CLIENT_ID=client_id
SECRET_ID=secret_id
SECRET_VALUE=secret
```


```
uvicorn app:app --reload
```