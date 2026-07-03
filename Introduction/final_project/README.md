# MEDITATION WEB PROGRAMMING
    #### Video Demo: https://youtu.be/mqulsbrp1Cc
    #### Description: The video demo showcases the meditation web app’s main features, including the index page, login/register system, and guided video sessions. It highlights the comment section with add/delete functionality, the like/dislike reactions, and the profile page where users can view their own and liked comments. Overall, it demonstrates how the app combines video content with interactive features to create an engaging mindfulness experience.




## Project Overview

This project is a meditation web application built with Flask and SQLite that allows users to explore two main styles of practice: **Normal Meditation** and **Letting Go Meditation**. The app provides a simple interface where visitors can choose the type of meditation they want to experience, access guided sessions in video format, and interact through a comment and reaction system.

The goal of the project is to combine technical learning with personal meaning. Meditation is presented not only as a tool for calming the mind, but also as a way to recognize emotions and release resistance. By integrating login and registration features, each user can create an account, leave comments, react with likes or dislikes, and view their own activity on a profile page. This makes the app both a personal mindfulness tool and a small social space.

From a technical perspective, the project demonstrates the use of Flask templates for page rendering, session management with `flask-session`, password hashing with `werkzeug`, and database operations through the CS50 SQL library. The database stores users, comments, and reactions, ensuring that interactions are persistent and tied to individual accounts. Static files such as CSS, JavaScript, images, and videos provide styling and multimedia support, while the layout template ensures consistency across all pages.

Overall, the meditation web programming project is designed as a practical application of web development concepts learned in CS50, while also reflecting the importance of mental health and mindfulness in everyday life.


### Templates (GENERAL)

The project is organized into several HTML templates that define the structure and behavior of each page in the application.

- **layout.html** serves as the base structure for every page. It provides the common layout elements, such as the header, footer, and links to static files, and makes it possible to interconnect all other templates in a consistent way.
- **index.html** is the main entry point for users. From here, visitors can select between Normal Meditation and Letting Go Meditation. If the user is signed in, this page also displays a profile section that uses JavaScript to show personalized information.
- **aboutme.html** is an extra page where I explain my background and the reasons why I decided to build this project. It connects back to the index page and adds a personal touch to the app.
- **normalmeditation.html** contains the video for the Normal Meditation practice. Below the video, users can leave comments and interact with the reaction system.
- **lettingo.html** is similar in structure but focused on the Letting Go Meditation practice. It shows the video and provides space for comments and reactions.
- **login.html** and **register.html** are templates that display forms for authentication. Depending on the user’s choice, they allow either logging into an existing account or registering a new one.


### App.py

The core of the application is contained in the `app.py` file, which defines the routes, logic, and database interactions for the meditation web app. This file is responsible for rendering all of the main pages, including the index, about me, normal meditation, and letting go meditation pages. Each route connects to its corresponding template and ensures that the correct information is passed to the user interface.

Authentication is handled through dedicated routes for login and registration. The login form allows existing users to access their accounts, while the registration form enables new users to create one. Both forms include validation to ensure that usernames and passwords are submitted correctly, and password hashing is implemented with Werkzeug for security. A logout route is also included, which clears the session and redirects the user back to the home page.

The application uses `flask-session` to manage sessions on the server side, storing user information securely. Database operations are performed with the CS50 SQL library, which connects to a SQLite database. This database stores users, comments, and reactions, making it possible to display personalized content such as a user’s own comments or the comments they have liked.

JavaScript is integrated with the backend to provide dynamic features. For example, users can add or delete comments without refreshing the page, and likes or dislikes are updated instantly in both the interface and the database. These functions are defined in `app.py` and return JSON responses that the frontend can process.

Overall, `app.py` serves as the backbone of the project. It ties together the templates, database, and static files, ensuring that the meditation app runs smoothly and provides an interactive experience for users.


### Database Implementation

The database for this project is built using SQLite and managed through the CS50 SQL library. It consists of three main tables: **users**, **comments**, and **reactions**, each serving a specific purpose in the meditation web app.

The **users** table stores essential account information. Every user has a unique ID, a username, and a hashed password for secure authentication. The use of `AUTOINCREMENT` ensures that each user receives a distinct identifier, while the `UNIQUE` constraint on the username prevents duplicates.

The **comments** table records all user interactions under each meditation video. Each comment includes the user ID, video ID, content, timestamp, and counters for likes and dislikes. The `FOREIGN KEY` linking `user_id` to the `users` table maintains referential integrity, ensuring that every comment belongs to a valid user. Default values for likes and dislikes start at zero, and the timestamp automatically captures when the comment was created.

The **reactions** table manages the like and dislike system. It connects users and comments through foreign keys and includes a `CHECK` constraint that limits reactions to either “like” or “dislike.” The `UNIQUE(user_id, comment_id)` rule ensures that each user can react only once per comment, preventing multiple likes or dislikes from the same account. The `ON DELETE CASCADE` option keeps the database clean by automatically removing reactions if a user or comment is deleted.

Together, these tables form a relational structure that supports user authentication, comment posting, and interactive reactions. This design keeps data consistent, scalable, and easy to query, providing a solid foundation for the app’s dynamic features.

### Features

The meditation web app includes several interactive features that make the experience more personal and engaging for users.

- **Login and Register System:** Users can create an account or log in to an existing one. After signing in, the app displays a personalized welcome message with the user’s name. This authentication system ensures that each user’s activity, such as comments and reactions, is securely linked to their account.

- **Comment Section:** Each meditation video page includes a comment area where users can share thoughts or reflections. Comments are added dynamically using JavaScript and stored in the database through Flask routes. Users can also delete their own comments, with a confirmation prompt to prevent accidental removal. The deletion process uses a fetch request to communicate with the backend, ensuring smooth and immediate updates without reloading the page.

- **Likes and Dislikes:** The app features a reaction system that allows users to express their opinions on comments. Each user can either like or dislike a comment, but only one reaction per comment is permitted. The color of the reaction button changes to green for likes and red for dislikes, and this state remains even after reloading the page. The counts are updated both in the interface and in the database, maintaining consistency between the frontend and backend.

- **Profile Page:** Logged-in users have access to a profile page that displays two sections — one showing the comments they have written and another showing the comments they have liked. This page uses JavaScript to load and toggle between the two views, giving users a clear overview of their participation in the community.

Together, these features create a complete interactive environment where users can meditate, reflect, and connect through shared experiences.


### Static Files

The project makes use of several static files that provide styling, interactivity, and multimedia content. These files are stored in the `static` folder and are essential for the overall user experience.

- **CSS:** The stylesheet defines the visual identity of the app. It applies a galaxy background image across all pages, animated with a slow pan effect to create a calming atmosphere. Fade‑in sequences are used for the welcome message and meditation options, giving the interface a smooth entry animation. Text styling emphasizes golden tones with glowing shadows, while links and buttons include hover effects for interactivity. Forms and comment sections are styled with semi‑transparent backgrounds and glowing accents, ensuring readability against the dark cosmic theme. Overall, the CSS ties the meditation concept to a consistent aesthetic that feels immersive and tranquil.

- **JavaScript:** Two main scripts are used to add interactivity.
  - `index.js` is connected to the index page and manages the profile view toggle. When the user clicks the profile button, the script hides the index view and welcome section while displaying the profile view. This ensures smooth navigation without reloading the page.
  - `meditation.js` is used on the meditation pages and the profile page. It handles comment submission, deletion, and reactions (likes and dislikes). The script uses `fetch` requests to communicate with Flask routes, updating the interface dynamically. It also attaches reaction handlers to multiple lists, ensuring that comments and reactions work consistently across the index, normal meditation, letting go meditation, and profile pages.

- **Images:** A background image (`galaxy.jpg`) is applied to all pages, giving the app a calming and immersive atmosphere that matches the meditation theme.

- **Videos:** The core content of the app is delivered through video files. The `normalmeditation.mp4` file is used for the Normal Meditation page, while the `lettingomeditation.mp4` file is used for the Letting Go Meditation page. These videos are embedded directly into the templates and serve as the guided meditation sessions for users.

By combining CSS, JavaScript, images, and videos, the static files bring the meditation app to life. They provide the visual design, interactive features, and multimedia experiences that make the project engaging and functional.
