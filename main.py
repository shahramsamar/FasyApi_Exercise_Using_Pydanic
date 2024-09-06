from fastapi import FastAPI, Query, status, Path, HTTPException
from typing import Optional
from fastapi.responses import JSONResponse
import random
from pydantic import BaseModel


apps = FastAPI()

class NameSchema(BaseModel):
    title : str
    description : str
    

class ResponseNameSchema(BaseModel):
    id : int
    title : str
    description : str
    is_published : bool

class UpdateSchema(BaseModel):
    id : int
    title : str
    description : str
    is_published : bool
    
    
post_list = [
    {
        "id": 1,
        "title": "post1",
        "description": "post1 description",
        "is_published": False,
    },
    {
        "id": 2,
        "title": "post2",
        "description": "post2 description",
        "is_published": True,
    },
    {
        "id": 3,
        "title": "post3",
        "description": "post3 description",
        "is_published": False,
    }
]



@apps.get('/posts')
async def show_post():
    return JSONResponse(post_list)


@apps.post('/posts',
           response_model=ResponseNameSchema,
           status_code=status.HTTP_201_CREATED,
           description='create post')
async def post_create(request:NameSchema ):
       if request.title and request.description: 
            post = {
                    "id" : random.randint(4,10),
                    "title" : request.title,
                    "description" : request.description,
                    "is_published" : False
                }
            post_list.append(post)              
            return post
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                           detail="We don't create  any post")                


@apps.get("/posts/{post_id}",description='post to search',status_code=status.HTTP_200_OK)
async def search_post(post_id: int = Path):
    for post in post_list:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"We don't have any id={id}")                
    
        
@apps.put("/posts/{post_id}", 
          status_code=status.HTTP_200_OK, 
          description="post update") 
async def post_update(request:UpdateSchema):
    for item in post_list:
        if item["id"] == request.id:
            item["title"] = request.title
            item["description"] = request.description
            item["is_published"] = request.is_published
        return item    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Post not found")   


@apps.delete("/posts/{post_id}",
             status_code=status.HTTP_200_OK,
             description="Post removed successfully")
async def post_delete(post_id: int = Path):
    for index, item in enumerate(post_list):
        if item["id"] == post_id:
            del post_list[index]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Post not found')