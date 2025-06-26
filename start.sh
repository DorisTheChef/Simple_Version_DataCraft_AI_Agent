#!/bin/bash

echo "🚀 Starting Virtual Patient Generator..."
echo "📱 Opening frontend interface..."

# Start Flask backend in background
python3 app.py &
FLASK_PID=$!

# Wait a moment for Flask to start
sleep 3

# Open frontend in default browser
open frontend/index.html

echo "✅ System started!"
echo "🌐 Frontend opened automatically"
echo "🔧 Backend running at: http://127.0.0.1:5001"
echo "⏹️  Press Ctrl+C to stop server"

# Wait for user to stop
wait $FLASK_PID 