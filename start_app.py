import webbrowser
import threading
import time
import os
from app import app

def open_frontend():
    """Open the frontend HTML file in the default browser"""
    time.sleep(2)  # Wait for Flask to start
    frontend_path = os.path.join(os.path.dirname(__file__), 'frontend', 'index.html')
    webbrowser.open(f'file://{frontend_path}')

if __name__ == '__main__':
    print("🚀 启动虚拟病人生成器...")
    print("📱 正在打开前端界面...")
    
    # Start frontend in a separate thread
    frontend_thread = threading.Thread(target=open_frontend)
    frontend_thread.daemon = True
    frontend_thread.start()
    
    # Start Flask backend
    print("🔧 后端服务器启动中...")
    print("🌐 访问地址: http://127.0.0.1:5001")
    print("📋 API端点: http://127.0.0.1:5001/generate_patients")
    print("⏹️  按 Ctrl+C 停止服务器")
    print("-" * 50)
    
    app.run(host='0.0.0.0', port=5001, debug=False) 