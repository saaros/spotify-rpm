rpm:
	rpmbuild --define '_sourcedir $(shell pwd)' -bb spotify.spec
