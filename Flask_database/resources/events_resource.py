from flask_restful import Resource
from flask import jsonify

events_list = [
    {"id": 1, "event": "International Week"},
    {"id": 2, "event": "Dance Crew Performance"},
    {"id": 3, "event": "Alumni Day"}
]
class Event_one(Resource):
    
           
    def post(self,event_id,name):  #post medhod

        id_exist = False
        for i in range(len(events_list)):
            if events_list[i-1]['id'] == event_id:
                id_exist = True
    
        if id_exist == False:
            events_list.append(dict({'id': event_id, 'name': name}))
            return jsonify(events_list)
        else:
            return "ID already exist"

    def put(self,event_id,name):  #put method

        for a in events_list:
            if a["id"] == event_id:
                a.update({'name': name})
                return jsonify(a)

        events_list.append(dict({'id': event_id, 'name': name}))
        return jsonify(events_list)
    
    

class Event_two(Resource):

    def delete(self, event_id):  #delete method
        flag = False
        for i in range(len(events_list)): 
            if events_list[i]['id'] == event_id: 
                del events_list[i]
                flag = True
                return "Event was  deleted!"

        if flag == False:
            return "ID was not Found!"
            

    def get(self, event_id):  #get method
        flag = False
        for event in events_list:
            if event["id"] == event_id:
                flag = True
                return jsonify(event)
        if flag == False:    
            return "ID  was not Found!"
      

class All_events(Resource):
    def get(self):
        return jsonify(events_list)


