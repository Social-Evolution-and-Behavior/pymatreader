# simple makefile to simplify repetetive build env management tasks under posix

# caution: testing won't work on windows, see README

VERSION_FILE:=VERSION
VERSION:=$(shell cat ${VERSION_FILE})

flake:
	@if command -v flake8 > /dev/null; then \
		echo "Running flake8"; \
		flake8 --count pymatreader; \
	else \
		echo "flake8 not found, please install it!"; \
		exit 1; \
	fi;
	@echo "flake8 passed"

code_quality:
	docker run --interactive --tty --rm --env \
	CODECLIMATE_CODE="$(CURDIR)" --volume "$(CURDIR)":/code \
	--volume /var/run/docker.sock:/var/run/docker.sock \
	--volume /tmp/cc:/tmp/cc  codeclimate/codeclimate analyze

build-doc:
	cd doc; make clean; make html

autobuild-doc:
	sphinx-autobuild doc/source doc/build

clean-dist:
	rm -rf dist
	rm -rf pymatreader.egg-info

upload-dist: clean-dist
	python setup.py sdist
	conda build .
	anaconda upload $(CONDA_PREFIX)/conda-bld/noarch/pymatreader-$(VERSION)-py_0.tar.bz2
	twine upload dist/*