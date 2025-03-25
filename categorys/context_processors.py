from django.contrib.auth.models import AnonymousUser

def user_context(request):
    return {
        'user': request.user if request.user.is_authenticated else AnonymousUser()
    }
