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

POSTGRES_USER=postgres
POSTGRES_PASSWORD=password123!
POSTGRES_PORT=5432
CLIENT_ID=client_id
SECRET_ID=secret_id
SECRET_VALUE=secret
DASHBOARD_URL=https://prod-useast-c.online.tableau.com/t/sitio/views/Dashboard/Overview%
```


```
uvicorn app:app --reload
```
