# Week 3 - Inheritance

## Assignment Details

For this exercise, we want you to code a generic superclass and at least three subclasses of that superclass, each class needs to have at least 2 attributes and 2 methods. It’s easiest to simply describe a real-world object in this manner. You need to provide a test method that shows your classes in operation.

## Assignment Submission

- LeaveManagement.py : Class files
- driver.py: Testing Leave Management classes
- helpers.py: functions for formatting print out
- test.py: Unit tests for each of the classes

# Week 3 - Inheritance 2

## Assignment Details and Answers

```
class Spell:
  def __init__(self, incantation, name):
    self.name = name
    self.incantation = incantation

  def __str__(self):
    return self.name + ’ ’ + self.incantation + ’\n’ + self.get_description()

  def get_description(self):
    return 'No description'

  def execute(self):
    print self.incantation

class Accio(Spell):
  def __init__(self):
    Spell.__init__(self, ’Accio’, ’Summoning Charm’)

class Confundo(Spell):
  def __init__(self):
    Spell.__init__(self, ’Confundo’, ’Confundus Charm’)

  def get_description(self):
    return ’Causes the victim to become confused and befuddled.’

def study_spell(spell):
  print spell

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
```

Answer the following questions:

1.  What are the parent and child classes here?

    - Parent class is `Spell`. The child classes are `Accio` and `Confundo`.

2.  What are the base and sub-classes?

    - Base class is `Spell` and the sub-classes are `Accio` and `Confundo`.

3.  What is the output from this code? Try without running if you can

    - Errors, because curly quotes are not used in programming, and the print statements will not work in Python 3 as Python 3 requires parenthesis.
    - Assuming the curly quotes exist because of limitations of the CMS and the code was formatted for Python 3 the output would be as follows:

             Accio
             Summoning Charm Accio
             No description
             Confundus Charm Confundo
             Causes the victim to become confused and befuddled.

4) When study_spell(Confundo()) executes...what get_description method gets called and why?

   - The `get_description` from the `Confundo` class gets called

   TODO answer why

5) The statement print Accio() needs to print ‘This charm summons an object to the caster, potentially over a significant distance’)? Write down the code that we need to add and/or change

   ```python

   class Accio(Spell):
       def __init__(self):
           Spell.__init__(self, 'Accio', 'Summoning Charm')

       # added code needed to print the description
       def get_description(self):
           return 'This charm summons an object to the caster, potentially over a significant distance'
   ```
