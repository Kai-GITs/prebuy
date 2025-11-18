import json

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def _parse_payload(request):
    """Support both form-encoded and JSON payloads."""
    if request.content_type == "application/json":
        try:
            return json.loads(request.body.decode())
        except json.JSONDecodeError:
            return {}
    return request.POST


@csrf_exempt
def login(request):
    if request.method != "POST":
        return JsonResponse({"status": False, "message": "Invalid request method."}, status=400)

    data = _parse_payload(request)
    username = data.get("username")
    password = data.get("password")

    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse(
            {"status": False, "message": "Login failed, please check your username or password."},
            status=401,
        )

    if not user.is_active:
        return JsonResponse({"status": False, "message": "Login failed, account is disabled."}, status=401)

    auth_login(request, user)
    return JsonResponse(
        {
            "username": user.username,
            "status": True,
            "message": "Login successful!",
        },
        status=200,
    )


@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({"status": False, "message": "Invalid request method."}, status=400)

    data = _parse_payload(request)
    form = UserCreationForm(data)
    if not form.is_valid():
        return JsonResponse({"status": False, "message": form.errors}, status=400)

    user = form.save()
    return JsonResponse(
        {
            "username": user.username,
            "status": "success",
            "message": "User created successfully!",
        },
        status=200,
    )


@csrf_exempt
def logout(request):
    username = request.user.username if request.user.is_authenticated else ""

    try:
        auth_logout(request)
        return JsonResponse(
            {
                "username": username,
                "status": True,
                "message": "Logged out successfully!",
            },
            status=200,
        )
    except Exception:
        return JsonResponse(
            {
                "status": False,
                "message": "Logout failed.",
            },
            status=401,
        )
