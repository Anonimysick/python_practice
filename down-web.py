##########################
# Скачивание web-страниц #
##########################

from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')

s = str(html)

print(s)
