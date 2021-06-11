from django import template
from news.models import News


register = template.Library()


@register.inclusion_tag('news/inc/top_question.html')
def get_top_question():
    news = News.objects.all().order_by('-view')[:6]
    return {'news': news}
