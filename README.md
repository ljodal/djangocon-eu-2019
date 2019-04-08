# Pushing the ORM to its limit

This repository contains an example project with code from my DjangoCon EU 2019
talk "Pushing the ORM to its limit". It contains code to demonstrate various ORM
features and tricks to work around quirks with the ORM.


## Setup

This project requires Django 2.2 or newer, as specified in `requirements.txt`.

To install the requirements run the following in an virtualenv:

```bash
pip install -r requirements.txt
```

Next I have set up a Docker Compose file to run the database, so you can set
that up if you have docker:

```bash
docker-compose up
```

Finally migrate the database and create some sample data:

```bash
./manage.py migrate
./manage.py create_sample_data
```


## The interesting bits

There's not too much code here, as the goal is to show off the database related
code. The interesting files are:

 * [orders/models.py](./orders/models.py)
 * [orders/managers.py](./orders/managers.py)
 * [orders/management/commands/create\_sample\_data.py](./orders/management/commands/create_sample_data.py)
 * [products/models.py](./products/models.py)
 * [customers/models.py](./customers/models.py)
 * [customers/managers.py](./customers/managers.py)
 * [budget/models.py](./budget/models.py)
 * [budget/managers.py](./budget/managers.py)

I have not set up any views or configured the admin, so I recommend using the
Django shell to explore the models:

```bash
./manage.py shell
```
