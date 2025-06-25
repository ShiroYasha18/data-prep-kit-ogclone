REPOROOT=../..

clean:
	rm -fr venv

test-src:
	python -m venv venv
	source venv/bin/activate; \
	pip install $(REPOROOT)/data-processing-lib; \
	pip install "$(REPOROOT)/transforms[lang_id, doc_quality]"; \
	pip install pytest; \
	pytest test

