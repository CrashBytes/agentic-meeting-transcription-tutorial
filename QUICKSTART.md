# Quick Setup Guide

Get the Agentic Meeting Transcription System running in under 10 minutes.

## Prerequisites

- Docker and Docker Compose installed
- OpenAI API key
- Hugging Face token (for speaker diarization)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/CrashBytes/agentic-meeting-transcription-tutorial.git
cd agentic-meeting-transcription-tutorial
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API keys
nano .env  # or use your preferred editor
```

Required environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key from https://platform.openai.com/api-keys
- `HUGGINGFACE_TOKEN`: Your Hugging Face token from https://huggingface.co/settings/tokens

### 3. Start All Services

```bash
# Start with Docker Compose
docker-compose up -d

# Wait for services to be ready (about 30 seconds)
sleep 30

# Check all services are running
docker-compose ps
```

### 4. Verify Installation

```bash
# Check backend health
curl http://localhost:8000/health

# Access API documentation
open http://localhost:8000/docs
```

Expected response:
```json
{
  "status": "healthy",
  "agents": {
    "transcription": true,
    "diarization": true
  }
}
```

### 5. Test the System

```bash
# Upload a test audio file (WAV format)
curl -X POST http://localhost:8000/api/meetings \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Meeting", "participants": ["Alice", "Bob"]}'

# Save the meeting ID from the response
# Then upload audio
curl -X POST http://localhost:8000/api/meetings/{meeting_id}/upload-audio \
  -F "audio=@path/to/your/audio.wav"
```

## Service URLs

- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Qdrant Dashboard**: http://localhost:6333/dashboard
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

## Next Steps

1. **Read the Full Documentation**: See [README.md](README.md) for detailed features
2. **Try Different Audio Files**: Test with various meeting recordings
3. **Explore the API**: Use the interactive API docs at `/docs`
4. **Review Analysis**: Check summaries and action items
5. **Deploy to Production**: See [Kubernetes Guide](#kubernetes-deployment)

## Common Issues

### Port Already in Use
```bash
# Check what's using the port
lsof -i :8000

# Stop conflicting services or change ports in docker-compose.yml
```

### API Key Not Working
- Verify key format in .env file
- Ensure no extra spaces or quotes
- Check OpenAI/HuggingFace account status

### Services Not Starting
```bash
# View logs
docker-compose logs backend
docker-compose logs postgres

# Restart services
docker-compose restart
```

### Memory Issues
- Whisper models require 2-4GB RAM
- Increase Docker memory limit in Docker Desktop settings
- Consider using 'tiny' or 'base' Whisper model

## Stop Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## Get Help

- [Full Documentation](README.md)
- [GitHub Issues](https://github.com/CrashBytes/agentic-meeting-transcription-tutorial/issues)
- [Tutorial Article](https://crashbytes.com/articles/tutorial-agentic-meeting-transcription-ai-agents-rag-enterprise-deployment-2025)

---

**Ready in 10 minutes** | Built by [CrashBytes](https://crashbytes.com)
