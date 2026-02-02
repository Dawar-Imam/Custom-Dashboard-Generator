#!/bin/bash

echo "Creating virtual environment for backend..."
python -m venv backend/venv

echo "Activating backend venv..."
# Windows
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source backend/venv/Scripts/activate
else
    # Linux / Mac
    source backend/venv/bin/activate
fi

echo "Installing backend requirements..."
pip install -r backend/requirements.txt

# Deactivate backend venv
deactivate

echo "Creating virtual environment for frontend..."
python -m venv frontend/venv

echo "Activating frontend venv..."
# Windows
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source frontend/venv/Scripts/activate
else
    # Linux / Mac
    source frontend/venv/bin/activate
fi

echo "Installing frontend requirements..."
pip install -r frontend/requirements.txt

# Deactivate frontend venv
deactivate

echo "Setup complete!"
