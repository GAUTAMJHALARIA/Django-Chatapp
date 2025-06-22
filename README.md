# Django Chatapp

## Overview

Django Chatapp is a real-time chat application built using Django, Channels, and WebSockets. It allows users to communicate with each other in real-time, with features like online user tracking, chat groups, and user profiles.

## Features

-   **Real-time Chat:** Utilizes WebSockets for instant messaging.
-   **User Authentication:** Secure user registration, login, and profile management.
-   **Online User Tracking:** Displays a list of currently online users.
-   **Chat Groups:** Organize conversations into different groups.
-   **User Profiles:** Customizable user profiles with avatar support.
-   **Asynchronous Task Handling:** Uses Channels for asynchronous communication.

## Technologies Used

-   **Django:** A high-level Python web framework.
-   **Django Channels:** Extends Django to support WebSockets and asynchronous tasks.
-   **WebSockets:** Provides full-duplex communication channels over a single TCP connection.
-   **Redis:** An in-memory data structure store, used as a message broker for Channels.
-   **HTML, CSS, JavaScript:** For the front-end interface.
-   **Poetry:** Python dependency management.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd Django Chatapp
    ```

2.  **Set up the environment using Poetry:**

    If you don't have Poetry installed, get it with:

    ```bash
    pip install poetry
    ```

    Then, install the dependencies:

    ```bash
    poetry install
    ```

3.  **Configure Redis:**

    Ensure Redis is installed and running. You can download it from [Redis Downloads](https://redis.io/download/) or use a package manager:

    ```bash
    # For Ubuntu
    sudo apt update
    sudo apt install redis-server

    # For macOS using Homebrew
    brew install redis
    ```

    Start the Redis server:

    ```bash
    redis-server
    ```

4.  **Set up Django settings:**

    Create a `.env` file in the project root and add the following:

    ```
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

    Modify the `core/settings.py` file to read these environment variables.

5.  **Run migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the application:**

    ```bash
    python manage.py runserver
    ```

    Open your browser and go to `http://localhost:8000`.

## Configuration

-   **Settings:**
    -   `core/settings.py`: Contains Django project settings, including database configuration, middleware settings, and static file configurations.
-   **Routing:**
    -   `chatapp/routing.py`: Defines the WebSocket routing configuration for the chat application.
-   **ASGI:**
    -   `core/asgi.py`: Asynchronous Server Gateway Interface configuration for handling WebSocket connections.

## Usage

1.  **Register/Login:**
    -   Navigate to the registration page to create a new account or log in with an existing account.
2.  **Update Profile:**
    -   Go to your profile page to update your avatar and other information.
3.  **Start Chatting:**
    -   Browse available chat groups or create a new one to start communicating with other users.
4.  **Online Users:**
    -   See the list of online users in the right sidebar.

## Contributing

We welcome contributions to Django Chatapp! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Test your changes thoroughly.
5.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or support, please contact [Your Name](your.email@example.com).
