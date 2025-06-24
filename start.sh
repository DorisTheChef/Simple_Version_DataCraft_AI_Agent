#!/bin/bash

echo "🚀 启动虚拟病人生成器..."
echo "📱 正在打开前端界面..."

# Start Flask backend in background
python3 app.py &
FLASK_PID=$!

# Wait a moment for Flask to start
sleep 3

# Open frontend in default browser
open frontend/index.html

echo "✅ 系统已启动！"
echo "🌐 前端已自动打开"
echo "🔧 后端运行在: http://127.0.0.1:5001"
echo "⏹️  按 Ctrl+C 停止服务器"

# Wait for user to stop
wait $FLASK_PID 