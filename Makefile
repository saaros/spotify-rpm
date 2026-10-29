version = 1.3.4.258
gitid = gc60b10b0946a
deb = spotify-client_$(version).$(gitid)_amd64.deb

rpm: $(deb).ok spotify.spec compatlib.py libcurl.json
	rpmbuild \
		--define '_sourcedir $(PWD)' \
		--define 'gitid $(gitid)' \
		--define 'version $(version)' \
		-bb spotify.spec

# Verify the download against SHA256SUMS; add the new hash there on updates.
$(deb).ok: $(deb) SHA256SUMS
	grep -F '$(deb)' SHA256SUMS | sha256sum -c -
	touch $@

$(deb):
	curl -O https://repository.spotify.com/pool/non-free/s/spotify-client/$@

clean:
	rm -f *.ok compat-*.c compat-*.map libcurl-gnutls.so.4

.PHONY: rpm clean
