Tornado blog
============

A simple blog project written in tornado.

Requirements
------------

* python
* pip
* MySQL

Installation
------------

Create the MySQL databases:

    make recreate-dbs

One command is necessary to setup the enviroment:

    make setup

To run the migrations to update the database:

    make data

To run the tests:

    make test

To run the server:

    make run
