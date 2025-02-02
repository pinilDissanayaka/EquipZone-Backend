from server import app
import uvicorn
from database import engine, Base, session
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    uvicorn.run(app,
                port=8000)
