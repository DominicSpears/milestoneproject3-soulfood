### Bugs Discovered

#### Solved Bugs

1. Time remaining
  * The time remaining would temporarily show the incorrect figure before starting the countdown. 
  * To solve this I altered the initial value in the html code to the start timer value.

#### Remaining Bugs

1. Audio restart
  * The background music restarts when the (instruction modal) return button is clicked. It would be better for the music to continue over multiple games. 

### Manual Testing

1. Start Game
  *Click start game on screen
  * Closes start modal and begins countdown timer
  * Result: pass

### Validator Tests

#### index.html
  * W3C HTML Validator - 
  * Chrome Lighthouse - 100, 100, 100, 89.
  * ![Lighthouse assessment](assets/images/indexhtml.png)

#### style.css
  * W3C CSS Validator - 

#### index2.js
  * JSHint Code Tester - 

#### app.py
  * PEP8 Python Validator - 

### User Story Tests

#### Experienced with console gaming:
Experienced with PC Gaming
1. As an experianced gamer, I want in-depth instructions to explain game mechanics.
  * To address this I added extra sections to the instruction modal with difficulty and reset explained.
  * ![User Story 1](assets/userstory/us1.png)
