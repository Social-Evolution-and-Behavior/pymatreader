# simple makefile to simplify repetetive build env management tasks under posix

# caution: testing won't work on windows, see README

flake:
	@if command -v flake8 > /dev/null; then \
		echo "Running flake8"; \
		flake8 --count pymatreader; \
	else \
		echo "flake8 not found, please install it!"; \
		exit 1; \
	fi;
	@echo "flake8 passed"
