# demo_college_attempt

## Requirements
* Python 3.10 или выше
* Git
* Pillow

## Local host instruction

### 1. Copy repos.
```bash
git clone https://github.com/WebPunky/demo_college_attempt
cd name_repos
```

### 2. Create and activate venv
```bash
python -m venv .venv
```

* **Windows:**
  ```bash
  .venv\Scripts\activate
  ```
* **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Django
```bash
pip install django
```

### 4. Make migrations
Make tables in local DB (SQLite):
```bash
python manage.py migrate
```

*(optionally)* Create admin account (`/admin/`):
```bash
python manage.py createsuperuser
```

### 5. Run server
```bash
python manage.py runserver
```