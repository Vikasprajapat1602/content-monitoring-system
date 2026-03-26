# Content Monitoring & Flagging System

A backend system built using Django and Django REST Framework that monitors content against user-defined keywords, generates match-based flags, and supports a reviewer workflow with suppression logic.

---

## Features

- Add and manage keywords
- Ingest content from mock dataset
- Keyword-based matching with scoring:
  - Exact match in title → 100
  - Partial match in title → 70
  - Match in body → 40
- Flag generation system
- Reviewer workflow (pending → relevant / irrelevant)
- Suppression logic:
  - Irrelevant flags are not re-generated unless content changes

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

---

## Project Structure
monitoring/
│── models.py
│── serializers.py
│── views.py
│── services.py
│── urls.py
│── mock_data.py


---

## Setup Instructions

```
git clone <your-repo-link>
cd content_monitoring_system
```
```
python -m venv venv
venv\Scripts\activate   
```
```
python manage.py migrate
python manage.py runserver
```


## API Endpoints

 - Keyword Management
    - POST /api/keywords/ → Create keyword
    - GET /api/keywords/ → List keywords
 - Content & Scan
    - POST /api/load-content/ → Load mock content
    - POST /api/generate-flags/ → Generate flags
    - POST /api/scan/ → Run full pipeline
 - Flags & Review
    - GET /api/flags/ → List flags
    - PATCH /api/flags/{id}/ → Update status
  
## Data Source

This project uses a mock JSON dataset for content ingestion.

Reason:
- Simpler and faster implementation
- No dependency on external APIs
- Deterministic and easy to test

Content is loaded via:
POST /api/load-content/

## Sample API Requests

### 1. Add Keyword

curl -X POST http://127.0.0.1:8000/api/keywords/ \
-H "Content-Type: application/json" \
-d '{"name": "python"}'


### 2. Load Content

curl -X POST http://127.0.0.1:8000/api/load-content/


### 3. Generate Flags

curl -X POST http://127.0.0.1:8000/api/generate-flags/


### 4. Run Full Scan

curl -X POST http://127.0.0.1:8000/api/scan/


### 5. Get Flags

curl http://127.0.0.1:8000/api/flags/


### 6. Update Flag Status

curl -X PATCH http://127.0.0.1:8000/api/flags/1/ \
-H "Content-Type: application/json" \
-d '{"status": "irrelevant"}'


## Suppression Logic

If a flag is marked as irrelevant, it is not re-created in future scans.
The system tracks last_reviewed_at timestamp.
If ContentItem.last_updated is newer than the review timestamp:
→ flag is allowed again.

##  Assumptions & Trade-offs

- Used mock dataset instead of external API for simplicity and reliability.
- Content uniqueness is determined using (title + source).
- Matching logic is rule-based (exact, partial, body match).
- No background jobs implemented (scan is synchronous).
- Suppression logic uses last_reviewed_at timestamp comparison.
