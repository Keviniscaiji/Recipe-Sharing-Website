# Team 14 - Recipe Website Project

### How to use the website:
First of all, non logged-in users will come to an index interface, where there are recipes uploaded by people before. Click the orange title of the recipe to jump to the details of these recipes. You can also search the menu you want with keywords, such as "pizza". The software also allows you to arrange recipes in a certain order, including chronological order from new to old, positive or reverse alphabetic order. The user can also select login account or registered account. Click login account, the user can enter his user name and password. The system will jump to the profile interface. In this interface, you can change your personal information, including birthday, gender and country (non required items). You can also upload your favorite avatar, preferably a square picture, otherwise the proportion will be distorted. If you haven't uploaded your avatar, the system will give you a default avatar, which is also a link to your profile interface. You can also click post to write your own recipe, including a title and text section. Logged-in users with different identities will see different navigation bars. The navigation bar of non logged-in users does not log out, profile and post. The navigation bar of logged-in users does not login and register, which is convenient for users.

### Overall Description:
The website allows registered users to create a recipe for a dish. The user can be able to specify ingredients required for a dish, and also upload photos/images about the dish. The user can be able to categorise the recipe (e.g., Italian, French, Chinese, Indian, Irish, etc.) and then search for recipes matching a particular category. The user can be able to create their categories themselves, i.e., one user may create categories about Chinese dishes, and another user may create categories about Italian dishes, etc. A user can be able to categorise their recipes only by the categories they have created. An unregistered user can be able to only view recipes, by selecting all the categories available in the system. 

### Milestone 1:
*  `Upload/Update Avatar Function`: Allow users to upload their own avatar and display it in the index. Click the avatar to jump to the profile interface. If users do not set their own avatar, the system will set a default avatar for users.
* `Login/Register Function`: Allow users to register accounts and login through their accounts and passwords.
* `Upload/Update resumes Function`: Users who register accounts can upload or change their resumes.
* `Relevant Function about Menu`: Users can click the menu link and view the details of the menu.
* `Post Recipes Function`: Users with registered accounts can write their own proprietary recipes and display their past recipes and release time.
* `View Recipes Function`: Registered users and unregistered users can see the recipes published by other users, the user name of the user publishing the recipes, and the time of publishing the recipes.
* `Search Function`: Users can search recipes published by others according to keywords.
* `CSS`: Set the CSS design for these existing interface.
* `Order Function`: Allows the user to select a certain sorting method to arrange the recipes on the main interface in a certain order.

### Milestone 2:

* `Enhanced user interaction `: The interaction between users and UI is enhanced. For example, in the post interface, the user input box will turn gray, and there is a red word count in the position of post body. When the user enters the password, mailbox and user name during registration, if the input does not meet the specification, the font will turn red and the reason for the non-compliance will be displayed on the right synchronously
* `Log-file Function`: A folder called logfile is established to save log file. Three log files are used to save debug, info and error information respectively.
* `UI Choice Function`: User can switch between light mode and dark mode through the buttons on the navigation bar. Through Ajax and session, users can also keep selected style when switching between different pages.
* `Database manage system`:  manager can enter "manager" for user name and "manager" for password in login interface  to enter the manager system, in the interface, user can choose which user or dish to remove, they can also remove all the users or dishes from the database by clicking the button remove all dishes or remove all users.
* `Add Picture for Dish Function`: Users can add a picture for each post, and the picture and the content of the post will be displayed in the index interface
* `Like Function`: Allow users to like their favorite dishes and record the amount of likes. In the interface of the main menu, users can arrange the dishes from high to low according to the number of like
* `Strict Inspection`: A large number of validators are added. In the login interface, registration interface and post interface, if the user inputs incorrectly, the system has an alert window to list all the places where the user's input does not meet the requirements. For example, user who login in fail will be informed whether they enter the wrong username or password.

