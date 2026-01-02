# Background Removal Server - Render.com Deployment Guide

## Quick Deployment Steps

### Step 1: Create Render Account (2 minutes)

1. Go to <https://render.com>
2. Click "Get Started for Free"
3. Sign up with your email or GitHub
4. Verify your email

### Step 2: Deploy to Render (5 minutes)

#### Option A: Deploy from GitHub (Recommended)

1. Push the `server` folder to your GitHub repository
2. In Render dashboard, click "New +" → "Web Service"
3. Connect your GitHub account
4. Select your repository
5. Configure:
   - **Name:** `bhejjo-bg-removal`
   - **Root Directory:** `server`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** `Free`
6. Click "Create Web Service"
7. Wait 5-10 minutes for deployment
8. Copy your service URL (e.g., `https://bhejjo-bg-removal.onrender.com`)

#### Option B: Deploy Manually (No GitHub)

1. In Render dashboard, click "New +" → "Web Service"
2. Select "Deploy an existing image from a registry" → Skip
3. Choose "Public Git repository"
4. I'll help you create a public repo with just the server code

### Step 3: Update Flutter App (2 minutes)

Once deployed, I'll update your Flutter app to use the Render URL instead of remove.bg.

### Step 4: Test (1 minute)

1. Upload an image in your app
2. Click "Remove BG"
3. First request might take 30 seconds (server waking up)
4. Subsequent requests will be fast!

---

## Server Details

**Endpoint:** `POST /remove-background`
**Request:** Multipart form-data with `image_file`
**Response:** PNG image with transparent background

**Free Tier Limits:**

- ✅ 750 hours/month (24/7 coverage)
- ✅ Unlimited requests
- ⚠️ Sleeps after 15 min inactivity (wakes in ~30 sec)

---

## Troubleshooting

**Server sleeping?**

- Normal behavior on free tier
- First request wakes it up
- Stays awake for 15 minutes after last request

**Deployment failed?**

- Check build logs in Render dashboard
- Verify all files are in `server` folder
- Ensure Python version is 3.11

**Slow processing?**

- First request after sleep is slower
- Large images take longer
- Consider upgrading to paid tier for always-on

---

## Next Steps

After deployment, I'll:

1. Update `BackgroundRemovalService` with your Render URL
2. Hot reload the app
3. Test background removal
4. You'll have unlimited free background removal! 🎉
