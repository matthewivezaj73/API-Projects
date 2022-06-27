#Importing libraries.
from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer, VoteSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    #Creating a variable that posts all objects.
    queryset = Post.objects.all()
    #Creating a Serializer.
    serializer_class = PostSerializer
    #Creating a blank list to contain different permissions.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #Creating a method.
    def perform_create(self, serializer):
        #Saving the post. Grabbing whatever user made the api call and set it as the poster.
        serializer.save(poster=self.request.user)
class PostRetrieveDestroy(generics.RetrieveDestroyAPIView):
    #Creating a variable that posts all objects.
    queryset = Post.objects.all()
    #Creating a Serializer.
    serializer_class = PostSerializer
    #Creating a blank list to contain different permissions.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #Creating a method to delete a post.
    def delete(self, request, *args, **kwargs):
        #Checking if the post belongs to the user.
        post = Post.objects.filter(pk=self.kwargs['pk'], poster=self.request.user)
        #checking if the post exists.
        if post.exists():
            #Making a proper delete.
            return self.destroy(request, *args, **kwargs)
        #handling the case where the post does not exist.
        else:
            #Raising a validation when the user tries to delete the post.
            raise ValidationError("You cannot delete someone else's post!")
# Create your views here.
class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    #Creating a Serializer.
    serializer_class = VoteSerializer
    #Creating a blank list to contain different permissions.
    permission_classes = [permissions.IsAuthenticated]

    #Creating a method.
    def get_queryset(self):
        #Assigning a request from the user to a variable.
        user = self.request.user
        #Creating a get request from a post object and assigning it to a variable.
        post = Post.objects.get(pk=self.kwargs['pk'])
        #Returning the votes.
        return Vote.objects.filter(voter=user, post=post)
    #Creating a perform_create method.
    def perform_create(self, serializer):
        #Checking if self.get_queryset() is available.
        if self.get_queryset().exists():
            #Raising an exception.
            raise ValidationError('You have already voted for this post :)')
        #Creating a way for the user to request a save.
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))
    #Creating a new function to delete vote.
    def delete(self, request, *args, **kwargs):
        #Checking if vote exists.
        if self.get_queryset().exists():
            #Deleting the query set.
            self.get_queryset().delete()
            #Returning a response.
            return Response(status=status.HTTP_204_NO_CONTENT)
        #Handling the case where the vote does not exist.
        else:
            #Raising a validationerror.
            raise ValidationError("You never voted for this post...silly!")
