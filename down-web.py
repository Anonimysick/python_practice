##########################
# Скачивание web-страниц #
##########################

from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')

s = str(html)
s.split(" ")
# print(s)
# print('**************************************************************')

for i in s:
    print(i)


# state = 0
# ans = []
# for c in s:
#     if c == "<code>":
#         state = 1
#     if c == "/<code>":
#         state = 0
#     elif state == 0:
#         ans.append(c)
#
# s = ''.join(ans)
#
# print(s)
