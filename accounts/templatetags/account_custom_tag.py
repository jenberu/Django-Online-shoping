from ..models import UserProfile
from django import template
from ..forms import UserProfileForm
register=template.Library()

@register.simple_tag(takes_context=True)
def get_profile_image(context):
    request= context['request']
    if request.user.is_authenticted:
        try:
            profile=UserProfile.objects.get(user=request.user)
            return profile.image.url
        except UserProfile.DoesNotExist:
            return None
    return None
@register.simple_tag
def get_profile_form():
    return UserProfileForm()

