from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from task import download_subs

app = FastAPI()
router = APIRouter(redirect_slashes=False)

origins = [
    "https://www.youtube.com",
]

# Add your routes to the router
@router.get("/sub")
def write_subs(url: str, filename: str = None):
    # Execute your Python script here
    file_contents = download_subs(url, filename) 
    return file_contents

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)