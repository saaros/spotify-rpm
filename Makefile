version = 1.2.63.394
gitid = g126b0d89
deb = spotify-client_$(version).$(gitid)_amd64.deb

rpm: $(deb)
	rpmbuild \
		--define '_sourcedir $(PWD)' \
		--define 'gitid $(gitid)' \
		--define 'version $(version)' \
		-bb spotify.spec

$(deb):
	curl -O https://repository.spotify.com/pool/non-free/s/spotify-client/$@
