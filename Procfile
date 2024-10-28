web: gunicorn app:app

web: streamlit run extraction.py --server.port $PORT --server.address 0.0.0.0


web: bash render-build.sh && streamlit run extraction.py --server.port $PORT --server.address 0.0.0.0
