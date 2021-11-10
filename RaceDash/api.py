import json
from flask import Flask
from flask_restful import Resource, Api, reqparse
import dbBroker

class api():
    
    def __init__(self, dbBroker: dbBroker.Broker) -> None:
        super().__init__()
        #start api server
        app = Flask(__name__)
        api = Api(app)
        self.dbBroker = dbBroker
        api.add_resource(GetMostRecentByName, '/getmostrecentbyname')
            #resource_class_kwargs={'car': curCar})
        api.add_resource(GetMostRecent, '/getmostrecent')
        api.add_resource(GetRangeByName, '/getrangebyname')
        api.add_resource(GetAllByRange, '/getallbyrange')
        api.add_resource(PutSingleFrame, '/postsingleframe')
        api.add_resource(PutFrameGroup, '/postframegroup')
        api.add_resource(PutCommand, '/postcommand')
        api.add_resource(GetAllByName, '/getallbyname')

        if __name__ == '__main__':
            app.run()

    def GetMostRecentByName():
            #copilot
            # parser = reqparse.RequestParser()
            # parser.add_argument('name', type=str)
            # args = parser.parse_args()
            # return self.dbBroker.getMostRecentByName(args['name'])
        pass

    def GetMostRecent():
        pass
    
    def GetRangeByName():
        pass
    
    def GetAllByRange():
        pass
    
    def PutSingleFrame(self, frame):
        self.dbBroker.insert()
        pass
    
    def PutFrameGroup():
        pass
    
    def PutCommand():
        pass
    
    def GetAllByName():
        pass

class GetMostRecentByName(Resource):
    
    def get():
        #execute sql cmd
        #take entry from db and conv to json
        #return json
        pass

class GetMostRecent(Resource):
    
    def get():
        pass

class GetRangeByName(Resource):
    
    def get():
        pass

class GetAllByRange(Resource):
    
    def get():
        pass

class GetLive(Resource):
    
    def get():
        pass

class PutSingleFrame(Resource):
    
    def put():
        pass

class PutFrameGroup(Resource):
    
    def put():
        pass

class PutCommand(Resource):
    
    def put():
        pass

class GetAllByName(Resource):
    
    def get():
        pass

#this is just here for example
class carApi(Resource):
    
    def __init__(self, car) -> None:
        self.car = car

    
    def ToJson(self):
        return json.dumps(self.car.__dict__, indent=4, sort_keys=True, default=str)

    def get(self):
        return self.ToJson(), 200