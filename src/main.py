import os
import requests
from bottle import run, post, get, request, Bottle, route, redirect
from bson.objectid import ObjectId
from src.database import Database
from src.tictactoe import Game


app = Bottle()
database = Database()


class Item:
    def __init__(self, item):
        self.item = item
        self.status = 0

    @staticmethod
    def to_dto(entry):
        item = dict()
        item['id'] = str(entry['_id'])
        item['item'] = entry['item']
        item['status'] = entry['status']
        return item

    @staticmethod
    def to_hateoas_list_dto(entry):
        item = dict()
        item['id'] = str(entry['_id'])
        item['href'] = request.url + '/' + str(entry['_id'])
        return item


@app.route('/')
def wrong():
    redirect('/items'),


@app.post('/items')
def create_item():
    item = request.json
    create_id = database.db.items.insert_one(item).inserted_id
    return dict(response=str(create_id))


@app.get('/items')
def list_items():
    find_items = database.db.items.find()
    entries = [Item.to_hateoas_list_dto(entry) for entry in find_items]
    return dict(response=entries)


@app.get('/items/<item_id>')
def get_item(item_id):
    find_item = database.db.items.find_one({'_id': ObjectId(item_id)})
    return dict(response=Item.to_dto(find_item))


@app.put('/items/<item_id>')
def update_item(item_id):
    item = request.json
    database.db.items.update_one({'_id': ObjectId(item_id)}, {'$set': item}, upsert=False)
    return


# -----------------------------------------------------


trivia_session_token = requests.get(
    'https://opentdb.com/api_token.php',
    params={
        'command': 'request'
    }
).json()['token']


def get_token():
    return trivia_session_token


def set_token(token):
    trivia_session_token = token
    return


@app.get('/trivia')
def trivia_game():
    response = requests.get(
        'https://opentdb.com/api.php',
        params={
            'amount': request.query.amount,
            'category': request.query.category,
            'token': get_token(),
        }
    )
    if response.json()['response_code'] == 3 or response.json()['response_code'] == 4:
        set_token(requests.get(
            'https://opentdb.com/api_token.php',
            params={
                'command': 'reset',
                'token': get_token(),
            }
        ).json()['token'])
        return requests.get(
            'https://opentdb.com/api.php',
            params={
                'amount': request.query.amount,
                'category': request.query.category,
                'token': get_token(),
            }
        ).json()
    return response.json()


@app.get('/trivia/categories')
def trivia_game_categories():
    response = requests.get('https://opentdb.com/api_category.php')
    return response.json()


# -----------------------------------------------------


# TODO: only one game instance?!?!
game = Game()


@app.get('/tictactoe/start')
def trivia_game_categories():
    game.start()


@app.get('/tictactoe/move')
def trivia_game_categories():
    compute_response = game.compute(int(request.query.position))
    return dict(response=compute_response)


# -----------------------------------------------------


if __name__ == '__main__':
    app.run(host='localhost', port=int(os.environ.get('PORT', 8080)))
