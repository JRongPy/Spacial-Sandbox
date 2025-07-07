// Simple WebSocket client
const ws = new WebSocket('ws://localhost:8000/ws');
ws.onmessage = (event) => {
    console.log('feedback', event.data);
};
