# Book Order System

## Overview

The **Book Order System** is a Python-based application designed to manage the ordering process for a bookstore. The system is built using the Factory design pattern, ensuring modularity and scalability. It provides an API to handle book orders, book management, and search functionalities, making it easy to integrate with other systems.

## Features

- **Factory Design Pattern**: The system leverages the Factory pattern to create different types of books and handle orders in a structured manner.
- **API Endpoints**: Provides a RESTful API to manage book orders, including adding books, placing orders, and searching for books.

## Technologies

- **Backend**:
  - Python
  - Flask
  - Factory Design Pattern
  
- **API**:
  - RESTful API with Flask

## API Endpoints

### `GET /api/v1/orders`
- **Description**: Retrieve a list of all orders.
- **Response**:
  - **200 OK**: Returns a JSON array of all orders.
  - **500 Internal Server Error**: If an error occurs during retrieval.

### `POST /api/v1/order`
- **Description**: Place a new book order.
- **Request Body**:
  ```json
  {
    "order_id": "string",
    "customer_name": "string",
    "total_amount": "number",
    "items": [
      {
        "book_id": "string",
        "quantity": "integer"
      }
    ]
  }
### `GET /api/v1/search`
- **Description**: Search for books by title or author name.
- **Query Parameters**:
  -title (optional): The title of the book to search for.
  -author_name (optional): The author of the book to search for.
- **Response**:
  - **200 OK**: Returns a JSON array of search results.
  - **500 Internal Server Error**: If an error occurs during the search.

### `GET /api/v1/books`
- **Description**: Retrieve a list of all available books.
- **Response**:
  - **200 OK**: Returns a JSON array of all books.
  - **500 Internal Server Error**: If an error occurs during retrieval.

### `POST /api/v1/book`
- **Description**: Add a new book to the bookstore.
- **Request Body**:
  ```json
  {
    "type": "string",  // e.g., "hardcover", "ebook", "audiobook"
    "author": "string",
    "title": "string",
    "price": "number",
    "weight": "number",       // Optional for physical books
    "file_size": "number",    // Optional for ebooks
    "duration": "number"      // Optional for audiobooks
  }  
  
