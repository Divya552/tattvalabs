from flask import Flask, render_template,request
import pandas as pd
import csv
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST','GET'])
def login():
    name=request.form.get('name')
    email=request.form.get('email')
    passwd=request.form.get('password')
    re_password=request.form.get('re_password')
    if passwd==re_password:
        with open('store2.csv','a')as nf:
            newFileWriter=csv.writer(nf)
            newFileWriter.writerow([name,email,passwd])
        return render_template('indexx.html')
    else:
        return "<h1>Invalid password or username</h1>"

@app.route('/direct', methods=['POST','GET'])
def dir():
    return render_template('indexx.html')

@app.route('/login', methods=['POST','GET'])
def login1():
    name1=request.form.get('username')
    passwd1=request.form.get('pass')
    d=pd.read_csv('store2.csv')
    n=len(d)
    print(n)
    print(d)
    print(name1,passwd1)
    for i in range(0,n):
        print(i)
        if name1 == str(d.iloc[i]['Username']) and passwd1 == str(d.iloc[i]['Password']):
            return "<h1>WELCOME TO PAGE</h1>"
    return "<h1>INVALID PASSWORD</h1>"

if __name__=="__main__":
    app.run()




#inde.html file SIGNUP PAGE
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Sign Up Form by Colorlib</title>

    <!-- Font Icon -->
    <link rel="stylesheet" href="/static/index1/fonts/material-icon/css/material-design-iconic-font.min.css">

    <!-- Main css -->
    <link rel="stylesheet" href="/static/index1/css/style.css">
</head>
<body>

    <div class="main">

        <section class="signup">
            <!-- <img src="images/signup-bg.jpg" alt=""> -->
            <div class="container">
                <div class="signup-content">
                    <form method="POST" id="signup-form" class="signup-form" action="/signup">
                        <h2 class="form-title">Create account</h2>
                        <div class="form-group">
                            <input type="text" class="form-input" name="name" id="name" placeholder="Your Name"/>
                        </div>
                        <div class="form-group">
                            <input type="email" class="form-input" name="email" id="email" placeholder="Your Email"/>
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-input" name="password" id="password" placeholder="Password"/>
                            <span toggle="#password" class="zmdi zmdi-eye field-icon toggle-password"></span>
                        </div>
                        <div class="form-group">
                            <input type="password" class="form-input" name="re_password" id="re_password" placeholder="Repeat your password"/>
                        </div>
                        <div class="form-group">
                            <input type="checkbox" name="agree-term" id="agree-term" class="agree-term" />
                            <label for="agree-term" class="label-agree-term"><span><span></span></span>I agree all statements in  <a href="#" class="term-service">Terms of service</a></label>
                        </div>
                        <div class="form-group">
                            <input type="submit" name="submit" id="submit" class="form-submit" value="Sign up"/>
                        </div>
                    </form>
                    <p class="loginhere">
                        Have already an account ? <a href="/direct" class="loginhere-link">Login here</a>
                    </p>
                </div>
            </div>
        </section>

    </div>

    <!-- JS -->
    <script src="/static/index1/vendor/jquery/jquery.min.js"></script>
    <script src="/static/index1/js/main.js"></script>
</body><!-- This templates was made by Colorlib (https://colorlib.com) -->
</html>



#indexx.html LOGIN PAGE
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Login V3</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="/static/index2/images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/static/index2/vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/static/index2/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/static/index2/fonts/iconic/css/material-design-iconic-font.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/static/index2/vendor/animate/animate.css">
<!--===============================================================================================-->	
	<link rel="stylesheet" type="text/css" href="/static/index2/vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/static/index2/vendor/animsition/css/animsition.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/static/index2/vendor/select2/select2.min.css">
<!--===============================================================================================-->	
	<link rel="stylesheet" type="text/css" href="/static/index2/vendor/daterangepicker/daterangepicker.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="/static/index2/css/util.css">
	<link rel="stylesheet" type="text/css" href="/static/index2/css/main.css">
<!--===============================================================================================-->
</head>
<body>
	
	<div class="limiter">
		<div class="container-login100" style="background-image: url('/static/index2/images/bg-01.jpg');">
			<div class="wrap-login100">
				<form class="login100-form validate-form" action="/login" method="post">
					<span class="login100-form-logo">
						<i class="zmdi zmdi-landscape"></i>
					</span>

					<span class="login100-form-title p-b-34 p-t-27">
						Log in
					</span>

					<div class="wrap-input100 validate-input" data-validate = "Enter username">
						<input class="input100" type="text" name="username" placeholder="Username">
						<span class="focus-input100" data-placeholder="&#xf207;"></span>
					</div>

					<div class="wrap-input100 validate-input" data-validate="Enter password">
						<input class="input100" type="password" name="pass" placeholder="Password">
						<span class="focus-input100" data-placeholder="&#xf191;"></span>
					</div>

					<div class="contact100-form-checkbox">
						<input class="input-checkbox100" id="ckb1" type="checkbox" name="remember-me">
						<label class="label-checkbox100" for="ckb1">
							Remember me
						</label>
					</div>

					<div class="container-login100-form-btn">
						<button class="login100-form-btn" type="submit">
							Login
						</button>
					</div>

					<div class="text-center p-t-90">
						<a class="txt1" href="#">
							Forgot Password?
						</a>
					</div>
				</form>
			</div>
		</div>
	</div>
	

	<div id="dropDownSelect1"></div>
	
<!--===============================================================================================-->
	<script src="/static/index2/vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="/static/index2/vendor/animsition/js/animsition.min.js"></script>
<!--===============================================================================================-->
	<script src="/static/index2/vendor/bootstrap/js/popper.js"></script>
	<script src="/static/index2/vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="/static/index2/vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="/static/index2/vendor/daterangepicker/moment.min.js"></script>
	<script src="/static/index2/vendor/daterangepicker/daterangepicker.js"></script>
<!--===============================================================================================-->
	<script src="/static/index2/vendor/countdowntime/countdowntime.js"></script>
<!--===============================================================================================-->
	<script src="/static/index2/js/main.js"></script>

</body>
</html>
