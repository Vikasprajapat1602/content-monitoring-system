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

## ⚙️ Setup Instructions

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

## Suppression Logic

If a flag is marked as irrelevant, it is not re-created in future scans.
The system tracks last_reviewed_at timestamp.
If ContentItem.last_updated is newer than the review timestamp:
→ flag is allowed again.

## Assumptions

Mock JSON dataset used instead of external API.
Content uniqueness is based on title + source.
Duplicate flags are prevented using keyword-content pair checks.
