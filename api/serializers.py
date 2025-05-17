from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.token import RefreshToken
class MultiSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls,user):
		token = super().get_token(user)

		token['username'] = user.username
		token['email'] = user.email
		token['first_name'] = user.first_name

		return token
	def validate(self,attrs):
		data = super().validate(attrs)

		data['username'] = self.user.username
		data['email'] = self.user.email
		data['first_name'] = self.user.first_name
		return data
