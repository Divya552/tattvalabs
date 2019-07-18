from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('web.html')
@app.route('/home',methods=['GET','POST'])
def index1():
    return render_template('home.html')
@app.route('/about',methods=['GET','POST'])
def index2():
    return render_template('about.html')
@app.route('/contact',methods=['GET','POST'])
def index3():
    return render_template('contact.html')
@app.route('/feedback',methods=['GET','POST'])
def index4():
    return render_template('feedback.html')
if __name__=="__main__":
    app.run()


#following are the html files
#web.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <div align="right">
       <a href="/home" ><button type="submit">Home</button></a>
        <a href="/about" ><button type="submit">About</button></a>
        <a href="/contact" ><button type="submit">Contact US</button></a>
        <a href="/feedback" ><button type="submit">Feedback</button></a>
    </div>

</body>
</html>

#home.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
<h1>
    hello all
    welcome to our page
</h1>
<img allign="middle" width="" src="http://www.thesitsgirls.com/wp-content/uploads/2011/05/Welcome.jpg">
</body>
</html>

#about.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About</title>
</head>
<body>
our website name is welcome website.<br>
you can find so many images which will motivate and will give happiness to you.<br>
it also contains motivational quotes and messages which will motivate you to achieve yur dreams.<br>

</body>
</html>

#contact.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>contact us</title>
</head>
<body>
<h1>here is our contact information:<h1>
    founder:7406832276<br>
    Manager:8762988276
</body>
</html>

#feedback.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Feedback</title>
</head>
<body>
<form  name="myform" action="/feedback" method="get">
    Enter Message: <br> <input type="text"  name="msg" id="msg">
    <button type="submit">Submit</button>
</form>
</body>
</html>
