from fastapi import FastAPI
from fastapi.responses import JSONResponse
from classifier import AI_classifier

from pydantic import BaseModel

app = FastAPI()

class ClassificationValidator(BaseModel):
    email: str

def prompt_generator(email: str) -> str:
    with open(r'D:\IT\AI\teaching\GenAI_module_1\Projects\Project3\prompts.txt', 'r') as data:
        prompt: str = data.read()

    final_prompt = prompt.format(input=email)

    return final_prompt

@app.post("/email-classifier")
def email_classifier(request: ClassificationValidator):
    email_to_classify = request.email
    final_prompt = prompt_generator(email_to_classify)
    output = AI_classifier(final_prompt)
    res = {"classification": output}
    return JSONResponse(content = res, status_code=200)
