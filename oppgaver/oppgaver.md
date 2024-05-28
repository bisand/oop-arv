# Oppgaver - Arv

### Oppgave 1: Enkel Arv

#### Beskrivelse:
Lag en baseklasse `Person` som har attributtene `name` og `age`, samt en metode `introduce` som skriver ut en introduksjon av personen. Lag deretter en underklasse `Student` som arver fra `Person` og legger til et nytt attributt `student_id` og en metode `study` som skriver ut at studenten studerer.

#### Krav:
1. `Person`-klassen skal ha en `__init__`-metode som initialiserer `name` og `age`.
2. `Person`-klassen skal ha en metode `introduce` som skriver ut "Hi, my name is [name] and I am [age] years old."
3. `Student`-klassen skal arve fra `Person` og ha en `__init__`-metode som initialiserer `name`, `age`, og `student_id`.
4. `Student`-klassen skal ha en metode `study` som skriver ut "[name] is studying."

### Oppgave 2: Metodeoverstyring

#### Beskrivelse:
Lag en baseklasse `Animal` med en metode `make_sound` som skriver ut "Some generic sound". Lag to underklasser `Dog` og `Cat` som overstyrer `make_sound`-metoden for å skrive ut respektive dyrelyder.

#### Krav:
1. `Animal`-klassen skal ha en metode `make_sound` som skriver ut "Some generic sound."
2. `Dog`-klassen skal arve fra `Animal` og overstyre `make_sound`-metoden til å skrive ut "Woof!".
3. `Cat`-klassen skal arve fra `Animal` og overstyre `make_sound`-metoden til å skrive ut "Meow!".

### Oppgave 3: Flerskiktsarv

#### Beskrivelse:
Lag en baseklasse `Vehicle` som har attributtene `make` og `model`, og en metode `display_info` som skriver ut informasjon om kjøretøyet. Lag en underklasse `Car` som legger til et attributt `num_doors`, og en metode `display_info` som overstyrer `Vehicle`'s `display_info` for å inkludere antall dører. Lag deretter en underklasse `ElectricCar` som legger til et attributt `battery_range`, og en metode `display_info` som overstyrer `Car`'s `display_info` for å inkludere batterirekkevidden.

#### Krav:
1. `Vehicle`-klassen skal ha en `__init__`-metode som initialiserer `make` og `model`, og en metode `display_info` som skriver ut "Make: [make], Model: [model]".
2. `Car`-klassen skal arve fra `Vehicle`, ha en `__init__`-metode som initialiserer `make`, `model`, og `num_doors`, og overstyre `display_info` for å inkludere antall dører.
3. `ElectricCar`-klassen skal arve fra `Car`, ha en `__init__`-metode som initialiserer `make`, `model`, `num_doors`, og `battery_range`, og overstyre `display_info` for å inkludere batterirekkevidden.

Disse oppgavene gir praktiske erfaringer med arv, inkludert hvordan man oppretter underklasser, overstyrer metoder og implementerer flerskiktsarv.