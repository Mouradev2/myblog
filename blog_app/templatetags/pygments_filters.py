from django import template
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

register = template.Library()


@register.filter(name="highlight")
def highlight_code(value, language):
    lexer = get_lexer_by_name(language, stripall=True)
    formatter = HtmlFormatter(style="default")
    highlighted_code = highlight(value, lexer, formatter)
    return mark_safe(highlighted_code)
