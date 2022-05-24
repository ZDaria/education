from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    },
    {
        'name': 'MyWonderfulStore2',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    },

]

# POST - used to receive data
# GET - used to send data back only


@app.route('/')
def home():
    return render_template('index.html')


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string: name>
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5001/store/some_name'
def get_store(name):
    # Iterate over stores
    # if store name matches, return it
    # If not - return error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_item = request.get_json()
    new_item = {
        'name': request_item['name'],
        'price': request_item['price']
    }
    for store in stores:
        if store['name'] == name:
            store['items'].append(new_item)
            return jsonify({'stores': stores})
    return jsonify({'message': 'store not found'})


# GET /store/<string: name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    # Iterate over items in the store
    # If there is no stores in list
    # return error
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'There is no such stor name'})


app.run(port=5000)
