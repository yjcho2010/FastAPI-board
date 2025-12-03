from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router
app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# [변경점] 루트 경로 접속 시 메시지 반환 (배포 확인용)
@app.get("/")
def read_root():
    return {"message": "Hello! Server is deployed successfully."}

'''
test12040050
'''

app.include_router(question_router.router)

app.include_router(answer_router.router)

