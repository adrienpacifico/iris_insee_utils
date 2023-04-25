install_library:
	pip install -r requirements.txt
	pip install -e .
download_and_initialize_data:
	python ./iris_insee_utils/download_data.py
launch_test:
	pytest -n auto --cov=iris_insee_utils --cov-report=xml