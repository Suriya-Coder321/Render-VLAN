import asyncio
import websockets

async def handler(websocket):
    print("Client connected")

    try:
        async for message in websocket:
            print("Received:", message)

            await websocket.send(f"Echo: {message}")

    except:
        print("Client disconnected")


async def main():

    print("Server running on port 10000")

    async with websockets.serve(
        handler,
        "0.0.0.0",
        10000
    ):
        await asyncio.Future()


asyncio.run(main())
