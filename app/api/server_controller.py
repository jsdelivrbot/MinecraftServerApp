from app import app
from flask import Response, jsonify
from app.utilities import server_utilities


# todo: need to return an error/correct HTTP response code if errored.
@app.route('/api/server_controller/turn_on', methods=['PUT'])
def turn_on():
    response = server_utilities.turn_on()
    if response:
        return Response('Server is on.', 200)
    return Response('Server is either already on or errored.', 404)


@app.route('/api/server_controller/turn_off', methods=['PUT'])
def turn_off():
    response = server_utilities.turn_off()
    if response:
        return Response('Server is off', 200)
    return Response('Server is either already off or errored', 404)


@app.route('/api/server_controller/who_is_on', methods=['GET'])
def who_is_on():
    response = server_utilities.who_is_on()
    return Response(jsonify(response), 200)


@app.route('/api/server_controller/is_players', methods=['GET'])
def is_players():
    response = server_utilities.is_players()
    return Response(jsonify(response), 200)


@app.route('/api/server_controller/is_on', methods=['GET'])
def is_on():
    try:
        response = server_utilities.is_on()
        return Response('{}'.format(response), 200)
    except Exception as error:
        print('ERROR!, {}'.format(error))
        return Response(404)
