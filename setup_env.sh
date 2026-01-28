#!/bin/bash
set -e

if ! command -v uv &> /dev/null; then
    echo "UV not found. Installing UV..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

echo ""
echo "Creating virtual environment with UV..."
uv venv .venv

echo ""
echo "Activating environment..."
source .venv/bin/activate

echo ""
echo "Installing dependencies..."
uv pip install -e .

echo ""
echo "Registering Jupyter kernel..."
uv pip install ipykernel
python -m ipykernel install --user --name=rayrl --display-name="Python (rayrl)"