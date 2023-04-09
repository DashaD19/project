from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update this with the origin of your frontend app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


tasks = [
{

        "title": "Le rhumes",
        "description": "Nouveau médicament contre le rhume",
        "status": "nouveau"
      },
      {
        "title": "Soins dentaires",
        "description": "Comment prendre soin de ses dents",
        "status": "non lu"
      },
      {
        "title": "La grippe",
        "description": "Les avantages du vaccin contre la grippe",
        "status": "lu"
      },
      {
        "title": "Maladies cardiaques",
        "description": "Les meilleures habitudes alimentaires",
        "status": "nouveau"
      },
      {
        "title": "Les allergies",
        "description": "Nouvelle thérapie pour les allergies saisonnières",
        "status": "non lu"
      },
      {
        "title": "Bien-être mental",
        "description": "Comment maintenir une bonne santé mentale",
        "status": "nouveau"
      },
      {
        "title": "Diabète",
        "description": "Comment bien manger avec le diabète",
        "status": "non lu"
      },
      {
        "title": "L'acné",
        "description": "Nouvelle crème pour l'acné",
        "status": "lu"
    },
    {
        "title": "Sommeil et santé",
        "description": "Les effets du manque de sommeil sur la santé",
        "status": "lu"
    }
]

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.post("/tasks")
async def add_task(task: dict):
    tasks.append(task)
    return task