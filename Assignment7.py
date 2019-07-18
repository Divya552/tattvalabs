from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("first.html")


@app.route('/Add',methods=["GET","POST"])
def add():
    val1=request.form.get("val1",type=int)
    val2=request.form.get("val2",type=int)
    return 'The result is' +str(val1+val2)


@app.route('/submit1',methods=["GET","POST"])
def sub1():
    va1=request.form.get("val1",type=int)
    va2=request.form.get("val2",type=int)
    return 'The result is' +str(va1-va2)


@app.route('/submit2',methods=["GET","POST"])
def mul1():
    val1=request.form.get("val1",type=int)
    val2=request.form.get("val2",type=int)
    return 'The result is' +str(val1*val2)


@app.route('/submit3',methods=["GET","POST"])
def div1():
    val1=request.form.get("val1",type=int)
    val2=request.form.get("val2",type=int)
    return 'The result is' +str(val1/val2)


if __name__=="__main__":
    app.run()
    
    
    #first.html file contains the following code
    
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form  name="myform" action="/Add" method="post">
        val1: <input type="text" name="val1" id="val1"> <br/><br/>
        val2:<input type="text" name="val2" id="val2"><br/><br/>
        <button type="submit">Add</button>
        <button type="submit" onclick="javascript:form.action='/submit1';">Sub</button>
        <button type="submit" onclick="javascript:form.action='/submit2';">Mul</button>
        <button type="submit" onclick="javascript:form.action='/submit3';">Div</button>
</form >
</body>
</html>
