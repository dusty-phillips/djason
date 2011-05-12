"""
Serialize data to/from JSON storing the results in an object with
possible extra attributes.

So where the djason.json serializer would return
[{attr1: val1},...] this one will return
{akey: avalue, anotherkey:anothervalue, objects:[{attr1:val1},...]}
"""
from django.utils import simplejson
from json import Serializer as JsonSerializer
from django.core.serializers.json import Deserializer as JSONDeserializer, \
    DjangoJSONEncoder

class Serializer(JsonSerializer):
    """
    Convert a queryset to JSON.
    """
    def end_serialization(self):
        """Output a JSON encoded queryset."""
        self.options.pop('stream', None)
        self.options.pop('fields', None)
        self.options.pop('excludes', None)
        self.options.pop('relations', None)
        self.options.pop('extras', None)
        self.options.pop('use_natural_keys', None)
        self.use_httpresponse=self.options.pop('httpresponse', None)

        attributes = self.options.pop('attributes', {})
        list_name = self.options.pop('list_name', 'objects')
        attributes[list_name] = self.objects
        simplejson.dump(attributes, self.stream, cls=DjangoJSONEncoder,
            **self.options)


Deserializer = JSONDeserializer
