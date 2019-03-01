from flask import Blueprint, request, render_template
from flask import jsonify

events_list = [
    {"id": 1, "event": "International Week"},
    {"id": 2, "event": "Dance Crew Performance"},
    {"id": 3, "event": "Alumni Day"}
]

event_bluep = Blueprint('event_bluep', __name__, template_folder='templates')
    

          
@event_bluep.route("/<int:event_id>/<name>", methods=['POST', 'PUT'])             #POST AND PUT   
def event_put_post(event_id,name):
    if request.method == 'POST':
        id_exist = False
        for i in range(len(events_list)):
            if events_list[i-1]['id'] == event_id:
                id_exist = True
    
        if id_exist == False:
            events_list.append(dict({'id': event_id, 'name': name}))
            return jsonify(events_list)
        else:
            return "ID already exist"

    else:
        for a in events_list:
            if a["id"] == event_id:
                a.update({'name': name})
                return jsonify(a)

        events_list.append(dict({'id': event_id, 'name': name}))
        return jsonify(events_list)
    

@event_bluep.route("/<int:event_id>", methods=['GET', 'DELETE'])       #GET METHOD                       
def event_delete_get(event_id):
    if request.method == 'GET':
        flag = False
        for event in events_list:
            if event["id"] == event_id:
                flag = True
                return jsonify(event)
        if flag == False:    
            return "ID not Found!"

    else:
        flag = False
        for i in range(len(events_list)): 
            if events_list[i]['id'] == event_id: 
                del events_list[i]
                flag = True
                return "Event was deleted!"

        if flag == False:
            return "ID was not Found!"

@event_bluep.route("/all", methods=['GET'])   # GET ALL METHOD
def get_all():
    return render_template('event.html', events=events_list)



