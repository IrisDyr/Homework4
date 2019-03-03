from flask_restful import Resource
from flask import jsonify

courses_list = [
    {"id": 1, "name": "MAT230"},
    {"id": 2, "name": "COS350"},
    {"id": 3, "name": "ENG330"}
]
class Course_one(Resource):
    
          
    def post(self,course_id,name):   #post method

        id_exist = False
        for i in range(len(courses_list)):
            if courses_list[i-1]['id'] == course_id:
                id_exist = True
    
        if id_exist == False:
            courses_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(courses_list)
        else:
            return "ID already exist"

    
    def put(self,course_id,name):  #Put method

        for a in courses_list:
            if a["id"] == course_id:
                a.update({'name': name})
                return jsonify(a)

        courses_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(courses_list)
    
    

class Course_two(Resource):

    def delete(self, course_id):  #delete method
        flag = False
        for i in range(len(courses_list)): 
            if courses_list[i]['id'] == course_id: 
                del courses_list[i]
                flag = True
                return "Course was  deleted!"

        if flag == False:
            return "ID was not Found!"


    def get(self, course_id):  #get method
        flag = False
        for course in courses_list:
            if course["id"] == course_id:
                flag = True
                return jsonify(course)
        if flag == False:    
            return "ID  was not Found!"
      

class All_courses(Resource):
    def get(self):
        return jsonify(courses_list)

