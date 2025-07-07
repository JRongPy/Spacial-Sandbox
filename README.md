# Spacial Sandbox

This project demonstrates a minimal sandbox for placing equipment in a room. It
provides a simple API for issuing placement commands and receiving immediate
feedback about clearance and structural constraints.

## Running the demo server

```bash
pip install fastapi uvicorn pydantic
python examples/mcp_integration.py
```

Open `web/index.html` in your browser to connect to the WebSocket server and see
console feedback.
