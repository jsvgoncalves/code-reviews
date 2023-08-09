from fastapi import FastAPI, Body, HTTPException, status

app = FastAPI()


IMPORTANT_PEOPLE = ["Boss", "Ned Stark", "Robert Baratheon", "Jaime Lannister"]


def add_to_destination_list(values: list[str], default=["Boss"]):
    to = default
    for value in values:
        if value not in default:
            to.append(value)
    return to


@app.post("/generate_message")
async def generate_message(
    destination: list[str] = Body(),
    message: str = Body("Hello World"),
    include_important_people: bool = False,
):
    """
    Generate a message that will be sent to all the people in the destination list.
    - **destination**: A list of people that should receive the message.
    - **message**: The content of the message that will be sent.
    - **include_important_people**: Whether to include important people in the destination list, default `False`.
    """
    if include_important_people:
        destination = add_to_destination_list(destination, default=IMPORTANT_PEOPLE)
    else:
        destination = add_to_destination_list(destination)
 
    return {"message": message, "destination": destination}
