from Document import Document
from Character import Character

d = Document()
d.insert('as')
d.insert('a')
d.delete()
d.delete()
d.insert('a')
d.save()
d.cursor.forward()
d.cursor.forward()
d.cursor.back()
d.cursor.back()
d.insert(Character('w', underline=True))
d.insert(Character('was', underline=True))
print(d.string)
