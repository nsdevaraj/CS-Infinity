


## 1. Flyweight Pattern

**Purpose:** Optimize memory usage by sharing common data among multiple objects.

**Real-World Analogy:** Consider a document editor displaying thousands of characters. Instead of storing each character's font and style repeatedly, the editor stores this information once and references it for each character.

**Structure:**

- **Flyweight:** Stores intrinsic (shared) state.
    
- **FlyweightFactory:** Creates and manages Flyweight objects.
    
- **Client:** Maintains references to Flyweight objects and stores extrinsic (unique) state.
    

**Example in Python:**

```python
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]

class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

# Usage
pine = TreeFactory.get_tree_type("Pine", "Green", "Rough")
tree1 = Tree(10, 20, pine)
tree2 = Tree(30, 40, pine)
```

**Key Takeaway:** By sharing common data, we significantly reduce memory consumption, which is crucial in applications like game development where numerous similar objects exist.

---

## 2. Specification Pattern

**Purpose:** Encapsulate business rules into reusable and combinable specifications.

**Real-World Analogy:** In an e-commerce platform, products may have various eligibility criteria (age restriction, location, membership status). Instead of hardcoding these rules, we define them as separate specifications.

**Structure:**

- **Specification:** Interface with a method `is_satisfied_by`.
    
- **ConcreteSpecifications:** Implement the `is_satisfied_by` method.
    
- **CompositeSpecifications:** Combine specifications using logical operations like AND, OR, NOT.
    

**Example in Python:**

```python
class Specification:
    def is_satisfied_by(self, candidate):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)

    def __neg__(self):
        return NotSpecification(self)

class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate):
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class IsAdultSpecification(Specification):
    def is_satisfied_by(self, candidate):
        return candidate.age >= 18

class IsFromUSSpecification(Specification):
    def is_satisfied_by(self, candidate):
        return candidate.country == "US"

# Usage
user = User(age=20, country="US")
spec = IsAdultSpecification() & IsFromUSSpecification()
print(spec.is_satisfied_by(user))  # Output: True
```

**Key Takeaway:** The Specification Pattern promotes flexibility and maintainability by allowing business rules to be defined, combined, and reused independently.

---

## 3. Memento Pattern

**Purpose:** Capture and restore an object's internal state without violating encapsulation.

**Real-World Analogy:** In a text editor, the undo functionality allows users to revert to previous states of the document.

**Structure:**

- **Originator:** The object whose state needs to be saved.
    
- **Memento:** Stores the state of the Originator.
    
- **Caretaker:** Manages the history of Mementos.
    

**Example in Python:**

```python
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content += text

    def save(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.get_state()

# Usage
editor = TextEditor()
editor.write("Hello, ")
saved = editor.save()
editor.write("World!")
print(editor._content)  # Output: Hello, World!
editor.restore(saved)
print(editor._content)  # Output: Hello, 
```

**Key Takeaway:** The Memento Pattern is essential for implementing features like undo/redo, allowing state restoration without exposing internal object details.

---

## 4. State Pattern

**Purpose:** Allow an object to alter its behavior when its internal state changes.

**Real-World Analogy:** A media player can be in different states like playing, paused, or stopped, each with distinct behaviors.

**Structure:**

- **State:** Interface defining behavior for each state.
    
- **ConcreteStates:** Implement behaviors for specific states.
    
- **Context:** Maintains an instance of a ConcreteState and delegates behavior to it.
    

**Example in Python:**

```python
class State:
    def play(self, player):
        pass

    def pause(self, player):
        pass

    def stop(self, player):
        pass

class PlayingState(State):
    def pause(self, player):
        print("Pausing...")
        player.change_state(PausedState())

class PausedState(State):
    def play(self, player):
        print("Resuming...")
        player.change_state(PlayingState())

class StoppedState(State):
    def play(self, player):
        print("Playing...")
        player.change_state(PlayingState())

class MediaPlayer:
    def __init__(self):
        self.state = StoppedState()

    def change_state(self, state):
        self.state = state

    def play(self):
        self.state.play(self)

    def pause(self):
        self.state.pause(self)

    def stop(self):
        self.state.stop(self)

# Usage
player = MediaPlayer()
player.play()   # Output: Playing...
player.pause()  # Output: Pausing...
player.play()   # Output: Resuming...
```

**Key Takeaway:** The State Pattern simplifies complex conditional logic by encapsulating state-specific behaviors, making the code more maintainable and scalable.

---

## 5. Event Sourcing Pattern

**Purpose:** Persist the state of a system as a sequence of events, allowing reconstruction of past states.

**Real-World Analogy:** In banking systems, every transaction (deposit, withdrawal) is recorded as an event, enabling the reconstruction of account balances at any point in time.

**Structure:**

- **Event:** Represents a change in state.
    
- **Aggregate:** Applies events to maintain current state.
    
- **Event Store:** Stores all events.
    

**Example in Python:**

```python
class Event:
    def apply(self, balance):
        pass

class Deposit(Event):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, balance):
        return balance + self.amount

class Withdraw(Event):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, balance):
        return balance - self.amount

class BankAccount:
    def __init__(self):
        self.events = []

    def deposit(self, amount):
        self.events.append(Deposit(amount))

    def withdraw(self, amount):
        self.events.append(Withdraw(amount))

    def get_balance(self):
        balance = 0
        for event in self.events:
            balance = event.apply(balance)
        return balance

# Usage
account = BankAccount()
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 300
```

**Key Takeaway:** Event Sourcing provides a robust mechanism for auditing and reconstructing system states, essential in domains requiring high data integrity.


---

# 5 Advanced Design Patterns for Scalable and Maintainable Code

Most junior engineers focus on getting their code to work. Experienced engineers, however, think about **efficiency**, **scalability**, and **long-term maintainability**.

Today we are diving into **five advanced design patterns** — used in industries like gaming, e-commerce, and banking — but often skipped in tutorials.

---

## 1. Flyweight Pattern

**Problem:**  
How do video games render thousands of trees without crashing the computer?

**Naïve Approach:**

```plaintext
Each tree = 50 KB → 1 million trees = 50 GB RAM (not scalable!)
```


![[_imgs/Pasted image 20250429053855.png]]


![[_imgs/Pasted image 20250429055150.png]]



**Solution:**  
Share common data between similar objects.

### Structure:

- **TreeType**: stores shared data like type, color, texture.
    
- **TreeFactory**: reuses or creates new TreeTypes.
    
- **Tree**: stores only a reference to TreeType and position.
    

### Example Code (Python):

```python
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

class TreeFactory:
    tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls.tree_types:
            cls.tree_types[key] = TreeType(name, color, texture)
        return cls.tree_types[key]

class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.type = tree_type

# Usage
pine_tree = TreeFactory.get_tree_type("Pine", "Green", "Rough")
tree = Tree(10, 20, pine_tree)
```

✅ **Saves memory** by reusing shared data.

---

## 2. Specification Pattern

**Problem:**  
Handling dynamic and complex filtering conditions without messy `if-else` blocks.

**Solution:**  
Turn rules into **reusable and combinable objects**.


![[_imgs/Pasted image 20250429054422.png]]


![[_imgs/Pasted image 20250429054707.png]]


![[_imgs/Pasted image 20250429054720.png]]


![[_imgs/Pasted image 20250429055103.png]]



### Structure:

- **Specification Interface**: defines a `is_satisfied_by` method.
    
- **Concrete Specifications**: age, location, premium membership checks.
    
- **Combinators**: `AND`, `OR`, `NOT`.
    

### Example Code (Python):

```python
class Specification:
    def is_satisfied_by(self, candidate):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)

    def __neg__(self):
        return NotSpecification(self)

class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate):
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class IsAdultSpecification(Specification):
    def is_satisfied_by(self, candidate):
        return candidate.age >= 18

class IsFromUSSpecification(Specification):
    def is_satisfied_by(self, candidate):
        return candidate.country == "US"

# Example User
class User:
    def __init__(self, age, country):
        self.age = age
        self.country = country

user = User(20, "US")
spec = IsAdultSpecification() & IsFromUSSpecification()
print(spec.is_satisfied_by(user))  # True
```

✅ **Flexible** and **extensible** for future business logic.

---

## 3. Memento Pattern

**Problem:**  
How to **undo** changes and **restore** previous states.

**Solution:**  
Capture and store the object’s state without violating encapsulation.



![[_imgs/Pasted image 20250429054452.png]]

![[_imgs/Pasted image 20250429054800.png]]


![[_imgs/Pasted image 20250429055112.png]]


### Structure:

- **Originator**: the object (like a TextEditor) whose state we save.
    
- **Memento**: stores the snapshot.
    
- **Caretaker**: keeps track of saved states.
    

### Example Code (Python):

```python
class Memento:
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state

class TextEditor:
    def __init__(self):
        self._content = ""

    def type(self, words):
        self._content += words

    def save(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.get_saved_state()

    def get_content(self):
        return self._content

# Usage
editor = TextEditor()
editor.type("Hello, ")
saved = editor.save()
editor.type("world!")
print(editor.get_content())  # Hello, world!

editor.restore(saved)
print(editor.get_content())  # Hello, 
```

✅ **Supports Undo** without exposing internal structure.

---

## 4. State Pattern

**Problem:**  
Changing behavior based on object's internal state without messy `if-else`.

**Solution:**  
Encapsulate state-specific behaviors into separate classes.


![[_imgs/Pasted image 20250429054916.png]]


![[_imgs/Pasted image 20250429054946.png]]



![[_imgs/Pasted image 20250429055125.png]]


### Structure:

- **State Interface**: defines actions like `play()`, `pause()`, `stop()`.
    
- **Concrete States**: PlayingState, PausedState, StoppedState.
    
- **Context (Player)**: delegates behavior to the current state.
    

### Example Code (Python):

```python
class State:
    def play(self, player):
        pass

    def pause(self, player):
        pass

    def stop(self, player):
        pass

class PlayingState(State):
    def pause(self, player):
        print("Pausing...")
        player.change_state(PausedState())

class PausedState(State):
    def play(self, player):
        print("Resuming...")
        player.change_state(PlayingState())

class Player:
    def __init__(self):
        self.state = StoppedState()

    def change_state(self, state):
        self.state = state

    def play(self):
        self.state.play(self)

    def pause(self):
        self.state.pause(self)

class StoppedState(State):
    def play(self, player):
        print("Playing...")
        player.change_state(PlayingState())

# Usage
player = Player()
player.play()   # Playing...
player.pause()  # Pausing...
player.play()   # Resuming...
```

✅ **Clean code** with easy addition of new states.

---

## 5. Event Sourcing Pattern

**Problem:**  
How do banks track every single transaction **without losing any data**?

**Solution:**  
Store **immutable events**, not the current state. Rebuild the state by replaying events.


![[_imgs/Pasted image 20250429054151.png]]


![[_imgs/Pasted image 20250429054626.png]]

### Structure:

- **Event Interface**: defines an `apply` method.
    
- **Concrete Events**: DepositEvent, WithdrawEvent.
    
- **Aggregate (Account)**: processes and stores events.
    

### Example Code (Python):

```python
class Event:
    def apply(self, balance):
        pass

class Deposit(Event):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, balance):
        return balance + self.amount

class Withdraw(Event):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, balance):
        return balance - self.amount

class BankAccount:
    def __init__(self):
        self.events = []

    def deposit(self, amount):
        self.events.append(Deposit(amount))

    def withdraw(self, amount):
        self.events.append(Withdraw(amount))

    def get_balance(self):
        balance = 0
        for event in self.events:
            balance = event.apply(balance)
        return balance

# Usage
account = BankAccount()
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # 300
```

✅ **Full audit trail** and **no data loss**.

---

# Conclusion

|Pattern|Use Case|
|---|---|
|Flyweight|Efficient memory usage for similar objects|
|Specification|Dynamic and composable business rules|
|Memento|Undo/Redo functionality|
|State|Behavior based on object's state|
|Event Sourcing|Immutable history and audit trails|

---



referred {

https://youtu.be/P5H9t2EpEg4?si=ei7cq67aATj4TkUu


}