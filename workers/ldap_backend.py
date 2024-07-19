import ldap3
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.conf import settings
from ldap3.core.exceptions import LDAPException

class LDAPBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        server = ldap3.Server(settings.AUTH_LDAP_SERVER_URI)
        try:
            conn = ldap3.Connection(server, user=f'{settings.AUTH_LDAP_DOMAIN}\\{username}', password=password, auto_bind=True)
            conn.search(settings.AUTH_LDAP_SEARCH_BASE, f'(sAMAccountName={username})', attributes=['givenName', 'sn', 'mail'])
            if not conn.entries:
                return None

            user_data = conn.entries[0]

            user, created = User.objects.get_or_create(username=username)
            user.first_name = user_data.givenName.value if user_data.givenName.value else ''
            user.last_name = user_data.sn.value if user_data.sn.value else ''
            user.email = user_data.mail.value if user_data.mail.value else ''
            user.set_unusable_password()
            user.save()

            return user
        except LDAPException:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
