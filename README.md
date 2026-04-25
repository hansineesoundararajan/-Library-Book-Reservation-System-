# LibraryFlow - Library Book Reservation System

A full-stack Library Book Reservation System built with FastAPI, SQLite, ReactJS, and an auto-generated Python SDK via OpenAPI Generator CLI.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Quick Start Windows](#quick-start-windows)
- [Manual Setup](#manual-setup)
- [Running the Application](#running-the-application)
- [API Reference](#api-reference)
- [Reservation Rules](#reservation-rules)
- [SDK Generation and Usage](#sdk-generation-and-usage)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Design Decisions](#design-decisions)
- [License](#license)
- [About](#about)

## Project Overview

LibraryFlow is a production-style library reservation application that demonstrates:

- Backend - FastAPI REST API with SQLite, Alembic migrations, strict input validation, and OpenAPI documentation.
- Frontend - ReactJS SPA for viewing books, adding books, reserving books, cancelling reservations, and tracking availability.
- Trick Logic - Limited book copies, reservation expiry, and cancellation logic that restores availability.
- SDK - Auto-generated Python SDK using OpenAPI Generator CLI.
- Automation - One-command setup and launch through Windows batch scripts.
- Tests - Backend unit tests for core reservation behavior and edge cases.

The main challenge requirement is correctly handling limited copies. A book can only be reserved while copies are available. Cancelling or expiring a reservation makes the copy available again.

## Architecture

```text
library-book-reservation-system/
|-- backend/                          FastAPI + SQLite
|   |-- core/
|   |   |-- database.py               SQLAlchemy engine + session
|   |   |-- deps.py                   get_db dependency
|   |   |-- main.py                   FastAPI app entry point
|   |   |-- models.py                 ORM models: Book, Reservation
|   |   |-- schemas.py                Pydantic schemas and validation
|   |   |-- routes/
|   |   |   |-- books.py              Book endpoints + reserve endpoint
|   |   |   `-- reservations.py       Reservation list + cancel endpoints
|   |   `-- services/
|   |       |-- book_service.py        Book service logic
|   |       `-- reservation_service.py Reservation limit, expiry, cancellation logic
|   |-- alembic/                      Database migration scripts
|   |-- tests/                        Backend unit tests
|   |-- alembic.ini
|   |-- requirements.txt
|   |-- seed_data.sql                 Sample book data
|   `-- library.db                    SQLite database, created by setup
|-- frontend/                         ReactJS SPA
|   |-- public/
|   |-- src/
|   |   |-- App.js                    Main UI and API interaction
|   |   |-- index.js                  React entry point
|   |   `-- index.css                 Styling
|   `-- package.json
|-- library_sdk/                      Auto-generated Python SDK
|-- test_sdk.py                       SDK usage smoke test
|-- setupdev.bat                      One-command environment setup
|-- runapplication.bat                One-command application launch
|-- pytest.ini                        Pytest configuration
`-- README.md
```

## Prerequisites

| Tool | Version | Download |
|---|---:|---|
| Python | 3.10+ | https://www.python.org/downloads/ |
| Node.js | 18+ | https://nodejs.org/ |
| npm | 8+ | Included with Node.js |
| Java | 11+ | https://adoptium.net/ |

Note: Docker is not used. All services run natively.

Check installed versions:

```powershell
python --version
node --version
npm --version
java --version
```

## Quick Start Windows

```bat
:: 1. Clone or extract the project
git clone <your-repository-url>
cd <repository-folder>

:: 2. Set up everything: Python venv, backend dependencies, SDK, DB migrations, seed data, npm packages
setupdev.bat

:: 3. Launch the full application
runapplication.bat
```

If you are using PowerShell, run local batch files with `.\`:

```powershell
.\setupdev.bat
.\runapplication.bat
```

The application will run at:

- Frontend: http://localhost:3000
- Backend: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Manual Setup

### Backend

Run these commands from the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r backend\requirements.txt
pip install -e library_sdk

python -m alembic -c backend\alembic.ini upgrade head
python -c "import pathlib, sqlite3; db=pathlib.Path('backend/library.db'); sql=pathlib.Path('backend/seed_data.sql').read_text(); con=sqlite3.connect(db); con.executescript(sql); con.commit(); con.close()"

.\.venv\Scripts\python.exe -m uvicorn core.main:app --reload --app-dir backend
```

Backend runs at:

```text
http://127.0.0.1:8000
```

### Frontend

Open another terminal from the project root:

```powershell
cd frontend
npm install
npm start
```

Frontend runs at:

```text
http://localhost:3000
```

## Running the Application

Windows recommended:

```powershell
.\runapplication.bat
```

The script starts:

- Backend server on `http://127.0.0.1:8000`
- Frontend React app on `http://localhost:3000`

The frontend interacts with the backend only through API calls. It does not access the database directly.

## API Reference

Base URL:

```text
http://127.0.0.1:8000
```

| Method | Endpoint | Description |
|---|---|---|
| POST | `/books/` | Create a new book |
| GET | `/books/` | List all books |
| GET | `/books/{book_id}` | Get book details |
| GET | `/books/stats` | Get dashboard stats |
| POST | `/books/{book_id}/reserve` | Reserve a book |
| GET | `/reservations/` | List active reservations |
| DELETE | `/reservations/{reservation_id}` | Cancel a reservation |

### Example Requests

Create a book:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/books/" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"title":"Clean Architecture","author":"Robert Martin","total_copies":2}'
```

List books:

```powershell
Invoke-RestMethod "http://127.0.0.1:8000/books/"
```

Reserve a book:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/books/1/reserve" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_name":"Library Member"}'
```

Cancel a reservation:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/reservations/1" `
  -Method Delete
```

## Reservation Rules

This is the core trick requirement. The backend enforces limited-copy reservation rules.

Each book has:

```text
total_copies
available_copies
```

Reservation behavior:

```text
reserve    -> available_copies decreases by 1
cancel     -> available_copies increases by 1
expire     -> reservation is deleted and available_copies increases by 1
```

Reservations expire after:

```text
7 days
```

### Rules

| Scenario | Result | HTTP Code |
|---|---|---:|
| Book exists and has available copies | Reservation created | 200 |
| Book does not exist | Rejected | 404 |
| Book has zero available copies | Rejected | 409 |
| Invalid payload | Rejected | 422 |
| Cancel existing reservation | Cancelled and copy restored | 200 |
| Cancel missing reservation | Rejected | 404 |

### Example Logic

```text
Book A has 3 copies.

Reservation 1 -> OK, available copies = 2
Reservation 2 -> OK, available copies = 1
Reservation 3 -> OK, available copies = 0
Reservation 4 -> rejected, no copies available

Cancel reservation 1 -> available copies = 1
Reserve again -> OK
```

### Error Response Example

```json
{
  "detail": "No copies available"
}
```

## SDK Generation and Usage

The SDK is generated from FastAPI's live OpenAPI schema.

The generated SDK folder:

```text
library_sdk/
```

The generated Python package name:

```text
openapi_client
```

### Generate the SDK

Start the backend first:

```powershell
.\runapplication.bat
```

Generate the SDK from another terminal:

```powershell
npx @openapitools/openapi-generator-cli generate -i http://127.0.0.1:8000/openapi.json -g python -o library_sdk
.\.venv\Scripts\python.exe -m pip install -e library_sdk
```

### Use the SDK

```python
from openapi_client import ApiClient, Configuration
from openapi_client.api.books_api import BooksApi
from openapi_client.models.book_create import BookCreate
from openapi_client.models.reservation_create import ReservationCreate

config = Configuration(host="http://127.0.0.1:8000")

with ApiClient(config) as client:
    api = BooksApi(client)

    book = api.create_book_books_post(
        BookCreate(
            title="Domain-Driven Design",
            author="Eric Evans",
            total_copies=2,
        )
    )

    reservation = api.reserve_book_books_book_id_reserve_post(
        book.id,
        ReservationCreate(user_name="Library Member"),
    )

    print(book)
    print(reservation)
```

Run the SDK smoke test:

```powershell
.\.venv\Scripts\python.exe test_sdk.py
```

## Running Tests

From the project root:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Expected output:

```text
6 passed
```

### Test Coverage

- Book creation
- Invalid book copy count
- Missing book lookup
- Reservation creation
- Reservation limit enforcement
- Reservation for missing book
- Reservation cancellation
- Expired reservation cleanup
- Copy availability restoration

## Project Structure

Most important files:

```text
backend/core/services/reservation_service.py   Reservation limit, expiry, cancellation logic
backend/core/services/book_service.py          Book business logic
backend/core/routes/books.py                   Book and reserve endpoints
backend/core/routes/reservations.py            Reservation list and cancel endpoints
backend/core/models.py                         SQLAlchemy models
backend/core/schemas.py                        Pydantic validation schemas
backend/tests/                                 Backend unit tests
frontend/src/App.js                            React UI and API calls
frontend/src/index.css                         Frontend styling
library_sdk/                                   Generated SDK
test_sdk.py                                    SDK demonstration
setupdev.bat                                   Development setup
runapplication.bat                             Full app launcher
```

## Design Decisions

### Why a service layer?

Separating business logic from API routes keeps the project modular and testable. The tricky reservation rules live in `reservation_service.py`, not inside route handlers.

### Why Alembic migrations?

Alembic keeps the database schema versioned and repeatable. Anyone cloning the project can recreate the SQLite database with `alembic upgrade head`.

### Why cleanup expired reservations in multiple places?

Expired reservations must free copies. Cleanup runs before reservation attempts, book reads, stats reads, reservation lists, and also through a background task while the backend is running.

### Why an OpenAPI-generated SDK?

The challenge requires a generated SDK instead of a manually written client. FastAPI exposes `/openapi.json`, and OpenAPI Generator CLI uses that schema to generate the Python client.

### Why a simple frontend?

The challenge prioritizes functionality. The React frontend focuses on the required workflows: viewing books, creating books, reserving books, viewing reservations, and cancelling reservations.

## License

This project is built for the Library Book Reservation intern coding challenge. Add a `LICENSE` file before publishing publicly if a specific license is required.

## About

Library Book Reservation System using FastAPI, SQLite, ReactJS, Alembic, and OpenAPI Generator.

Core logic: limited copies, reservation expiry, and cancellation restoring availability.

## Resources

- README: this file
- API Docs: `http://127.0.0.1:8000/docs`
- Frontend: `http://localhost:3000`
- SDK folder: `library_sdk/`
