from flask import Flask,jsonify, request
#creating a class - name is parameter
app = Flask(__name__)

contact = [
    {
        'Contact': '9987644456',
        'Name': 'Raju', 
        'done': False,
        'id': 1
    },
    {
        'Contact': '9876543222',
        'Name': 'Rahul', 
        'done': False,
        'id': 2
    }
]
# / - basic address and will take to main page
@app.route("/")
def hello_world():
    return "Hello World!"
#.route(inner info inside the page, method = posting information) 
# GET - get request asking the comp to get info
#create and update a resource
#Post can create multiple, PUT only 1 copy of the resource
#DELETE - remove completely
@app.route("/add-data", methods=["POST"])
#create a task
def add_task():
    #if request is not received - for flask output is always returned in json format
    if not request.json:
        return jsonify({
            #status - success or error
            "status":"error",
            "message": "Please provide the data!"
        #code for error - like 404 error
        },400)

    data = {
        'id': contact[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    #add the tasks
    contact.append(data)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    
#get data for you
@app.route("/get-data")
def get_task():
    return jsonify({
        #display the data, o ther para is status and errror
        "data" : contact
    }) 
#run the app o
if (__name__ == "__main__"):
    #if any error comes up it will try and fix it - debug
    app.run(debug=True)