# MySQL Learning Guide

## Table of Contents

- [Introduction](#introduction)
- [What’s a Database](#whats-a-database)
- [What’s a Relational Database](#whats-a-relational-database)
- [What does SQL Stand For](#what-does-sql-stand-for)
- [What’s MySQL](#whats-mysql)
- [How to Create a Database in MySQL](#how-to-create-a-database-in-mysql)
- [What do DDL and DML Stand For](#what-do-ddl-and-dml-stand-for)
- [How to CREATE or ALTER a Table](#how-to-create-or-alter-a-table)
- [How to SELECT Data from a Table](#how-to-select-data-from-a-table)
- [How to INSERT, UPDATE, or DELETE Data](#how-to-insert-update-or-delete-data)
- [What are Subqueries](#what-are-subqueries)
- [How to Use MySQL Functions](#how-to-use-mysql-functions)

## Introduction

This guide provides a comprehensive overview of MySQL, a popular relational database management system. You will learn the fundamental concepts of databases, SQL, and MySQL, including how to create, manipulate, and query databases.

## What’s a Database

A database is an organized collection of data, generally stored and accessed electronically from a computer system. Databases allow for efficient storage, retrieval, and manipulation of data.

## What’s a Relational Database

A relational database is a type of database that stores and provides access to data points that are related to one another. Data is organized into tables (also known as relations) which consist of rows and columns. Each table represents a different type of entity and its attributes.

## What does SQL Stand For

SQL stands for Structured Query Language. It is the standard language used to communicate with and manipulate relational databases. SQL allows users to perform tasks such as querying data, updating records, and managing database schema.

## What’s MySQL

MySQL is an open-source relational database management system (RDBMS) that uses SQL. It is widely used for web applications and is known for its reliability, performance, and ease of use.

## How to Create a Database in MySQL

To create a database in MySQL, you can use the following SQL command:

```sql
CREATE DATABASE database_name;
```

## What do DDL and DML Stand For

   - DDL: Data Definition Language. It includes SQL commands that define the database schema, such as CREATE, ALTER, and DROP.
   - DML: Data Manipulation Language. It includes SQL commands used for managing data within schema objects, such as SELECT, INSERT, UPDATE, and DELETE.

### How to CREATE or ALTER a Table
### CREATE

To create a table in MySQL, you can use the following SQL command:

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```
## What are Subqueries

Subqueries are queries nested inside another query. They are used to perform operations that require multiple steps, allowing you to retrieve data based on the results of another query. For example:

```sql
SELECT column1
FROM table_name
WHERE column2 = (SELECT column2 FROM another_table WHERE condition);
```

## How to Use MySQL Functions

MySQL provides a variety of built-in functions to perform operations on data. Some common functions include:

   - String Functions: CONCAT(), UPPER(), LOWER()
   - Numeric Functions: ABS(), ROUND(), CEIL()
   - Date and Time Functions: NOW(), CURDATE(), DATE_ADD()

You can use these functions in your SQL queries to manipulate and retrieve data as needed.
