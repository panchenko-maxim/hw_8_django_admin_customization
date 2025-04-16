from django.utils import timezone
from django.conf import settings
from datetime import timedelta
import jwt


def generate_jwt_token(user):
    payload = {
        "user_id": user.id,
        "username": user.nickname,
        "exp": timezone.now() + timedelta(days=settings.TOKEN_TTL.get("days", 0),
                                          minutes=settings.TOKEN_TTL.get("minutes", 0)),
        "iat": timezone.now()
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")