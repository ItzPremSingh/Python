import asyncio
import websockets

# Dictionary to store connected clients
clients = {}


async def handle_client(websocket, path):
    global clients

    # Store the client
    client_id = id(websocket)
    clients[client_id] = websocket

    print(f"Client {client_id} connected.")

    # If there's more than one client, make them friends
    if len(clients) > 1:
        # Get the first client
        first_client_id = list(clients.keys())[0]
        first_client = clients[first_client_id]

        # Make them friends
        await first_client.send("You have a new friend!")
        await websocket.send("You have a new friend!")

    try:
        async for message in websocket:
            print(f"Received message from {client_id}: {message}")
    finally:
        # Remove the client when connection is closed
        del clients[client_id]
        print(f"Client {client_id} disconnected.")


start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
