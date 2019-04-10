PY=$(shell which python3 || which python)

env/.created:
	echo $(PY)
	$(PY) -m venv env
	touch $@

env/.installed: env/.created
	pip install -r requirements.txt
	touch $@

mock_client: env/.installed
	sh -c '. env/bin/activate ; python mock_client.py'

run: env/.installed
	sh -c '. env/bin/activate ; python app.py'
