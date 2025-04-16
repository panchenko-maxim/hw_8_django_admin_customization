from django.utils import timezone
from django.conf import settings
from datetime import timedelta
import jwt
# import secrets

# def creat_token_for_user(user):
#     from tasks_restfull.models import CustomToken
#     token = secrets.token_hex(20)
#     expires_at = timezone.now() + timedelta(days=settings.TOKEN_TTL.get("days", 0),
#                                             minutes=settings.TOKEN_TTL.get("minutes", 0))
#     return CustomToken.objects.create(key=token, user=user, expires_at=expires_at)



def generate_jwt_token(user):
    payload = {
        "user_id": user.id,
        "username": user.nickname,
        "exp": timezone.now() + timedelta(days=settings.TOKEN_TTL.get("days", 0),
                                          minutes=settings.TOKEN_TTL.get("minutes", 0)),
        "iat": timezone.now()
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")