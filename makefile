.DEFAULT_GOAL := test

FILES :=						\
	# IDB1.html					\
	IDB1.log					

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint3.5
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.4
    AUTOPEP8 := autopep8
endif

config:
	git config -l
	
.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f .coverage
	rm -f .pylintrc
	rm -f *.pyc
	rm -f IMDB1.html
	rm -f IMDB1.log
	rm -r __pycache__

format:
	$(AUTOPEP8) -i run.py
	$(AUTOPEP8) -i app/models.py
	$(AUTOPEP8) -i app/tests.py
	$(AUTOPEP8) -i app/views.py
	$(AUTOPEP8) -i app/__init__.py

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

# TODO
TestApp:
	python3.5 app/tests.py

IDB1.log:
	git log > IDB1.log

# FIXME ImportError: No module named 'flask'
IDB1.html:
	pydoc3.5 app/views.py

test: IDB1.log check
# TODO add reference to test
# test: IDB1.html IDB1.log check

versions:
	which make
	make --version
	@echo
	which git
	git --version
	@echo
	which $(PYTHON)
	$(PYTHON) --version
	@echo
	which $(PIP)
	$(PIP) --version
	@echo
	which $(PYLINT)
	$(PYLINT) --version
	@echo
	which $(COVERAGE)
	$(COVERAGE) --version
	@echo
	which $(PYDOC)
	$(PYDOC) --version
	@echo
	which $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	$(PIP) list