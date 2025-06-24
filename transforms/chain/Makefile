REPOROOT=../..

clean:
	rm -fr venv

test-src:
	python -m venv venv
	source venv/bin/activate && pip install $(REPOROOT)/data-processing-lib
	source venv/bin/activate &&  pip install "$(REPOROOT)/transforms[lang_id, doc_quality]"
	source venv/bin/activate && pip install pytest
	source venv/bin/activate && pytest test

