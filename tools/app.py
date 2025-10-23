from flask import Flask, request
from controllers import send_email,  check_code, generate_verification_code
from flask import *

app = Flask(__name__)

@app.route('/codigo', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return 'Hello, World!'
    elif request.method == 'GET':
        sender_email = "codeverify@gmail.com"
        receiver_email = "el16062007@gmail.com"
        subject = "Login page verification code"
        send_code = generate_verification_code()
        send_email(sender_email, receiver_email, subject, code=send_code)
        base_url = f"{request.scheme}://{request.host.split(':')[0]}/app/html/code.html"
        return redirect(base_url, code=302)
@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        return 'Hello, World!'
    elif request.method == 'GET':
        stored_code = check_code()
        if stored_code == request.args.get('code'):
            base_url = f"{request.scheme}://{request.host.split(':')[0]}/app/html/homepage.html"
            return redirect(base_url, code=302)
        else :
            base_url = f"{request.scheme}://{request.host.split(':')[0]}/app/html/code.html"
            return redirect(base_url, code=302)


if __name__ == '__main__':
    app.run()