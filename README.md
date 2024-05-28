# Objektorientert Programmering

## Arv

Arv (engelsk: Inheritance) er et grunnleggende prinsipp i objektorientert programmering (OOP) som muliggjør at en klasse kan arve egenskaper (som metoder og variabler) fra en annen klasse.
Dette konseptet er sentralt for å skape en hierarkisk klassifisering av klasser, og det bidrar til kodegjenbruk og en mer organisert og forståelig struktur i programmer.

### Praktisk eksempel på bruk av arv
___
`Eksempel: Person -> Student, Person -> Teacher `
```python
class Person:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, student_id: str, major: str):
        super().__init__(first_name, last_name, age, gender)
        self.student_id = student_id
        self.major = major

    def vis_info(self):
        return f"Student: {self.first_name} {self.last_name}, Alder: {self.age}, Kjønn: {self.gender}, ID: {self.student_id}, Studieretning: {self.major}"

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, employee_id: str, department: str):
        super().__init__(first_name, last_name, age, gender)
        self.employee_id = employee_id
        self.department = department

    def vis_info(self):
        return f"Lærer: {self.first_name} {self.last_name}, Alder: {self.age}, Kjønn: {self.gender}, ID: {self.employee_id}, Avdeling: {self.department}"

# Eksempel på bruk
student = Student("Alice", "Larsen", 20, "Kvinne", "S12345", "Datavitenskap")
teacher = Teacher("Bob", "Johansen", 45, "Mann", "T67890", "Matematikk")

print(student.vis_info())
print(teacher.vis_info())

```

### Oppgaver

Oppgaver nedenfor er ment for å gi deg en forståelse av hvordan klasser og objekter fungerer. Disse skal leveres innen neste forelesning. Arbeidskravet vil bestå av å få godkjent minst 2 av oppgavene. Det er ønskelig at dere leverer så mange som mulig, men det er ikke et krav.

Klikk [her](oppgaver/oppgaver.md) for å se oppgaver ([PDF](oppgaver/oppgaver.pdf)).
