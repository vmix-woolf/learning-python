import memcache

client = memcache.('localhost', 11211)

client.set('key', {'value': 'ert'}, 60)

value = client.get('key')
print(value)

