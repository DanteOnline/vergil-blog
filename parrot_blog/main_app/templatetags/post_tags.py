from django import template

register = template.Library()


@register.filter(name='can_moderate')
def can_moderate(user, post):
    """
    Проверяет может ли пользователь редактировать и удалять пост
    Они либо его создатель или это админ
    post.user.username == user.username or user.is_superuser
    """
    result = post.user.username == user.username or user.is_superuser
    return result

@register.filter(name='times')
def times(number, start=0):
    return range(start, number+start)

@register.filter(name='has_perm')
def has_perm(user, perm_name):
    result = user.has_perm(perm_name)
    return result

