%global debug_package %{nil}
%global __os_install_post %{nil}

Name:           spotify
Version:        %{version}
Release:        0%{?dist}.os1
Summary:        Spotify desktop client
Group:          Applications/Multimedia
License:        Commercial
URL:            http://www.spotify.com/

Source0:        http://repository.spotify.com/pool/non-free/s/spotify-client/spotify-client_%{version}.%{gitid}_amd64.deb
Source10:	compatlib.py
Source11:	libcurl.json

BuildRequires:	libcurl-devel

%description
%{summary}

%prep
%setup -c -T
ar p %{SOURCE0} data.tar.gz | tar zx

%build
python3 %{SOURCE10} %{SOURCE11}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir} \
         %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/pixmaps
mv usr/bin/spotify %{buildroot}%{_bindir}
mv usr/share/spotify %{buildroot}%{_datadir}
mv libcurl-gnutls.so.4 %{buildroot}/%{_datadir}/%{name}
ln -s %{_datadir}/%{name}/spotify.desktop %{buildroot}%{_datadir}/applications/spotify.desktop
ln -s %{_datadir}/%{name}/icons/spotify-linux-512.png %{buildroot}%{_datadir}/pixmaps/spotify-client.png

%filter_from_requires /libcef.so/d;
%filter_from_requires /libcurl-gnutls.so.4/d;
%filter_from_provides /libcurl-gnutls.so.4/d;
%filter_setup

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-client.png

%changelog
* Tue Feb 16 2021 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Update to 1.1.42.622

* Sat Aug 11 2018 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Update to 1.0.80.480
- Add a new libcurl-gnutls compatibility hack and drop the ssl hacks

* Thu Dec 3 2015 Oskari Saarenmaa <oskari@saarenmaa.fi>
- Update to 1.0.19.106

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
