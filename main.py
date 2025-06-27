from fastapi import FastAPI
app = FastAPI()

def index():
    return 'heyy'

@app.get('/')
def test():
    return {'message': 'Hello World'}