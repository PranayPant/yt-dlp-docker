from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
import ssl

from task import download_subs

app = FastAPI()
router = APIRouter(redirect_slashes=False)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('cert.pem', keyfile='key.pem')

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
# app.add_middleware(HTTPSRedirectMiddleware)
app.include_router(router)

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080, ssl=ssl_context)