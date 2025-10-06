# Setup Guide - Local Development

## Prerequisites

Before you start, ensure you have:
- ✅ Docker running (Rancher, Colima, or Docker Desktop)
- ✅ Python 3.11-3.13
- ✅ At least 16 GB RAM, 8 cores
- ✅ watsonx credentials in `.env` file

## Step-by-Step Setup

### Step 1: Check Your .env File

Your `.env` file should have these variables:
```bash
# Option 1: watsonx Orchestrate credentials (if you have them)
WO_INSTANCE=https://api.dl.watson-orchestrate.ibm.com/instances/...
WO_API_KEY=your_api_key

# Option 2: WatsonX AI credentials (alternative)
WATSONX_APIKEY=your_watsonx_api_key
WATSONX_SPACE_ID=your_space_id
```

### Step 2: Start Docker

Make sure Docker is running:
```bash
docker ps
```

If it's not running, start Docker Desktop/Rancher/Colima first.

### Step 3: Start Orchestrate Server

```bash
# Activate virtual environment
source watonx-env/bin/activate

# Start the server (this may take 5-10 minutes first time)
orchestrate server start --env-file .env
```

**Wait for this message:**
```
✅ Server is ready!
```

### Step 4: Activate Local Environment

In a **new terminal** (keep the server running):
```bash
source watonx-env/bin/activate
orchestrate env activate -n local
```

### Step 5: Deploy Your Agent

```bash
./deploy.sh
```

### Step 6: Start Chatting

```bash
orchestrate chat start
```

This will open a web UI in your browser (usually at http://localhost:3000)

## Troubleshooting

### Issue: "Remote end closed connection"
**Solution:** The server isn't running. Follow Step 3 above.

### Issue: "No tools found"
**Solution:** Tools need to be imported before the agent. The deploy script handles this, but make sure the server is running first.

### Issue: "Docker not found"
**Solution:** Install and start Docker (Rancher Desktop recommended for Mac)

### Issue: Server takes too long
**Solution:** First startup downloads Docker images. Be patient (5-10 min).

## Quick Start Commands

```bash
# Terminal 1: Start server
source watonx-env/bin/activate
orchestrate server start --env-file .env

# Terminal 2: Deploy and chat (after server is ready)
source watonx-env/bin/activate
orchestrate env activate -n local
./deploy.sh
orchestrate chat start
```

## Alternative: Using Cloud Instance

If you have watsonx Orchestrate cloud access, you don't need to run the local server:

```bash
# Just deploy directly
source watonx-env/bin/activate
orchestrate tools import -k python -f tools.py
orchestrate agents import -f customer_support_agent.yaml
orchestrate chat start
```

Your credentials in `.env` will connect to the cloud instance automatically.
