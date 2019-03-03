from flask_restful import Resource
from flask import jsonify

students_list = [
    {"id": 1, "student": "Iris Dyrmishi"},
    {"id": 2, "student": "Ilda Duka"},
    {"id": 3, "student": "Fatme Tsiko"}
]
class Student_one(Resource):
    
          
    def post(self,student_id,name): #post method

        id_exist = False
        for i in range(len(students_list)):
            if students_list[i-1]['id'] == student_id:
                id_exist = True
    
        if id_exist == False:
            students_list.append(dict({'id': student_id, 'name': name}))
            return jsonify(students_list)
        else:
            return "ID already exist"

    def put(self,student_id,name):  #put method

        for a in students_list:
            if a["id"] == student_id:
                a.update({'name': name})
                return jsonify(a)

        students_list.append(dict({'id': student_id, 'name': name}))
        return jsonify(students_list)
    
    

class Student_two(Resource):

    def delete(self, student_id):  #delete method
        flag = False
        for i in range(len(students_list)): 
            if students_list[i]['id'] == student_id: 
                del students_list[i]
                flag = True
                return "Student was  deleted!"

        if flag == False:
            return "ID was not Found!"
            

    def get(self, student_id):  #get method
        flag = False
        for student in students_list:
            if student["id"] == student_id:
                flag = True
                return jsonify(student)
        if flag == False:    
            return "ID  was not Found!"
      

class All_students(Resource):
    def get(self):
        return jsonify(students_list)


