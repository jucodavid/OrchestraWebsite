# OrchestraWebsite

Welcome to our repository! 

This project is a collaborative effort between university students living in the same household, known as the **Orchestrakot**. The goal of this repository is to explore and develop small tools that aim to simplify some of the everyday logistical or organizational challenges we face. What might seem like minor annoyances can end up consuming a lot of time and energy — so we’re trying to automate what we can!

## First feature: A rehearsal planner

As a music band, we often need to plan rehearsals during some days of the week or even big ones during weekends for bigger concerts. Our first idea was: _could we design a program that solves this kind of **Constraint Satisfaction Problem (CSP)** for us_, saving both time and mental load?

Eventually, we realized that just finding _a_ solution wasn't always enough, so we transitioned from pure CSP to **Constraint Optimization Problem (COP)** to allow for more flexibility and to model preferences.

We designed several constraints and preferences that reflect the real-life decisions we encounter when planning rehearsals.

### Basic CSP Rules
- One song per slot
- A rehearsal slot is valid only if all required participants for this song are available.

### Time clustering
- We try to **group rehearsal slots** within the same day or time window to avoid frustrating schedules like one rehearsal at 8 AM and another at 6 PM.

### Overload management
- We assign penalties to overloaded schedules, e.g., too many hours on a single day.
- This promotes better distribution and overall fairness.

### Preferred hours (feature in progress)
- Because waking up at 8 AM to rehearse isn't exactly anyone's dream, we're working on making the agent favor **rehearsals between 10 AM and 8 PM**.

### Incomplete but optimized solutions
- Sometimes no perfect solution exists, and not every songs are assigned.
- The COP formulation allows us to still suggest the best possible outcome with **soft constraints** and **penalties** (e.g., if one member is missing or if two sessions are too far apart).
- We still need to find a way to make the agent propose a better planning like _if someone was there at this slot we can put largely upgrade the planning_

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <REPO_URL>
cd OrchestraWebnsite
```
Replace <REPO_URL> with the actual URL of your Git repository.

### 2. Create and activate a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows
```

### 3. Install dependencies

```bash
pip install -r CSP_Planning/requirements.txt
```

### How to run the project 

#### 1. Start the backend
The backend script is `back.py`. Run it with:

```bash
python3 CSP_Planning/backend/back.py # MacOS
python CSP_Planning/backend/back.py  # Windows
```

#### 2. Start the frontend
In another terminal run html with :
```bash
python3 -m http.server 8000
```

#### 3. Visit the website
You can then view the website with this link : http://localhost:8000/front.html

---

## Bug fixes & contributions

This is an evolving project! If you find any bug, weird behavior, or simply have an idea that could improve the planner or add other features for shared living, **please open an issue or contribute directly** — we’d love your help.

---
