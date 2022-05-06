# CommonCents

CommonCents is a web application that is intended to be used by individuals who are visually impaired. After researching, my team members and I realized that there aren't many resources for people with visual disabilities, especially when it relates to their finances. We decided to create this application to help these individuals be able to differentiate between the USD currency.

The application can tell the difference between the most common US bank notes. These include $1, $5, $10, $20, $50, and $100 bills.

## Requirements:

1. React (https://reactjs.org/)
2. Python (https://www.python.org/)
3. Pipenv (https://pipenv.pypa.io/en/latest/)
4. Teachable machine (https://teachablemachine.withgoogle.com/)

Note: This web application uses machine learning algorithms to be able to differentiate between the different dollar bills. For this we relied heavily on teachable machine to do the heavylifting for us.

## Installation:

1. Clone the project.
2. Make sure you have python and pipenv installed on your machine, this is mandatory to be able to get this project up and running.
3. In the root directory run `pipenv install` to install Python dependencies.
4. In the root directory run `pipenv shell` to activated the Python virtual environment.

Please note: You will need two separate terminals: one for the client folder, and one for the flask app folder.

## Running the project:

The web application uses a react frontend, to allow the user to upload a file. Which then passes along the file that was uploaded to the flask app backend. The backend will pass that file to the trained machine learning model. The prediction then returned to react.

To run the react app:

1. `cd` into the `client` folder.
2. Run `npm start`, this should open up a browser with a url of 'http://localhost:3000'.

To run the flask server:

1. In the root directory, run `flask run` to start the flask server.

## How to use the web application:

Once the application is up and running, you can upload a file/picture of a us currency note. The prediction will be returned and displayed.

## Next steps:

There are a few features that we want to add to our project:

1. Display the image that the user uploaded onto the screen.
2. Feedback section, where the user can tell us if the output that was provided was correct or not.
3. Accessibility options: have the output be read out loud to the user.
