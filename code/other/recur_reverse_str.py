def reverse(s):
    if not s:
        return ''
    else:
        return reverse(s[1:]) + s[0]

r_s = reverse('hello')
print(r_s)