from matplotlib import pyplot as plt
import pandas as pd
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('setosa.html')
@app.route('/submit', methods=['POST','GET'])
def index2():
    s1 = request.form.get('splen', type=float)
    s2 = request.form.get('spwid', type=float)
    s3 = request.form.get('pelen', type=float)
    s4 = request.form.get('pewid', type=float)
    if s1 < 4.3 or s1 > 7.9 or s2 < 2.0 or s2 > 4.4 or s3 < 1.0 or s3 > 6.9 or  s4 < 0.1 or s4 > 2.5:
        return "<h1>the input value is invalid</h1>"
    '''if s2 < 2.0 or s2 > 4.4:
        return "the value for sepal width is invalid"
    if s3 < 1.0 or s3 > 6.9:
        return "the value for petal length is invalid"
    if s4 < 0.1 or s4 > 2.5:
        return "the value for petal width is invalid"'''
    if (s1 >= 4.3 and s1 <= 5.8) and (s2 >= 2.3 and s2 <= 4.4) and (s3 >= 1.0 and s3 <= 1.9) and (
            s4 >= 0.1 and s4 <= 0.6):
        return "<h1>the species is setosa</h1>"
    elif (s1 >= 4.9 and s1 <= 7.0) and (s2 >= 2.0 and s2 <= 3.4) and (s3 >= 3.0 and s3 <= 5.1) and (
            s4 >= 1.0 and s4 <= 1.8):
        return "<h1>the species is versicolor</h1>"
    elif (s1 >= 4.9 and s1 <= 7.9) and (s2 >= 2.2 and s2 <= 3.8) and (s3 >= 4.5 and s3 <= 6.9) and (
            s4 >= 1.4 and s4 <= 2.5):
        return "<h1>the species is verginica</h1>"
    else:
        return "<h1>does not belong to any species</h1>"


if __name__=="__main__":
    app.run()


'''
to find max and minimum value for virginica
    setosa range will be(0,50)
    versicolor range will be (50,100)

max1 = 0
min1 = 99
    for i in range(100, 150):
        if str(df.iloc[i]['species']) == 'virginica':
            if (max1 < df.iloc[i]['sepal_width']):
                max1 = df.iloc[i]['sepal_width']
            if (min1 > df.iloc[i]['sepal_width']):
                min1 = df.iloc[i]['sepal_width']
    print(max1, min1)'''
    
    
    
    
    
    
    #HTML FILE
    
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>sample</title>
</head>

<body style="background-image:url('/static/irisf.jpg');">
<form action="/submit" method="post">
    Enter sepal length: <input type="number" step="any" name="splen"/><br/><br>
    Enter sepal length: <input type="number" step="any" name="spwid"/><br/><br>
    Enter sepal length: <input type="number" step="any" name="pelen"/><br/><br>
    Enter sepal length: <input type="number" step="any" name="pewid"/><br/><br><br>
    <button type="submit">SUBMIT</button>
</form>
</body>
</html>
