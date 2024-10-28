web: gunicorn app:app
web: bash render-build.sh
web: streamlit run comparison.py --server.port $PORT --server.address 0.0.0.0
web: streamlit run extraction.py --server.port $PORT --server.address 0.0.0.0
