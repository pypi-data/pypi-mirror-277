# CryptLab

An E2EE Exploitation Practice Infrastructure

## How To Run

This works on my setup.

1. Make venv `python -m venv .venv` and activate it `source .venv/bin/activate`
2. Install requirements `pip install loguru fastapi python-decouple`
3. Install cryptlab editable locally `pip install -e .`
4. Run the orchestrator on one terminal `ORCHESTRATOR_WEBAPP_PORT=8000 FLAG="flag{test}" python cryptlab/orchestrator/main.py`
5. Open the browser webapp `http://localhost:8000`
6. Watch for the server logs for a long token
7. Paste this token in `examples/server.py` at the top
8. Run `python examples/server.py` to connect the server script to the orchestrator
9. Open `http://localhost:8000/docs` to open the Swagger docs
10. Use the Swagger docs to send a post request to `/api/v1/exec` to execute some actions (Use the example below and the token you used earlier). You should see the corresponding actions being run against your server!

Use the following example execution config:

```json
{
  "n_clients": 2,
  "actions": [
    [0, "SAVE_MESSAGE", "Hello"],
    [1, "SAVE_MESSAGE", "World"],
    [0, "RETRIEVE_MESSAGES"]
  ]
}
```

## Stuff to try out

- Open a serverscript (`python examples/server.py`) and then open another one in another terminal. The first one should get immediately disconnected.
- Open two serverscripts, one locally and one remotely (i.e. send the post to `/api/v1/exec`) and see that both clients will execute.
- Make a serverscript sleep with `time.sleep(10)`. The execution will abort because you took too long to reply to the client (only works for remote clients).
- Make a client and server go into an infinite loop with the LOOP command. This will also abort execution.

## Important Notes

- If you restart the orchestrator server, refresh the page so that the server can re-register the tokens (the orchestrator is stateless)
- You can also run clients locally `python examples/client.py`! You can change the execution config at the bottom.

## Known Bugs

- Disconnecting a serverscript and reconnecting a new one makes the SERVER_SCRIPT_DISCONNECTED event fire twice in the websocket.
