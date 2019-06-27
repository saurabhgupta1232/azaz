from app import app
@app.route('/')
@app.route('/index')
def index ():
    return '<html><head><title>aditya</title></head><body>hello world</body></html>' 

