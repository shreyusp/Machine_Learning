from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/compute')
def compute():
    a=10
    b=20
    c=a+b
    return " Sum of {} and {} is {}".format(a,b,c)

if __name__=='__main__':
    app.run(debug=True)