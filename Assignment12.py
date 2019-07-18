from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index2():
    return render_template('index2.html')
@app.route('/submit',methods=['GET','POST'])
def abc():
    pwd=request.form.get('pwd')
    if (pwd=="divya"):
        return  "welcome to the page"
    else:
        return "login Failed"

if __name__=="__main__":
    app.run()

#in index2.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<form name="myform" action="/submit" method="post">
    Password:<input type="text" name="pwd" id="pwd">
    <button type="submit">Submit</button>
</form>
</body>
</html>
