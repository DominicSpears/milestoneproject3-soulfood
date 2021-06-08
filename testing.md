### Bugs Discovered
#### Solved Bugs

1. Ingredients list/ method
  * When adding a recipe, I needed to add a list of ingredients and a method list.
  Each list needed to have a way to add or remove an item. When I originally used a 
  javascript funtion to achieve this, it would return a blank array to the database. 
  * To solve this I altered the python code to request.form.getlist, enabling the 
  complete list of ingreinent/method steps to appear.

2. Reicpe list 
  * When I first created a set of recipes, only 1 would appear on the recipe page. 
  It would not itterate through the loop and show all recipes in the database. 
  * To solve this I found a discrepancy in the name of the database that the loop 
  was searching. Instead of being named recipes, I had called it recipe. By adding 
  the s it was able to search the database successfully.

3. User access to site maintenance
  * Users had access to the management section of the site, where an admin can 
  add/edit/delete cuisines and users.
  * To solve this I added a conditional startement to the navbar, only allowing 
  administrators to access the pages at all.

4. Modal pop up windows
  * The modal pop up window to confirm an action would not appear.
  * To solve this I added the initialsation jquery code inside the document.ready 
  function.

#### Remaining Bugs

1. Edit recipe ingredients/ method
  *  While editing a recipe, the instructions list add button will 
    add as many input fields as are already pressent. All of these input 
    fields must be filled or all removed. The same occurance happens for 
    the method input.

2. is_admin status
  *  I cuurently have one admin user whose access is based on the 
    username "admin". I have tried to add an extra field to each user 
    (is_admin) which can be either on or off. this would be how access 
    to parts of the site would be based. However, the field will not work.

3. Edit user password
  * When editing user details I would like to leave the password unchanged. 
  But when te update has been confirmed, the password comes back as either 
  null or blank. 

4. Delete confirmation modals
  * Each delete confirmation modal does not target the correct item. The 
  first item (e.g. card) on the page, located in the top left corner, is 
  deleted instead.
  
### Manual Testing

1. Start Game
  *Click start game on screen
  * Closes start modal and begins countdown timer
  * Result: pass

### Validator Tests
#### All html Pages
  * W3C HTML Validator - Other than errors due to jinja syntax, no issues.

#### style.css
  * W3C CSS Validator - Congratulations, no error found!

#### script.js
  * JSHint Code Tester - There are 7 functions in this file. No warnings or undefined variables.

#### app.py
  * PEP8 Python Validator - All right.

### User Story Tests

#### Experienced with console gaming:
Experienced with PC Gaming
1. As an experianced gamer, I want in-depth instructions to explain game mechanics.
  * To address this I added extra sections to the instruction modal with difficulty and reset explained.
  * ![User Story 1](assets/userstory/us1.png)

