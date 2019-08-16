from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display',methods=['POST'])
def display():
    name=request.form.get('user_name')
    return "hello "+name

if __name__=='__main__':
    app.run(debug=True)

