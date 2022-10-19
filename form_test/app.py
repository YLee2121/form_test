import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message


UPLOAD_FOLDER = './static/product_pic/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# send mail

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bumarketplace488@gmail.com'
app.config['MAIL_PASSWORD'] = 'grihtpchplddgqkv'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



mail = Mail(app)




a = 'kylelee@gapp.nthu.edu.tw'
b = 'kyleleey@bu.edu'

@app.route("/send")
def send():
    msg = Message('COOLCOOLONE', sender = 'bumarketplace488@gmail.com', recipients = [a, b])
    msg.body = "TODAY IS GOOD Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"







def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)


        pic_name  = secure_filename(request.files['file'].filename)

        saver = request.files['file']

        directory = './status/product_pic/' + 'mike/'
        if not os.path.exists(directory):
            os.mkdir(directory)
        path1 = directory + pic_name 


        path = f'./status/product_pic/{pic_name}'
        print(path1)
        # saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        saver.save(path1)


    return render_template('home.html')


if __name__ == '__main__':
    print(os.path.join(app.config['UPLOAD_FOLDER']))
    app.run(debug=True)