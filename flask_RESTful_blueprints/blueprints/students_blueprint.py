from flask import Blueprint, request, render_template
from flask import jsonify

students_list = [
    {"id": 1, "student": "Iris Dyrmishi"},
    {"id": 2, "student": "Ilda Duka"},
    {"id": 3, "student": "Fatme Tsiko"}
]

student_bluep = Blueprint('student_bluep', __name__, template_folder='templates')
    
          
@student_bluep.route("/<int:student_id>/<name>", methods=['POST', 'PUT'])             #POST AND PUT   
def student_put_post(student_id,name):
    if request.method == 'POST':
        id_exist = False
        for i in range(len(students_list)):
            if students_list[i-1]['id'] == student_id:
                id_exist = True
    
        if id_exist == False:
            students_list.append(dict({'id': student_id, 'name': name}))
            return jsonify(students_list)
        else:
            return "ID already exist"

    else:
        for a in students_list:
            if a["id"] == student_id:
                a.update({'name': name})
                return jsonify(a)

        students_list.append(dict({'id': student_id, 'name': name}))
        return jsonify(students_list)
    

@student_bluep.route("/<int:student_id>", methods=['GET', 'DELETE'])       #GET METHOD                       
def student_delete_get(student_id):
    if request.method == 'GET':
        flag = False
        for student in students_list:
            if student["id"] == student_id:
                flag = True
                return jsonify(student)
        if flag == False:    
            return "ID not Found!"

    else:
        flag = False
        for i in range(len(students_list)): 
            if students_list[i]['id'] == student_id: 
                del students_list[i]
                flag = True
                return "Student was deleted!"

        if flag == False:
            return "ID was not Found!"

@student_bluep.route("/all", methods=['GET'])   # GET ALL METHOD
def get_all():
    return render_template('student.html', students=students_list)



