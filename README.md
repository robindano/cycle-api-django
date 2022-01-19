# Cycle

Cycle is a community building app where neighbors can exchange goods for free.

This is the API, built with Django, using Django Rest Framework and Celery. This utilizes a MYSQL database, and Redis as a broker for Celery tasks. The [Frontend](https://github.com/joeylking/cycle) was built with React.

## Project Features

• JWT authentication for user registration, login, and logout.

• Gifts are listed with a description, condition, picture, and a specified ending time.

• Users in the same city can add themselves to a gift’s list of interested users and publicly comment to ask questions about a specific gift.

• Integrates Celery, using a Redis broker, to schedule an asynchronous ‘pick_winner’ task, randomly choosing a winner from the interested list at the time specified by the giver and setting the gift inactive.

• Users, gifts, comments, and celery task results are stored in a MySQL database.

• Utilizes Axios to fetch data via API endpoints created with Django Rest Framework.
