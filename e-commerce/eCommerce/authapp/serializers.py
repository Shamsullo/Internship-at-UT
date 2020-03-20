from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import * 


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        models = User
        fields = '__all__'


# class CustomAuthToken(ObtainAuthToken):

    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data,
    #                                        context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data['user']
    #     token, created = Token.objects.get_or_create(user=user)
    #     return Response({
    #         'token': token.key,
    #         'user_id': user.pk,
    #         'email': user.email
    #     })