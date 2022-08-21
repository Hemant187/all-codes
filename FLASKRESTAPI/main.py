import re
from flask import Flask , jsonify ,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"
@app.route("/armstrong/<int:n>")
def armstrong(n):
    # n = int(input('Enter your number\n'))
    sum =0
    order = len(str(n))
    copy_n =n

    while(n>0):
        digit = n%10
        sum += digit ** order
        n = n//10

    if sum == copy_n:
        result ={
            'Number':copy_n,
            'result':True
        }
    else:        
        result ={
            'Number':copy_n,
            'result':False
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)