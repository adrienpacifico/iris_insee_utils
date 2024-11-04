install_library:
	uv sync
	uv pip install -e .
download_and_initialize_data:
	uv run python ./iris_insee_utils/get_iris_contours_data.py
launch_test:
	uv run pytest -n auto --cov=iris_insee_utils --cov-report=xml