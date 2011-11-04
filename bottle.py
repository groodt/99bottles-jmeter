import bottle
import simplejson

bottle.debug(True)

@bottle.post('/bottle')
def store_bottle():
    raw_json = bottle.request.body
    json_string = ''.join(raw_json.readlines())
    parsed_json = simplejson.loads(json_string)
    print(parsed_json)
    return "Thanks"


bottle.run(host='localhost', port=9999, reloader=True)
