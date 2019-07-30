from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('string.html')

@app.route('/submit',methods=['GET','POST'])
def index1():
    v1 = request.form.get('val1',type=int)
    v2 = request.form.get('val2',type=int)
    v3=  request.form.get('val3',type=int)
    print(v1,v2,v3)
    n='''Hello all Welcome to 
    HUBBALLI'''
    d=len(n)
    c=d-(n.count(' ')+n.count('\n'))
    print(c)
    a = n.split()
    words=len(a)
    b = n.split('\n')
    lines=len(b)
    if v1==lines and v2==words and v3==c:
        return "<h1>SUCCESS</h1>"
    else:
        return "<h1>FAIL</h1>"

if __name__=="__main__":
    app.run()
    
    
    
    
    #HTMLFILE
    
    <!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <title>time game</title>
</head>
<body style="background-color:aqua;">
<form name="myform" style="position:absolute;top:15%;left:40%;">
    <h1> Hello all Welcome to </h1>
    <h1>HUBBALLI</h1>
</form>
        <form name="myform"   method="post" >
            <div style="position:absolute;top:45%;left:10%;">
No of Lines:<p><input type="number"name="val1" id="val1" style="font-size:18pt;height=35px;width=200px;"></p>
No of Words:<p><input type="number"name="val2" id="val2" style="font-size:18pt;height=35px;width=200px;"></p>
No of Characters:<p><input type="number"name="val3" id="val3" style="font-size:18pt;height=35px;width=200px;"></p></div>
          <div style="position:absolute; bottom:10%;right:45%; font-size:40pt;">
        <input type="submit" formaction="/submit" name="submit" id="submit" style="font-size:9pt;height:35px;width:100px; background-color:grey;" value="SUBMIT">
            </div>

<div id="timer" style="position:absolute; top:5%;right:5%; font-size:40pt; color:red;"></div>

<script type="text/javascript">

var timeoutHandle;
function countdown(minutes,seconds){
 function tick(){
  var counter=document.getElementById("timer");

  counter.innerHTML=minutes.toString()+":" + (seconds<10 ? "0" : "")+ String(seconds);
  seconds--;
  if(seconds>=0) {
  timeoutHandle=setTimeout(tick,1000);
  }else {
   if(minutes>=1) {
   setTimeout(function() {
   countdown(minutes-1,59);
   }, 1000);
   }
  }
 }
 tick();
 }
 countdown(1,30);
var auto_refresh=setInterval(function(){
submitform();
},90000);

function submitform() {
document.getElementById("submit").click();
}
</script>
            </form>
</body>
</html>
