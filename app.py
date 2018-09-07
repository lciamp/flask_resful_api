from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
app.secret_key = 'my_key'
api = Api(app)


items = []


class ItemList(Resource):
    def get(self):
        return {"items": items}


class Item(Resource):
    def get(self, name):
        item = next(iter([item for item in items if item['name'] == name]), None)
        return ({'item': item}, 200) if item else ({"message": "item '{}' not found".format(name)}, 404)

    def post(self, name):
        if next(iter([item for item in items if item['name'] == name]), None):
            return {'message': "An item with name '{}' already exists".format(name)}, 400
        data = request.get_json()
        item = {
            "name": name,
            "price": data['price']
        }
        items.append(item)
        return item, 201

    def put(self, name):
        pass

    def delete(self, name):
        pass


api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')


app.run(port=5000, debug=True)