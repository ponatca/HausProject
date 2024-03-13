# Key/Value Store Server with Transactions

This is a simple key/value store server that supports transactions. The server allows clients to connect over a plain socket connection and issue commands to add or update key/value pairs, retrieve values by key, delete values by key, and control transactions (start, commit, rollback).

## Requirements

- Python 3.x

## Usage

1. Clone the repository:

    ```bash
    git clone git@github.com:ponatca/HausProject.git
    ```

2. Run the server:

    ```bash
    python server.py
    ```

3. Run the client to send commands:

    ```bash
    python client.py
    ```

## Commands

### Data Modification Commands

- **PUT [key] [value]**: Add or update a key/value pair. This command overwrites existing values.
- **GET [key]**: Retrieve a value by key. It retrieves the latest value from all committed transactions.
- **DEL [key]**: Delete a value by key.

### Transaction Control Commands

- **START**: Start a transaction.
- **COMMIT**: Commit a transaction.
- **ROLLBACK**: Rollback a transaction. Discard changes.

## Example Command Sequence

```plaintext
START
GET most_popular_leader
PUT georgew {"first_name":"George", "last_name":"Washington", "role":"President"}
PUT winstonc {"first_name":"Winston", "last_name":"Churchill", "role":"Prime Minister"}
COMMIT
```

## Refactoring Ideas
Some points that should be kept in mind if this server was to be implemented in real world

- **Error Handling**: Currently, error handling is quite basic. It responds with an error message for invalid commands or when a key is not found. It would be beneficial to implement more robust error handling, including handling unexpected exceptions and providing informative error messages.

- **Input Validation**: The input is assumed to be well-formed. However, in a real-world scenario, it's essential to validate input commands and data thoroughly to prevent potential security vulnerabilities and unexpected behavior.

- **Concurrency Handling**: This implementation doesn't handle concurrency issues. In a real-world scenario with multiple clients accessing the data store simultaneously, proper concurrency control mechanisms like locks or transaction isolation levels would need to be implemented to maintain data consistency and integrity.

- **Data Persistence**: The current implementation stores data in memory, which means that data will be lost when the server is restarted. For a more robust solution, consider adding support for data persistence, such as writing data to disk or using a database.

- **Optimizations**: Depending on the expected usage patterns and performance requirements, there might be opportunities for optimization. For example, optimizing data lookup and storage mechanisms, reducing memory usage, or improving network communication efficiency.

- **Security**: Security considerations, such as authentication and encryption, are crucial for a production-ready system, especially if the data store is accessible over the network. Implementing proper security measures would be essential to protect data and prevent unauthorized access.

- **Logging and Monitoring**: Adding logging and monitoring capabilities would facilitate debugging, troubleshooting, and performance analysis. It's important to log relevant events and metrics to gain insights into system behavior and performance.

- **Code Modularity and Readability**: While the current implementation is relatively concise, breaking down the code into smaller, more modular components and improving code readability can make it easier to understand, maintain, and extend in the future.

- **Testing**: Comprehensive unit tests and integration tests are essential to ensure the correctness and robustness of the system. Automated testing helps detect bugs early and provides confidence when making changes or refactoring code.

- **Documentation**: Documenting the code, including function and method docstrings, as well as providing high-level documentation for users and developers, improves the usability and maintainability of the system.