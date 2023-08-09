from fastapi import FastAPI, Body, HTTPException, status

app = FastAPI()


@app.post("/generate_message")
async def generate_message(
    destination: list[str] = Body(),
    message: str = Body("Hello World"),
):
    """
    Generate a message that will be sent to all the people in the destination list.
    - **destination**: A list of people that should receive the message.
    - **message**: The content of the message that will be sent.
    """
    return {"message": message, "destination": ["Boss"] + destination}

