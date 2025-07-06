[![Python](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.0-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Screenshot
![Project Screenshot](link_to_your_screenshot)

# Django Chatapp 💬

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

# Django Chatapp 💬

🚀 A real-time chat application built with Django, Channels, and WebSockets. 🚀

## Overview ℹ️

Django Chatapp is a cutting-edge real-time chat application meticulously crafted using the robust Django framework, enhanced by the asynchronous capabilities of Channels, and powered by the efficiency of WebSockets. This dynamic combination enables users to engage in seamless, instantaneous communication, fostering vibrant interactions and collaborations.

Key features include:

-   **Real-time Communication:** Experience the immediacy of live conversations, eliminating delays and enhancing user engagement.
-   **Online User Tracking:** Stay connected with a dynamic display of currently active users, promoting a sense of community and presence.
-   **Chat Groups:** Organize discussions into focused groups, facilitating efficient collaboration and knowledge sharing.
-   **User Profiles:** Personalize your identity with customizable profiles, complete with avatar support, adding a touch of individuality to the platform.

## Features ✨

-   **Real-time Chat:** 💬
    -   Experience instantaneous messaging powered by WebSockets, ensuring seamless and responsive conversations.
-   **User Authentication:** 🔒
    -   Securely manage user accounts with robust registration, login, and profile management features, safeguarding user data and privacy.
-   **Online User Tracking:** 🟢
    -   Stay connected with a dynamic display of currently active users, fostering a sense of community and presence within the application.
-   **Chat Groups:** 👥
    -   Organize discussions into focused groups, facilitating efficient collaboration, knowledge sharing, and streamlined communication.
-   **User Profiles:** 👤
    -   Personalize your identity with customizable profiles, complete with avatar support, adding a touch of individuality and enhancing user engagement.
-   **Asynchronous Task Handling:** ⏳
    -   Leverage Channels for efficient asynchronous task management, ensuring smooth performance and responsiveness even during high-traffic periods.

## Technologies Used 🛠️

-   **Django:** 🐍
    -   A high-level Python web framework that encourages rapid development and clean, pragmatic design.
-   **Django Channels:** 📡
    -   A project that adds WebSocket, long-poll, and other asynchronous capabilities to Django.
-   **WebSockets:** 🔗
    -   A communication protocol that provides full-duplex communication channels over a single TCP connection.
-   **HTML, CSS, JavaScript:** 🎨
    -   The core technologies for building the user interface of the chat application.
-   **Poetry:** 📦
    -   A tool for dependency management and packaging in Python.

## Installation ⚙️

1.  **Clone the repository:** ⬇️
    -   Clone the repository to your local machine using Git:

    ```bash
    git clone <repository_url>
    cd Django Chatapp
    ```

2.  **Set up the environment using Poetry:** 📝
    -   If you don't have Poetry installed, get it with:

    ```bash
    pip install poetry
    ```
    -   Then, install the dependencies:

    ```bash
    poetry install
    ```

3.  **Set up Django settings:** ⚙️
    -   Create a `.env` file in the project root and add the following:

    ```
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```
    -   Modify the `core/settings.py` file to read these environment variables.

4.  **Run migrations:** 🚀
    -   Apply the database migrations to set up the database schema:

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser:** 🧑‍💻
    -   Create an administrative user to manage the application:

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the application:** 🏃‍♂️
    -   Start the Django development server:

    ```bash
    python manage.py runserver
    ```
    -   Open your browser and go to `http://localhost:8000` to access the application.

## Configuration 🛠️

-   **Settings:** ⚙️
    -   `core/settings.py`: Contains Django project settings, including database configuration, middleware settings, static file configurations, and more.
-   **Routing:** 🔀
    -   `chatapp/routing.py`: Defines the WebSocket routing configuration for the chat application, mapping URL patterns to consumers.
-   **ASGI:** ⚡
    -   `core/asgi.py`: Asynchronous Server Gateway Interface configuration for handling WebSocket connections, enabling real-time communication.

## Usage 🚀

1.  **Register/Login:** 🔑
    -   Navigate to the registration page to create a new account or log in with an existing account to access the chat application.
2.  **Update Profile:** ✏️
    -   Go to your profile page to update your avatar and other personal information, customizing your identity within the platform.
3.  **Start Chatting:** 💬
    -   Browse available chat groups or create a new one to start communicating with other users and engage in real-time conversations.
4.  **Online Users:** 🟢
    -   See the list of online users in the right sidebar, providing a dynamic view of the active community members.

