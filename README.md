# Agentic Meeting Transcription System

A production-ready, enterprise-grade meeting transcription system powered by multiple AI agents working in concert. This system provides real-time audio transcription, speaker diarization, intelligent meeting analysis, RAG-powered context retrieval, and automated action item extraction.

## 🎯 Features

- **Real-time Transcription**: WebSocket-based audio streaming with OpenAI Whisper
- **Speaker Diarization**: Automatic speaker identification using Pyannote.audio
- **RAG Integration**: Vector-based semantic search across meeting history with Qdrant
- **Multi-Agent Analysis**: Parallel summarization and action item extraction
- **LangGraph Orchestration**: Sophisticated multi-agent workflow management
- **Production Ready**: Docker containerization and Kubernetes deployment manifests
- **Enterprise Scale**: Handles concurrent meetings with resource management

## 📋 Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Meeting Audio Stream                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              Transcription Agent (Whisper)                   │
│  ┌────────────────┐           ┌──────────────────┐         │
│  │  Audio Chunks  │  ───────► │  Text Segments   │         │
│  └────────────────┘           └──────────────────┘         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         Speaker Diarization Agent (Pyannote)                │
│  ┌────────────────┐           ┌──────────────────┐         │
│  │  Audio Signal  │  ───────► │  Speaker Labels  │         │
│  └────────────────┘           └──────────────────┘         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                 LangGraph Orchestrator                       │
│                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ │
│  │   Context    │───►│ Summarizer   │───►│ Action Items │ │
│  │   Retrieval  │    │    Agent     │    │    Agent     │ │
│  │  (RAG/Qdrant)│    │  (GPT-4)     │    │   (GPT-4)    │ │
│  └──────────────┘    └──────────────┘    └──────────────┘ │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                      PostgreSQL                              │
│  Stores: Meetings, Transcripts, Summaries, Action Items    │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Technology Stack

- **Backend Framework**: FastAPI 0.104+
- **Agent Orchestration**: LangGraph 0.0.40+, LangChain 0.1.0+
- **Speech-to-Text**: OpenAI Whisper (openai-whisper 20231117)
- **Speaker Diarization**: Pyannote.audio 3.1+
- **Vector Database**: Qdrant 1.7+
- **LLM**: OpenAI GPT-4 Turbo
- **Database**: PostgreSQL 16+
- **Cache**: Redis 7+
- **Containerization**: Docker, Docker Compose
- **Orchestration**: Kubernetes 1.28+
- **Frontend**: Next.js 14+ with TypeScript
- **WebSocket**: python-socketio 5.10+

## 📦 Installation

### Prerequisites

- Python 3.11+
- PostgreSQL 16+
- Redis 7+
- Qdrant (Docker or Cloud)
- OpenAI API key
- Hugging Face token (for Pyannote)
- Node.js 18+ (for frontend)

### Quick Start with Docker Compose

```bash
# Clone the repository
git clone https://github.com/CrashBytes/agentic-meeting-transcription-tutorial.git
cd agentic-meeting-transcription-tutorial

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Start all services
docker-compose up -d

# The system will be available at:
# - Backend API: http://localhost:8000
# - Frontend: http://localhost:3000
# - Qdrant: http://localhost:6333
```

### Manual Installation

```bash
# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Install Whisper model
python -c "import whisper; whisper.load_model('base')"

# Frontend setup
cd ../frontend
npm install

# Database setup
cd ../backend
alembic upgrade head
```

## 🚀 Usage

### Starting the Backend

```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Starting the Frontend

```bash
cd frontend
npm run dev
```

### API Endpoints

#### Start Meeting
```bash
POST /api/meetings
{
  "title": "Product Strategy Discussion",
  "participants": ["alice@example.com", "bob@example.com"]
}
```

#### Stream Audio (WebSocket)
```javascript
const ws = new WebSocket('ws://localhost:8000/ws/meetings/{meeting_id}/audio');
ws.send(audioChunk);  // Send audio as binary data
```

#### Get Meeting Analysis
```bash
GET /api/meetings/{meeting_id}/analysis
```

#### Retrieve Meeting Summary
```bash
GET /api/meetings/{meeting_id}/summary?detail=medium
# detail: brief, medium, detailed
```

#### Extract Action Items
```bash
GET /api/meetings/{meeting_id}/action-items
```

## 🏗️ Project Structure

```
agentic-meeting-transcription-tutorial/
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   ├── transcription_agent.py      # Whisper integration
│   │   │   ├── diarization_agent.py        # Pyannote speaker detection
│   │   │   ├── context_retrieval_agent.py  # RAG with Qdrant
│   │   │   ├── summarization_agent.py      # LangChain summarizer
│   │   │   └── action_items_agent.py       # Structured extraction
│   │   ├── orchestration/
│   │   │   ├── graph.py                    # LangGraph workflow
│   │   │   └── state.py                    # Shared state management
│   │   ├── api/
│   │   │   ├── meetings.py                 # REST endpoints
│   │   │   └── websocket.py                # Audio streaming
│   │   ├── models/
│   │   │   ├── meeting.py                  # SQLAlchemy models
│   │   │   └── schemas.py                  # Pydantic schemas
│   │   ├── services/
│   │   │   ├── audio_processor.py          # Audio handling
│   │   │   └── vector_store.py             # Qdrant integration
│   │   ├── config.py                       # Configuration
│   │   └── main.py                         # FastAPI app
│   ├── alembic/                            # Database migrations
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── components/
│   │   ├── MeetingRecorder.tsx             # Audio recording UI
│   │   ├── TranscriptDisplay.tsx           # Real-time transcript
│   │   ├── MeetingAnalysis.tsx             # Summary & action items
│   │   └── MeetingHistory.tsx              # Past meetings
│   ├── pages/
│   │   ├── index.tsx                       # Home page
│   │   ├── meetings/
│   │   │   ├── [id].tsx                    # Meeting detail
│   │   │   └── new.tsx                     # New meeting
│   │   └── api/                            # Next.js API routes
│   ├── lib/
│   │   ├── websocket.ts                    # WebSocket client
│   │   └── api.ts                          # API client
│   ├── public/
│   ├── Dockerfile
│   ├── package.json
│   └── tsconfig.json
├── kubernetes/
│   ├── backend-deployment.yaml
│   ├── frontend-deployment.yaml
│   ├── postgres-statefulset.yaml
│   ├── redis-deployment.yaml
│   ├── qdrant-deployment.yaml
│   ├── ingress.yaml
│   └── configmap.yaml
├── docker-compose.yml
├── .env.example
├── LICENSE
└── README.md
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
# OpenAI Configuration
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4-turbo-preview

# Hugging Face (for Pyannote)
HUGGINGFACE_TOKEN=hf_...

# Database
POSTGRES_USER=meeting_user
POSTGRES_PASSWORD=secure_password
POSTGRES_DB=meeting_transcription
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Redis
REDIS_URL=redis://localhost:6379/0

# Qdrant
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=  # Optional for cloud instance

# Application
DEBUG=False
LOG_LEVEL=INFO
MAX_AUDIO_DURATION=7200  # 2 hours in seconds
CHUNK_SIZE=1024  # Audio chunk size in bytes
```

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest tests/ -v --cov=app

# Frontend tests
cd frontend
npm test

# Integration tests
cd backend
pytest tests/integration/ -v
```

## 🐳 Docker Deployment

### Build Images

```bash
# Backend
docker build -t meeting-transcription-backend:latest ./backend

# Frontend
docker build -t meeting-transcription-frontend:latest ./frontend
```

### Run with Docker Compose

```bash
docker-compose up -d
```

Services:
- **Backend**: http://localhost:8000
- **Frontend**: http://localhost:3000
- **Qdrant Dashboard**: http://localhost:6333/dashboard
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

## ☸️ Kubernetes Deployment

### Prerequisites

- Kubernetes cluster (v1.28+)
- kubectl configured
- Persistent Volume provisioner

### Deploy

```bash
# Create namespace
kubectl create namespace meeting-transcription

# Apply configurations
kubectl apply -f kubernetes/ -n meeting-transcription

# Check deployment status
kubectl get pods -n meeting-transcription

# Get service URLs
kubectl get ingress -n meeting-transcription
```

### Scaling

```bash
# Scale backend
kubectl scale deployment backend --replicas=5 -n meeting-transcription

# Scale frontend
kubectl scale deployment frontend --replicas=3 -n meeting-transcription
```

## 📊 Monitoring

### Metrics Endpoints

- **Backend Health**: `GET /health`
- **Metrics**: `GET /metrics` (Prometheus format)
- **Database Status**: `GET /health/db`
- **Vector Store Status**: `GET /health/vectordb`

### Key Metrics

- `meeting_transcriptions_total`: Total meetings transcribed
- `transcription_duration_seconds`: Time to transcribe audio
- `diarization_duration_seconds`: Time for speaker identification
- `rag_query_duration_seconds`: Vector search latency
- `agent_execution_duration_seconds`: Agent processing time
- `websocket_connections_active`: Active audio streams

## 🔒 Security Considerations

- **API Authentication**: Implement JWT tokens for production
- **Rate Limiting**: Configured per-client limits
- **Input Validation**: Pydantic models validate all inputs
- **Audio Encryption**: Use WSS (WebSocket Secure) in production
- **Database Security**: Use strong passwords, connection pooling
- **API Key Management**: Store in secrets management service
- **CORS**: Configured for specific origins only

## 🎯 Performance Optimization

### Backend

- **Connection Pooling**: SQLAlchemy engine with pool size 20
- **Async Processing**: FastAPI async endpoints
- **Caching**: Redis for frequent queries
- **Batch Processing**: Vectorization in batches of 100
- **Model Loading**: Lazy load Whisper/Pyannote models

### Database

- **Indexes**: B-tree on meeting_id, participant_id, timestamp
- **Vector Index**: HNSW index in Qdrant for fast similarity search
- **Partitioning**: Time-based partitioning for transcripts table

### Resource Limits (Kubernetes)

```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "4Gi"
    cpu: "2000m"
```

## 🐛 Troubleshooting

### Whisper model not loading
```bash
python -c "import whisper; whisper.load_model('base', download_root='/path/to/models')"
```

### Pyannote authentication failed
```bash
huggingface-cli login
# Enter your HF token
```

### WebSocket connection refused
- Check CORS settings in `app/config.py`
- Verify firewall allows WebSocket connections
- Ensure frontend uses correct WebSocket URL

### Vector search returns no results
- Verify Qdrant is running: `curl http://localhost:6333/health`
- Check collection exists: `curl http://localhost:6333/collections`
- Rebuild embeddings if needed

## 📚 Learn More

- [Tutorial Article](https://crashbytes.com/articles/tutorial-agentic-meeting-transcription-ai-agents-rag-enterprise-deployment-2025)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [Pyannote.audio](https://github.com/pyannote/pyannote-audio)
- [Qdrant Documentation](https://qdrant.tech/documentation/)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for Whisper and GPT-4
- Pyannote team for speaker diarization
- LangChain team for agent framework
- Qdrant team for vector database

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/CrashBytes/agentic-meeting-transcription-tutorial/issues)
- **Discussions**: [GitHub Discussions](https://github.com/CrashBytes/agentic-meeting-transcription-tutorial/discussions)
- **Blog**: [CrashBytes](https://crashbytes.com)

---

**Built with ❤️ by CrashBytes** | [Website](https://crashbytes.com) | [Twitter](https://twitter.com/crashbytes)
