# FastAPI CRUD Demo

A small, layered FastAPI application for learning how a real API is organized.
It uses SQLite, so no external database is required.

## Project structure

```text
src/
	config/          Application settings
	controllers/     HTTP routes and dependency wiring
	database/        SQLAlchemy engine, session, and base model
	models/          Database models
	repositories/    Database access
	schemas/         Request and response validation
	services/        Business rules
	utils/           Shared exceptions and error helpers
	main.py          Application entry point
```

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for Swagger UI.

## Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| POST | `/api/v1/books` | Create a book |
| GET | `/api/v1/books` | List books |
| GET | `/api/v1/books/{book_id}` | Get one book |
| PUT | `/api/v1/books/{book_id}` | Replace a book |
| DELETE | `/api/v1/books/{book_id}` | Delete a book |

The SQLite file is created as `books.db` when the application starts.
