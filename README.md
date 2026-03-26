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

## 📂 Project Structure
monitoring/
│── models.py
│── serializers.py
│── views.py
│── services.py
│── urls.py
│── mock_data.py
