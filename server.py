#!/usr/bin/env python

import bottle
import simplejson

bottle.debug(True)

@bottle.post('/bottle')
def store_bottle():
    # Extract values from JSON POST body
    raw_json = bottle.request.body
    json_string = ''.join(raw_json.readlines())
    parsed_json = simplejson.loads(json_string)
    (num_bottles, drink, date, thread) = (parsed_json['bottles'], parsed_json['drink'], \
                                            parsed_json['date'], parsed_json['thread'])
    
    # Print the "99 Bottles" song to the console. Correctly pluralise "bottle".
    plural_bottles = "bottle" if (int(num_bottles)==1) else "bottles"
    print("%s %s of %s on the wall. Date=%s Thread=%s" % (num_bottles, plural_bottles, \
                                                                drink, date, thread))
    return "Cheers!"

# Run the server
bottle.run(server="paste", host='localhost', port=9999, reloader=True)
