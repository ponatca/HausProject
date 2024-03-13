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