# Quick Deployment Guide - 10 Minutes

## Step 1: Push to GitHub (3 minutes)

### Option A: Create New Repo (Fastest)

1. Go to <https://github.com/new>
2. Name: `bhejjo-bg-removal-server`
3. Make it **Public** (required for free Render deployment)
4. Click "Create repository"
5. Run these commands:

```bash
cd e:\bhejjo_now\server
git init
git add .
git commit -m "Initial commit: Background removal server"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bhejjo-bg-removal-server.git
git push -u origin main
```

### Option B: Use Existing Repo

If you already have a GitHub repo for bhejjo_now, just push the server folder:

```bash
cd e:\bhejjo_now
git add server/
git commit -m "Add background removal server"
git push
```

---

## Step 2: Deploy on Render.com (5 minutes)

1. **Sign up:** <https://render.com> (use GitHub to sign up - faster!)

2. **Create Web Service:**
   - Click "New +" → "Web Service"
   - Connect GitHub
   - Select `bhejjo-bg-removal-server` repo

3. **Configure:**
   - **Name:** `bhejjo-bg-removal`
   - **Root Directory:** Leave empty (or `server` if using existing repo)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** `Free`

4. **Deploy:**
   - Click "Create Web Service"
   - Wait 5-10 minutes
   - **Copy your URL:** `https://bhejjo-bg-removal-XXXX.onrender.com`

---

## Step 3: Update Flutter App (1 minute)

I'll do this for you once you give me the Render URL!

---

## Alternative: I Can Help You

If you want, I can:

1. Create a temporary public GitHub gist with the server code
2. You deploy from that gist to Render
3. Takes 5 minutes total

**Which do you prefer?**

- A) I guide you through GitHub + Render (you do it)
- B) I create a gist, you deploy from gist (faster, I help more)
