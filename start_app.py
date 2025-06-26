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
    print("🚀 Starting Virtual Patient Generator...")
    print("📱 Opening frontend interface...")
    
    # Start frontend in a separate thread
    frontend_thread = threading.Thread(target=open_frontend)
    frontend_thread.daemon = True
    frontend_thread.start()
    
    # Start Flask backend
    print("🔧 Backend server starting...")
    print("🌐 Access URL: http://127.0.0.1:5001")
    print("📋 API Endpoint: http://127.0.0.1:5001/generate_patients")
    print("⏹️  Press Ctrl+C to stop server")
    print("-" * 50)
    
    app.run(host='0.0.0.0', port=5001, debug=False) 