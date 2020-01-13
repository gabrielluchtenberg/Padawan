def adicionar_html(html, i):
    return "<%s>%s</%s>" % (html, i, html)


print(adicionar_html('html', 'Gabriel'))