from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Welcome to the WebSocket server!")  # Send an initial message

    try:
        while True:
            # Wait to receive a message from the client
            data = await websocket.receive_text()
            print(f"Received message: {data}")

            # Send a response back to the client
            # await websocket.send_text(f"Message received: {data}")

            # Optionally, send periodic messages
            await asyncio.sleep(5)
            await websocket.send_text(f"Hello {data}")
    except Exception as e:
        print("Connection closed:", e)