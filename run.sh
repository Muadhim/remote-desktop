#!/bin/bash

echo "📦 Menginstall dependensi..."

cd server && pip install -r requirements.txt && cd ..
cd agent_client && pip install -r requirements.txt && cd ..
cd control_client && pip install -r requirements.txt && cd ..

echo "✅ Semua dependensi terinstall!"
echo "🚀 Menjalankan server..."
uvicorn server.main:app --reload &
sleep 2

echo "🖥️  Menjalankan agent client..."
python3 agent_client/agent.py &
sleep 2

echo "🕹️  Menjalankan controller client..."
python3 control_client/control.py
