from flask import render_template, request, redirect, url_for
from app.views import insert_details
from app import app
from flask import jsonify


@app.route('/')
def index(error=None):
    return render_template('index.html', error=error)


@app.route('/insert', methods=["POST"])
def insert():
    print(request.form)
    print(request.method)
    if request.method == "POST":
        print('Posting')
        try:
            username = request.form.get('fullname')
            license = request.form.get('licence')
            gender = request.form.get('gender')
            dob = request.form.get('date')
            contact = request.form.get('phone')

            try:
                insert_details(username, license, gender, dob, contact)
                return render_template('main.html', username=username)
            except Exception as e:
                return render_template('main.html')
        except Exception as e:
            print(str(e))
            return render_template('main.html')
    else:
        print("Wrong")


@app.route('/test', methods=["GET"])
def test():
    data = {"message": "yooo"}
    print("Working")
    return jsonify(data)


@app.route('/send_message', methods=["POST"])
def send_message():
    message = request.get_json()
    print("MESSAGE", message)
    if len(message['message']) > 0:
        add_message(message['message'], message['username'])
        messages = get_all_messages()
        data = {}
        data['message'] = messages[-1].message
        data['sender'] = messages[-1].sentBy.username
        return jsonify(data)
    else:
        pass