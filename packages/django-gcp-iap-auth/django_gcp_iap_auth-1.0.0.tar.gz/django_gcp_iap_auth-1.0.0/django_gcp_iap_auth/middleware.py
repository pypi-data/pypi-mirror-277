from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import login

User = get_user_model()


class IAPAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        iap_user_email = request.META.get('HTTP_X_GOOG_AUTHENTICATED_USER_EMAIL')

        if iap_user_email:
            email = iap_user_email.split(':')[1]  # Extract email from the header
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return

            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
