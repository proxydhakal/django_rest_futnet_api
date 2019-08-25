from rest_framework import serializers
from apis.posts.models import Post,Feedback
from django.shortcuts import render,get_object_or_404

class CommentSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print('kwargs',kwargs)
        self.kwargs=kwargs
        context = kwargs.get('context')
        # print('context',context)
    
        if context:
            # print(dir(context.get('view')))
            # print(context.get('view').kwargs)
            self.request = context.get('request')
            self.parms=context.get('view').kwargs
    class Meta:
        model=Feedback
        fields =('pk','comment',)

    def create(self, validated_data):
        comments=Feedback(**validated_data)
        comments.commentator= self.request.user
        comments.post = get_object_or_404(Post,pk=self.parms.get('pk'))
        comments.save()
        return comments


class PostSerializer(serializers.ModelSerializer):
    comments= CommentSerializer(many=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('request')

    class Meta:
        model =Post
        fields =('pk','time','date','venue','author','created_at','likes','comments')


    def create(self, validate_data):
        posts =Post(**validate_data)
        posts.author=self.request.user
        posts.save()
        return posts
