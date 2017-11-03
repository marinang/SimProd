export DECFILESROOT=$(shell pwd)

all: doc/newdecfiles.txt .create_options.stamp 

.create_options.stamp: $(wildcard $(DECFILESROOT)/dkfiles/*.dec)
	$(DECFILESROOT)/cmt/create_options.py
	touch $@

doc/newdecfiles.txt: .create_options.stamp
	$(DECFILESROOT)/cmt/listNewEvtTypes.py
