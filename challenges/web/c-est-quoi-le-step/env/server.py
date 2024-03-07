from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
import re

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

def is_valid_origin(header: str) -> bool:
    if header is None:
        return False
    pattern = re.compile('^132\.207\.31\.\d{1,3}$')
    return pattern.match(header) is not None

@app.get("/docs", response_class=HTMLResponse)
def forbidden_docs():
    raise HTTPException(status_code=403, detail="Forbidden")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return open("index.html").read()

@app.get("/admin", response_class=HTMLResponse)
def read_admin(x_forwarded_for: str = Header(None, alias="X-Forwarded-For")):
    if is_valid_origin(x_forwarded_for):
        return open("step_yes.html").read()
    else:
        content = open("step_no.html").read()
        return content
