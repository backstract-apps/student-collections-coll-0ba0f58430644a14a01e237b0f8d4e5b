from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - student-collections-coll-0ba0f58430644a14a01e237b0f8d4e5b',debug=False,docs_url='/interesting-omkar-194f0f3cc6a311efad090242ac12000541/docs',openapi_url='/interesting-omkar-194f0f3cc6a311efad090242ac12000541/openapi.json')

app.include_router(router, prefix='/interesting-omkar-194f0f3cc6a311efad090242ac12000541/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()