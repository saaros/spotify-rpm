version = 1.1.42.622
gitid = gbd112320-37
deb = spotify-client_$(version).$(gitid)_amd64.deb

rpm: $(deb)
	rpmbuild \
		--define '_sourcedir $(PWD)' \
		--define 'gitid $(gitid)' \
		--define 'version $(version)' \
		-bb spotify.spec

$(deb):
	curl -O http://repository.spotify.com/pool/non-free/s/spotify-client/$@
