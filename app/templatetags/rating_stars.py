from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def rating_stars(rating):
    full_stars = int(rating)
    half_star = 1 if rating % 1 >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star
    stars_html = full_stars * '<i class="bi bi-star-fill"></i>' + \
                 half_star * '<i class="bi bi-star-half"></i>' + \
                 empty_stars * '<i class="bi bi-star"></i>'
    return mark_safe(stars_html)
