#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response
from subjectDAO import subjectDAO

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

@app.route('/')
def index():
    return "Hello, World!"

subjects = [
    {
        "subject":"History",
        "term":"1",
        "lecturer":"M. Angelo",
        "credits":5
    },
    {
        "subject":"Mechanics",
        "term":"2",
        "lecturer":"J. Ford",
        "credits":10
    },
    {
        "subject":"Electronics",
        "term":"2",
        "lecturer":"A. Bell",
        "credits":15
    }
]

# I found various repo's on github helpful in understanding the below so I have ensured to reference them within the references of my project in the README file, along with the other useful sites I referenced for this project.

@app.route('/subjects', methods=['GET'])
def get_subjects():
    return jsonify( {'subjects':subjects})
# curl -i http://localhost:5000/subjects

@app.route('/subjects/<string:reg>', methods =['GET'])
def get_subject(subject):
    foundCars = list(filter(lambda t : t['subject'] == subject , subjects))
    if len(foundSubjects) == 0:
        return jsonify( { 'subjects' : '' }),204
    return jsonify( { 'subjects' : foundSubjects[0] })
#curl -i http://localhost:5000/subjects/test

@app.route('/subjects', methods=['POST'])
def create_subject():
    if not request.json:
        abort(400)
    if not 'subject' in request.json:
        abort(400)
    car={
        "subject":  request.json['subject'],
        "term": request.json['term'],
        "lecturer":request.json['lecturer'],
        "credits":request.json['credits']
    }
    subjects.append(subject)
    return jsonify( {'subject':subject }),201

curl -i -H "Content-Type:application/json" -X POST -d "{\"subject\":\"Geography\",\"term\":\"1\",\"lecturer\":\"C. Columbus\",\"credits\":10}" http://localhost:5000/subjects
@app.route('/subjects/<string:subject>', methods =['PUT'])
def update_subject(subject):
    foundSubjects=list(filter(lambda t : t['subject'] ==subject, subjects))
    if len(foundSubjects) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'make' in request.json and type(request.json['term']) != str:
        abort(400)
    if 'model' in request.json and type(request.json['lecturer']) is not str:
        abort(400)
    if 'price' in request.json and type(request.json['credits']) is not int:
        abort(400)
    foundSubjects[0]['term']  = request.json.get('term', foundSubjects[0]['term'])
    foundSubjects[0]['lecturer'] =request.json.get('lecturer', foundSubjects[0]['lecturer'])
    foundSubjects[0]['credits'] =request.json.get('credits', foundSubjects[0]['credits'])
    return jsonify( {'subject':foundSubjects[0]})

curl -i -H "Content-Type:application/json" -X PUT -d "{\"term\":\"3\"}" http://localhost:5000/subjects/History

@app.route('/subjects/<string:subject>', methods =['DELETE'])
def delete_subject(subject):
    foundSubjects = list(filter (lambda t : t['reg'] == subject, subjects))
    if len(foundSubjects) == 0:
        abort(404)
    subjects.remove(foundSubjects[0])
    return  jsonify( { 'result':True })

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)