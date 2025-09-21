# app/api.py

from fastapi import FastAPI, Body, Depends

from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import sign_jwt
from app.model import PostSchema, UserSchema, UserLoginSchema


app = FastAPI()

posts = [
    {
        'id': 1,
        'title': 'Pancake',
        'content':'lorem ipsum ...'
    }
]

users = []

@app.get('/', tags=['root'])
def read_root() -> dict:
    return {'message': 'welcome to the best blog of the year'}


@app.get('/posts', tags =['posts'])
async def get_posts() -> dict:
    return {'data': posts}


@app.get('/posts/{id}', tags=['posts'])
async def get_post(id: int) -> dict:
    if id > len(posts):
        return {
            'error':'No such post with the supplied id'
        }

    for post in posts:
        if post['id'] == id:
            return {
                'data':post
            }


@app.post('/posts', dependencies=[Depends(JWTBearer())], tags=['posts'])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts)+1
    posts.append(post.dict())

    return {
        'message': 'post added'
    }


@app.post('/users/signup', tags=['user'])
async def create_user(user: UserSchema = Body(...)):
    # replace with DB call in production and hash the password before saving
    users.append(user) 
    return sign_jwt(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
            
    # no matching user found    
    return False

@app.post('/user/login', tags=['user'])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return sign_jwt(user.email)
    else:
        return {
            'error':'Wrong login details'
        }