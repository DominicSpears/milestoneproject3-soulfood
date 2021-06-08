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

5. Search recipes
  * After seaching through the recipes, the page would reset at the top, meaning 
  that the user needed to scroll dow to see their search results.
  * To solve this I created a dedicated recipe page with the searchbar at the top
  of the page.

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

### Validator Tests
#### All html Pages
  * W3C HTML Validator - Other than errors due to jinja syntax, no issues.

#### style.css
  * W3C CSS Validator - Congratulations, no error found!

#### script.js
  * JSHint Code Tester - There are 7 functions in this file. No warnings or undefined variables.

#### app.py
  * PEP8 Python Validator - All right.

### Manual Testing

1. Register
  * New users add a username and password to the input fields
  * Username and password(hashed) saved in the database, user lgged in to site
  * Result: pass

2. Existing user button
  * User with existing details clicks login button at the bottom of the page
  * User taken to login page to sign in
  * Result: pass

3. Register flash message
  * New users adds a username and password and confirms the register
  * Message of successful registry flashes up
  * Result: pass
  
4. Login
  * Existing users add a username and password to the input fields
  * User logged into site, to the profile page
  * Result: pass

5. New user button
  * New user clicks register account button at the bottom of the page
  * User taken to register page to register
  * Result: pass

6. Login flash message
  * User adds a username and password and confirms login
  * Message of successful login flashes up
  * Result: pass

7. Navbar
  * Click on each button in the bar
  * Takes the user to the appropriate page
  * Result: pass

8. Restricted navbar access (logged out)
  * When logged out, the user cannot access all pages/buttons
  * Only home, cookare, recipes, login and register available
  * Result: pass

9. Restricted navbar access (user logged in)
  * When logged in, the user cannot access all pages/buttons
  * Only home, cookare, recipes, add recipe, profile ad log out available
  * Result: pass

10. Unrestricted navbar access (Admin logged in)
  * When logged in, the administrator can access all pages/buttons
  * All pages/buttons available e.g. manage
  * Result: pass

11. Footer
  * Click social media buttons
  * Each button creates a new tab with the appropriate website
  * Result: pass

12. Homepage
  * Click any of the website feature links
  * The corresponding page appears
  * Result: pass

13. Homepage profile button
  * When logged in, the button will take you to you profile page
  * When logged out, the button will take you to the login page
  * Result: pass

14. Cookware
  * Display all cookware items present in the database
  * Result: pass

15. Add cookware
  * Click button (available to admin) to bring up the add cookware page
  * Input all required fields and confirm to add an item to the database
  * Click cancel to stop and return to cookware page
  * Result: pass

16. Recipes
  * Display all recipes present in the database
  * Result: pass

17. Recipe search
  * Enter enquiry into the search bar and click search button
  * Shows recipes based on recipe name or cuisine name
  * Result: pass

18. Recipe search reset
  * Click on the reset button in the search bar
  * Shows all recipes in the database
  * Result: pass

19. View recipe 
  * Click full recipe button  
  * Reveals dedicated recipe page
  * Result: pass

20. Recipe Page
  * Shows information about the selected recipe
  * Vegetarian/vegan/spicy indicators differ depending on the status of that feature
  * Result: pass

21. Add recipe 
  * Input fields are all required
  * Cuisine dropdown active, contains all cuisines in the database 
  * Can add or remove items to the ingregients/method sections
  * Click add recipe to confirm
  * Click cancel to return to recipe page
  * Result: pass

22. Profile page 
  * Shows all recipes created by the user
  * If user is admin, all recipes are shown 
  * Full recipe button links to dedicated page
  * Edit button links to edit recipe page
  * Delete button removes recipe from database
  * Result: pass

23. Edit recipe 
  * Input fields fill with current information about the recipe
  * Click edit recipe button confirms changes
  * Click cancel button to return to profile page
  * Result: pass

24. Cuisines
  * Display all cuisines present in the database
  * Click edit reveals edit cuisine page
  * Click delete to remove cuisine from database
  * Result: pass

25. Add cuisine
  * Click button to bring up the add cuisine page
  * Input all required fields and confirm to add an item to the database
  * Click cancel to stop and return to cuisine page
  * Result: pass

26. Edit cuisine 
  * Input field fills with current information about the cuisine
  * Click edit cuisine button confirms changes
  * Click cancel button to return to cuisine page
  * Result: pass

27. Users
  * Display all users present in the database
  * Click edit reveals edit user page
  * Click delete to remove user from database
  * Result: pass

28. Edit user 
  * Input fields fill with current information about the user
  * Click edit user button confirms changes
  * Click cancel button to return to user page
  * Result: pass

29. Log out 
  * Click log out button
  * Return user to log in page
  * Removes user from session cookie
  * Result: pass

### User Story Tests
#### Experienced with console gaming:
Experienced with PC Gaming
1. As an experianced gamer, I want in-depth instructions to explain game mechanics.
  * To address this I added extra sections to the instruction modal with difficulty and reset explained.
  * ![User Story 1](assets/userstory/us1.png)