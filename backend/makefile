dev:
	poetry run python3 backend/__main__.py dev

secure-dev:
	poetry run python3 backend/__main__.py secure-dev

init:
	poetry install
	@mkdir secrets
	@head -c 16 /dev/urandom > secrets/secret_key.txt
	@echo "\033[33;1mPlease create the file ./secret/client_secret.json from the google API console (https://support.google.com/cloud/answer/6158849)\033[0m" 

# poetry run python3 -c "import backend; backend.run_prod()"