#Importing serializers.
from rest_framework import serializers
#Importing Todo.
from todo.models import Todo
#Creating a class.
class TodoSerializer(serializers.ModelSerializer):
    #Specifying read only fields.
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()
    #Creating a sub class.
    class Meta:
        #Creating a object of a class.
        model = Todo
        #Creating a fields list.
        fields = [
            'id', 'title', 'memo', 'created', 'datecompleted', 'important'
        ]
#Creating a class.
class TodoCompleteSerializer(serializers.ModelSerializer):
    #Creating a sub class.
    class Meta:
        #Creating a object of a class.
        model = Todo
        #Creating a list of fields.
        fields = ['id']
        #Creating a read-only field list.
        read_only_fields = [
            'title', 'memo', 'created', 'datecompleted', 'important'
        ]