%global gitid g2b1a638.81-1

Name:           spotify
Version:        0.9.11.27
Release:        0%{?dist}.os1
Summary:        Spotify desktop client
Group:          Applications/Multimedia
License:        Commercial
URL:            http://www.spotify.com/

Source0:        http://repository.spotify.com/pool/non-free/s/spotify/spotify-client_%{version}.%{gitid}_amd64.deb
Source1:	https://kojipkgs.fedoraproject.org//packages/libgcrypt/1.5.3/3.fc21/x86_64/libgcrypt-1.5.3-3.fc21.x86_64.rpm
Source10:	sslsymbol.map
Source11:	libcrypto-symbols.c
Source12:	libssl-symbols.c

BuildRequires:	openssl-devel

%description
%{summary}

%prep
%setup -c -T
ar p %{SOURCE0} data.tar.gz | tar zx
rpm2cpio %{SOURCE1} | cpio -id

%build
gcc -shared -o libcrypto.so.1.0.0 -Wl,--version-script,%{SOURCE10} %{SOURCE11} -fPIC -lcrypto
gcc -shared -o libssl.so.1.0.0 -Wl,--version-script,%{SOURCE10} %{SOURCE12} -fPIC -lssl

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} %{buildroot}/opt/spotify \
         %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/pixmaps
mv opt/spotify/spotify-client %{buildroot}/opt/spotify/spotify-client
mv lib{crypto,ssl}.so.1.0.0 %{buildroot}/opt/spotify/spotify-client/Data
mv usr/lib64/libgcrypt.so.11.8.2 %{buildroot}/opt/spotify/spotify-client/Data/libgcrypt.so.11
ln -s %{_libdir}/libudev.so.1 %{buildroot}/opt/spotify/spotify-client/Data/libudev.so.0
ln -s /opt/spotify/spotify-client/spotify %{buildroot}%{_bindir}/spotify
ln -s /opt/spotify/spotify-client/spotify.desktop %{buildroot}%{_datadir}/applications
ln -s /opt/spotify/spotify-client/Icons/spotify-linux-512.png %{buildroot}%{_datadir}/pixmaps/spotify-client.png

%filter_from_requires /libcef.so/d;
%filter_from_requires /libcrypto.so.1.0.0/d;
%filter_from_requires /libssl.so.1.0.0/d;
%filter_from_provides /libcrypto.so.1.0.0/d;
%filter_from_provides /libssl.so.1.0.0/d;
%filter_from_provides /libudev.so.0/d;
%filter_from_provides /libgcrypt.so.11/d;
%filter_setup

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/*/*
/opt/spotify

%changelog
* Tue Oct  7 2014 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Update to 0.9.11.
- Bundle libgcrypt.so.11 for Fedora 21

* Wed May 28 2014 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Update to 0.9.10.
- Add a symbolic link from libudev.so.1 to libudev.so.0
- Build real versioned fake ssl libs
- Install in /opt

* Tue Jan  7 2014 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Update to 0.9.4.

* Thu May  9 2013 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Update to 0.9.0.

* Thu Jan  3 2013 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Update to 0.8.8.

* Wed Jun 13 2012 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Update to 0.8.3.

* Wed Apr 25 2012 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Update to 0.8.2.

* Fri Jan 27 2012 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Create dummy libssl0.9.8.

* Sun Dec 11 2011 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Initial.
