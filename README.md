# Global View

Global View is an application that shows a live camera feed from ip cams around the world.  

## Getting Started

To run the flask app locally, clone or download the directory. First, create a MySQL database and run the "dump.sql" script on it. Then, input the database conncetion details into 'main.py'. Finally, activate the virtualenv and run the flask server "main.py". 
It should now be running on your local machine.

### Prerequisites

You should have python, virtualenv and mysql installed on your machine 

## Live Demo

https://global-view.herokuapp.com/

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) - Dependency Management
* [MySQL](https://www.mysql.com/) - Database

## Authors

* **Guillermo Casal** - *Initial work* - [gcasa032](https://github.com/gcasa032)

## Know bugs

* Live feed request time out - On the live deployed version, the livestreams will die after 30s due to Heroku's request time limit. 