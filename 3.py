student = {
    'name':'john',
    'age':28,
    'major':'it',
    'gpa':5.7
}
print(student)

print(student['name'])
print(student['major'])
student['gpa'] =5.8
print(student)
student['university'] = 'kop'
del student['age']
print(student)

print('major' in student)
print('age' in student)
print(len(student))

keys = student.keys()
print(keys)
values = student.values()
print(values)

for key,value in student.items():
    print(key,":",value)

student.clear()
print(student)
