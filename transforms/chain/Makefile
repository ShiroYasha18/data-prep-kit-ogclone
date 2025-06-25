REPOROOT=../..
include $(REPOROOT)/.make.defaults


clean:
	rm -fr venv

venv::
	@# Help: Create the virtual environment using pyproject.toml
	$(PYTHON) -m venv venv
	source venv/bin/activate; \
	$(PYTHON) -m pip install -e $(REPOROOT)/data-processing-lib; \
	$(PYTHON) -m pip install -e "$(REPOROOT)/transforms[lang_id, doc_quality]"; \
	$(PYTHON) -m pip install pytest

test-src: venv
	source venv/bin/activate; \
	$(PYTHON) -m pip list; \
	pytest test

