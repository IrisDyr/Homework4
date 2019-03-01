from flask import Blueprint, request, render_template
from flask import jsonify

courses_list = [
    {"id": 1, "name": "MAT230"},
    {"id": 2, "name": "COS350"},
    {"id": 3, "name": "ENG330"}
]

course_bluep = Blueprint('course_bluep', __name__, template_folder='templates')
    

          
@course_bluep.route("/<int:course_id>/<name>", methods=['POST', 'PUT'])             #POST AND PUT   
def course_put_post(course_id,name):
    if request.method == 'POST':
        id_exist = False
        for i in range(len(courses_list)):
            if courses_list[i-1]['id'] == course_id:
                id_exist = True
    
        if id_exist == False:
            courses_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(courses_list)
        else:
            return "ID already exist"

    else:
        for a in courses_list:
            if a["id"] == course_id:
                a.update({'name': name})
                return jsonify(a)

        courses_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(courses_list)
    


@course_bluep.route("/<int:course_id>", methods=['GET', 'DELETE'])       #GET METHOD                       
def course_delete_get(course_id):
    if request.method == 'GET':
        flag = False
        for course in courses_list:
            if course["id"] == course_id:
                flag = True
                return jsonify(course)
        if flag == False:    
            return "ID not Found!"

    else:
        flag = False
        for i in range(len(courses_list)): 
            if courses_list[i]['id'] == course_id: 
                del courses_list[i]
                flag = True
                return "Course was deleted!"

        if flag == False:
            return "ID was not Found!"


@course_bluep.route("/all", methods=['GET'])   # GET ALL METHOD
def get_all():
    return render_template('course.html', courses=courses_list)

