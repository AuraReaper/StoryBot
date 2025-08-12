# StoryBot - AI-Powered Interactive Story Generator

StoryBot is a full-stack web application that generates interactive, branching narratives using AI. Users can input themes and experience dynamic storytelling with multiple choice paths leading to different endings.

## 🚀 Features

- **AI-Powered Story Generation**: Leverages Google's Gemini 1.5 Flash model via LangChain for creative story generation
- **Interactive Branching Narratives**: Dynamic story paths with multiple choice options
- **Real-time Story Processing**: Asynchronous job processing with status tracking
- **Session Management**: Persistent story sessions for continued gameplay
- **Responsive Frontend**: Modern React-based UI with smooth navigation
- **RESTful API**: Well-structured FastAPI backend with automatic documentation

## 🛠 Tech Stack

### Backend
- **FastAPI** - High-performance Python web framework
- **SQLAlchemy** - Database ORM with PostgreSQL support
- **LangChain** - AI/LLM integration framework
- **Google Gemini AI** - Large language model for story generation
- **Pydantic** - Data validation and settings management
- **Uvicorn** - ASGI server for production deployment

### Frontend
- **React 19** - Modern frontend framework
- **Vite** - Fast build tool and development server
- **React Router** - Client-side routing
- **Axios** - HTTP client for API communication
- **ESLint** - Code linting and formatting

### Database
- **SQLite** (Development) / **PostgreSQL** (Production)
- Structured story and node relationships
- JSON field support for dynamic options

## 📁 Project Structure

```
├── backend/
│   ├── core/           # Core business logic
│   ├── models/         # Database models
│   ├── schemas/        # Pydantic schemas
│   ├── routers/        # API route handlers
│   └── db/            # Database configuration
└── frontend/
    ├── src/
    │   ├── components/ # React components
    │   └── App.jsx    # Main application
    └── public/        # Static assets
```

## 🚦 Getting Started

### Prerequisites
- Python 3.13+
- Node.js 18+
- Google Gemini API key

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env  # Add your GEMINI_API_KEY
python main.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 🔧 Configuration

### Environment Variables
- `GEMINI_API_KEY` - Google Gemini API key for AI story generation
- `DATABASE_URL` - PostgreSQL connection string (production)
- `ALLOWED_ORIGINS` - CORS allowed origins
- `DEBUG` - Development mode toggle

## 📖 API Documentation

Once running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🎮 How It Works

1. **Theme Input**: User provides a story theme (e.g., "Harry Potter", "Space Adventure")
2. **AI Generation**: Backend uses Gemini AI to create a structured story with branching paths
3. **Database Storage**: Story nodes and relationships are stored with session tracking
4. **Interactive Gameplay**: Frontend renders story content with clickable options
5. **Dynamic Progression**: User choices determine story path and ending

## 🏗 Architecture Highlights

- **Microservices Ready**: Modular backend design with clear separation of concerns
- **Async Processing**: Background job processing for story generation
- **Type Safety**: Full Pydantic validation and TypeScript-ready schemas
- **Scalable Database**: Relational design supporting complex story structures
- **Modern Frontend**: Component-based React architecture with hooks

## 🚀 Deployment

The application is configured for deployment on Choreo platform with:
- Containerized backend service
- Environment-based configuration
- Production database support
- CORS configuration for cross-origin requests

## 📝 License

This project is open source and available under the MIT License.