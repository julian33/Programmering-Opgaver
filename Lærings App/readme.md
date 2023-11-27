# Matematik Lærings App
I Dette projekt har jeg skulle programmere en lærings app som var bygget op om et designmønster.
Den læringsapp som jeg har valgt at lave, fokuserer på folkeskole matematik emner ca. 5 klasses niveau som Addition, subtraktion, mulitplikation, division. Og i min udvikling af appen har jeg brugt "Factory Method" til at opbygge funktioner med.

## Udviklingsprocess
Jeg startede med at brainstorm lidt ideer om hvad jeg vil lave, men endte bare med at vælge folkeskolematematik. Inde for folkeskolematematik tænkte jeg at jeg gærne vil have de 4 basale regneformer: Addition, subtraktion, mulitplikation, division.
Med den ide begyndt jeg at sætte noget simpel tkinter UI op og få nogen knappet til at kunne printe ting og finde ud af hvordan jeg fjernede knapperne igen.
Efter jeg havde fundet ud af det basale tkinter satte jeg nogen knappet op med matematikemnerne ved hjælp af "actory Method" og fik dem til at gå til åbne hver deres sprøgsmål alt efter valgte emne.
Tilsidst programerede jeg at man kunne svare på spørgsmålene og hvis man svarede rigtigt sagede programmet: ```"Rigtigt!"``` og hvis det var forkert: ```"Forkert! Det rigtige svar var {correct_answer}"```
Derefter ville programmet komme med 4 nye svar inde for det samme emne.

## Flowchart Over Brugergrænseflade
Min app virker ved at man først starter den, så får man mulighederne for at  vælge imellem Addition, subtraktion, mulitplikation, division og  man får også vedvarende muligheder for at kunne slukke, minimere og maksimere appen( Dog skalere UI'et ikke ved maksimereing og minimering).
Hvis man vælger en af de matematiske emner får man tildelt et spørgsmål og 4 svarmuligheder. hvis man trykker på det rigtige svar får man det at vide og man får igen 4 nye spørgsmål og ligeledes hvis man svarer forkert.
Læg mærke til at divisions stykkerne er afrundet til nærmeste heltal.
```mermaid
graph LR;
    A[Tænd Appen] --> B[Vælg Addering];
    A --> C[Vælg Subtraktion];
    A --> D[Vælg Multiplikation];
    A --> E[Vælg Division];

    A --> F[Sluk Knap];

    B --> G[1 Spørgsmål og\n 4 Svar Muligheder\n Tildeles]
    C --> G;
    D --> G;
    E --> G;

    G --> H[Svar Rigtit];
    G --> I[Svar Forkert];

    H --> G;
    I --> G;

```
![image](https://github.com/julian33/Programmering-Opgaver/assets/12980973/195fa763-c5d0-41bf-81c3-b80fe0e4dfbf)

## Design Patterns
Mit valgte designpattern har været "Factory Method". Denne metoder har været god til at splitte et stort kompliceret emne ned i mindre bider som nemt kan vedligeholdes i tilfælde af fremtidige brugerkrav som skal implementeres.
Herunder er det vist hvordan jeg har implementeret "Factory Method" Til at opsplitte: Addition, subtraktion, mulitplikation, division

```python
# Klasse til at generere spørgsmål
class QuestionFactory:
    def generate_question(self):
        num1, num2 = self.generate_numbers()
        question, answer = self.create_question(num1, num2)
        return question, answer

    def generate_numbers(self):
        return random.randint(-10, 10), random.randint(-10, 10)

    def create_question(self, num1, num2):
        raise NotImplementedError("Subclasses must implement create_question method")

# Underklasse til addition
class AdditionFactory(QuestionFactory):
    def create_question(self, num1, num2):
        question = f"What is {num1} + {num2}?"
        answer = num1 + num2
        return question, answer

# Underklasse til subtraktion  
class SubtractionFactory(QuestionFactory):
    def create_question(self, num1, num2):
        num1, num2 = max(num1, num2), min(num1, num2)
        question = f"What is {num1} - {num2}?"
        answer = num1 - num2
        return question, answer

# Underklasser til multiplikation
class MultiplicationFactory(QuestionFactory):
    def create_question(self, num1, num2):
        question = f"What is {num1} * {num2}?"
        answer = num1 * num2
        return question, answer

# Underklasser til division
class DivisionFactory(QuestionFactory):
    def create_question(self, num1, num2):
        if num2 == 0:
            num1, num2 = self.generate_numbers()
        result = num1 // num2
        question = f"What is {num1} / {num2}?"
        answer = result
        return question, answer
```

## Test Af Program
Til test af program har jeg lavet skema over alle
| Input | Forventet output | Faktisk output |
| a | a | a |
