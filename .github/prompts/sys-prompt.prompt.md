---
agent: agent
description: This prompt is used to generate a secure admin panel for managing a personal portfolio backend built with FastAPI.
model: Claude Opus 4.5 (copilot)
tools: [execute, read, edit, search, web, agent, todo]
---
You’re now at the “product-owner thinking like an architect” stage.

You already have:

✅ Backend (FastAPI + Postgres + Gemini)

✅ Flutter app (consumer-facing)

Now you want:

An Admin Panel to manage your own data,
built using Python frontend,
that talks to the same APIs,
without breaking anything in future versions.

That’s exactly how real SaaS portfolios are built.

🧠 Big Decision First: What kind of “Python frontend”?

There are 3 valid Python frontend choices.
I’ll pick the best one for YOUR use case, then explain why.

🏆 BEST CHOICE FOR YOU → FastAPI Admin Panel (Server-rendered UI)
Why this is the best for you:

Same backend language (Python)

Reuse models, schemas, auth later

No JS/React headache

Clean, professional

Easy to secure

Easy to deploy

Looks like real internal admin tools

👉 This is how internal dashboards are often done.

🔥 Final Stack (Admin Panel)
Backend (already exists)

FastAPI (your current backend)

Admin Frontend (new)

FastAPI + Jinja2

Tailwind CSS (optional but recommended)

Forms → call existing APIs

JWT/Auth scaffold (admin-only)

🧱 Overall Architecture (Very Important)
portfolio-backend/
 ├── app/
 │    ├── versions/v1/        ← existing APIs (DO NOT TOUCH)
 │    ├── admin/              ← NEW admin panel
 │    │    ├── routes.py
 │    │    ├── templates/
 │    │    ├── static/
 │    │    └── services.py
 │    └── main.py


✅ Admin panel is separate
✅ Uses same APIs
✅ No tight coupling
✅ Future-proof

🔐 Admin Panel Security (v1 – Simple & Safe)

For version 1:

Single admin user

Username + password in .env

Session-based auth (cookie)

Later (v2):

JWT

Role-based access

OAuth (Google/GitHub)

📋 Admin Features (v1)

Admin should be able to:

1️⃣ Personal Info

Update name, bio, contact info

Upload profile image URL

2️⃣ Skills

Add / delete skills

Category

Proficiency

3️⃣ Certifications

Add certifications

Issuer + link

4️⃣ Projects

Add personal/professional projects

Tech stack (comma-separated)

GitHub + live links

5️⃣ Experience

Add work experience

Learnings

6️⃣ View Contact Requests

Read-only (no edit)

🌐 How Admin Panel Talks to Backend

Admin panel does NOT access DB directly.

It calls:

POST /api/v1/projects
POST /api/v1/skills
POST /api/v1/experience
...


This ensures:

Same validation

Same rules

Same data shape

Zero duplication

🖥️ Admin UI Pages
/admin/login
/admin/dashboard
/admin/personal
/admin/skills
/admin/certifications
/admin/projects
/admin/experience
/admin/contacts

🧩 Templates (Jinja2)

Each page has:

Form

Submit button

Success / error message

Table preview (optional)

Example:

<form method="post">
  <input name="title" />
  <textarea name="description"></textarea>
  <button type="submit">Save</button>
</form>

🧠 Services Layer (IMPORTANT)

Admin never calls DB.
It calls internal HTTP API.

async def create_project(data):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{API_BASE}/projects",
            json=data
        )
    return response.json()

📦 Python Packages Needed (Admin)
jinja2
python-multipart
httpx
itsdangerous
fastapi
uvicorn


(You already have FastAPI)

🎨 UI Styling (Optional but Recommended)

Tailwind CDN (quick)

Or simple CSS

Keep it internal-tool style

Clean > Fancy

🚀 VERSIONING STRATEGY (CRITICAL)

Admin panel is NOT versioned

APIs are versioned (/api/v1)

Admin automatically works with v2 APIs later

This avoids breaking your Flutter app.

🔥 MASTER PROMPT — ADMIN PANEL GENERATION

THIS is what you asked for
One prompt → full admin panel

Copy-paste everything below 👇

🚀 ADMIN PANEL MASTER PROMPT START

You are a senior Python full-stack engineer.

I want you to build a secure admin panel for a personal portfolio backend.

The backend is already built using FastAPI and exposes REST APIs under:

/api/v1

🎯 GOAL

Create a Python-based admin frontend that allows me (admin) to insert and manage portfolio data using the existing APIs.

This admin panel is internal-only.

🧱 TECH STACK

Python 3.11+

FastAPI

Jinja2 templates

httpx (API calls)

Session-based authentication

Tailwind CSS (optional)

No JavaScript framework

🗂️ PROJECT STRUCTURE
app/
 ├── admin/
 │    ├── routes.py
 │    ├── services.py
 │    ├── auth.py
 │    ├── templates/
 │    │    ├── login.html
 │    │    ├── dashboard.html
 │    │    ├── personal.html
 │    │    ├── skills.html
 │    │    ├── projects.html
 │    │    ├── experience.html
 │    │    ├── certifications.html
 │    │    └── contacts.html
 │    └── static/
 └── main.py

🔐 AUTHENTICATION

Admin username & password from .env

Session cookie

Login required for all /admin/* routes

🔗 API INTEGRATION

Admin must call these APIs:

POST /api/v1/personal

POST /api/v1/skills

POST /api/v1/projects

POST /api/v1/experience

POST /api/v1/certifications

GET /api/v1/contact

Use httpx.AsyncClient.

📋 ADMIN FEATURES

Login / Logout

Dashboard

Manage Personal Info

Add Skills

Add Certifications

Add Projects

Add Experience

View Contact Requests

📑 UI REQUIREMENTS

Simple forms

Validation messages

Success / error feedback

Clean internal-dashboard UI

📦 DELIVERABLES

Complete admin panel code

Authentication logic

API service layer

HTML templates

README with setup steps

🚀 ADMIN PANEL MASTER PROMPT END
🏁 What You Have Now

You now own:

🔥 Backend (API)

📱 Flutter App (users)

🧑‍💼 Admin Panel (you)

This is NOT a toy project anymore.
This is a real, deployable product