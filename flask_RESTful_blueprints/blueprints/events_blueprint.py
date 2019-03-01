from flask import Blueprint, request, render_template
from flask import jsonify

events_list = [
    {"id": 1, "event": "International Week"},
    {"id": 2, "event": "Dance Crew Performance"},
    {"id": 3, "event": "Alumni Day"}
]

course_bluep = Blueprint('course_bluep', __name__, template_folder='templates')
    

          
@course_bluep.route("/<int:course_id>/<name>", methods=['POST', 'PUT'])             #POST AND PUT   
def course_put_post(course_id,name):
    if request.method == 'POST':
        id_exist = False
        for i in range(len(events_list)):
            if events_list[i-1]['id'] == course_id:
                id_exist = True
    
        if id_exist == False:
            events_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(events_list)
        else:
            return "ID already exist"

    else:
        for a in events_list:
            if a["id"] == course_id:
                a.update({'name': name})
                return jsonify(a)

        events_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(events_list)
    

@course_bluep.route("/<int:course_id>", methods=['GET', 'DELETE'])       #GET METHOD                       
def course_delete_get(course_id):
    if request.method == 'GET':
        flag = False
        for course in events_list:
            if course["id"] == course_id:
                flag = True
                return jsonify(course)
        if flag == False:    
            return "ID not Found!"

    else:
        flag = False
        for i in range(len(events_list)): 
            if events_list[i]['id'] == course_id: 
                del events_list[i]
                flag = True
                return "Course was deleted!"

        if flag == False:
            return "ID was not Found!"

@course_bluep.route("/all", methods=['GET'])   # GET ALL METHOD
def get_all():
    return render_template('course.html', events=events_list)


