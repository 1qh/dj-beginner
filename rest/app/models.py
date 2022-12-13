from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LANG = sorted(
    set(
        [
            (i[1][0], i[0])
            for i in get_all_lexers()
            if i[1] and '+' not in i[1][0] and ' ' not in i[0] and '-' not in i[0]
        ]
    )
)
STYLE = sorted([(i, i) for i in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=True, default='')
    code = models.TextField()
    line = models.BooleanField(default=True)
    lang = models.CharField(choices=LANG, default='python', max_length=50)
    style = models.CharField(choices=STYLE, default='monokai', max_length=50)
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE
    )
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.lang)
        line = 'table' if self.line else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, line=line, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created']
