from .models import Profile

from doctors.models import Doctor
def user_profile(request):
    """Add user profile to template context"""
    context = {}
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            context['user_profile'] = profile
            context['user_role'] = profile.role
        except Profile.DoesNotExist:
            context['user_profile'] = None
            context['user_role'] = None
    return context


def role_flags(request):
    is_doctor = "no"
    if request.user.is_authenticated:
        is_doctor = "yes" if Doctor.objects.filter(user=request.user).exists() else "no"
    return {"is_doctor": is_doctor}
