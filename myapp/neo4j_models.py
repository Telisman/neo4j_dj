from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipTo

class Person(StructuredNode):
    name = StringProperty()
    age = IntegerProperty()

    friends = RelationshipTo('Person', 'FRIENDS_WITH')
