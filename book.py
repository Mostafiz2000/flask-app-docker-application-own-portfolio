from flask import Flask,jsonify,request,render_template
from flask.wrappers import Request
from werkzeug.wrappers import request


app=Flask(__name__,template_folder='template')
book_db=[{
    'name':"Physics",
    'price':250},
    {
        'name':"Mathematics",
        'price':180
    }
]
@app.route("/")
def hello_world():
  return "hello world"
@app.route("/portfolio")
def portfolio():
    return render_template('index.html')

@app.route("/books")
def get_all_books():
    return jsonify({'books':book_db})
# retreive a single books object
@app.route("/books/<string:n>")
def get_book(n):
    for book in book_db:
        if book['name'] == n:
            return jsonify(book)
    jsonify({'message':'book not found'})
#create an object using API
@app.route("/books",methods=['POST'])
def create_books():
    body_data=request.get_json()
    book_db.append(body_data)
    return jsonify({'message':"books hasbeen create"})
if __name__ =="__main__":
    app.run(debug=True)