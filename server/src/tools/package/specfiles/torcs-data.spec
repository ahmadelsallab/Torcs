Summary: The Open Racing Car Simulator - DATA
Name: TORCS-data
Version: 1.3.4
Release: 1
Epoch: 1
Source: TORCS-%{version}-data.tgz
Group: Amusements/Games
BuildRoot: %{_tmppath}/%{name}-buildroot
Copyright: GPL
BuildArch: noarch
URL: http://torcs.org
Packager: Eric Espi� <Eric.Espie@free.fr>

%description
Mandatory data (images, fonts, menus...) for TORCS

%prep
%setup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/games/torcs
cp -r * $RPM_BUILD_ROOT/%{_prefix}/share/games/torcs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/share/games/torcs/*

%changelog
* Mon Mar 24 2003 Eric Espi� <Eric.Espie@free.fr> 1.2.0
- new version

* Mon Jul 15 2002 Eric Espi� <Eric.Espie@free.fr> 1.1.0-2
- improved specfile

* Sat Jul 13 2002 Eric Espi� <Eric.Espie@free.fr> 1.1.0
- initial RPM
