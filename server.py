import asyncio
import websockets
import os

PORT = int(os.environ.get("PORT", 10000))

async def handler(websocket):
    print("Client connected")

    try:
        async for message in websocket:
            print("Received:", message)

            await websocket.send(f"Echo: {message}")

    except:
        print("Client disconnected")


async def main():

    print(f"Server running on port {PORT}")

    async with websockets.serve(
        handler,
        "0.0.0.0",
        PORT
    ):
        await asyncio.Future()


asyncio.run(main())
