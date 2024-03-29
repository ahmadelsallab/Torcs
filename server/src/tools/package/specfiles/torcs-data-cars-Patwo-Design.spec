Summary: TORCS - Patwo Design Car Pack
Name: TORCS-data-cars-Patwo-Design
Version: 1.3.4
Release: 1
Epoch: 1
Source: TORCS-%{version}-data-cars-Patwo-Design.tgz
Group: Amusements/Games
BuildRoot: %{_tmppath}/%{name}-buildroot
Copyright: Patrick Wisselo,  Patwo Design Production 1999, 2002
BuildArch: noarch
URL: http://torcs.org
Packager: Eric Espi� <Eric.Espie@free.fr>
Requires: TORCS

%description
Patwo Design Car Pack for TORCS.
PLEASE, these files may NOT BE EDITED or COPIED in any way.
http://www.patwodesign.com

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
* Thu Jan 2 2003 Eric Espi� <Eric.Espie@free.fr> 1.2.0
- cars compiled

* Mon Jul 15 2002 Eric Espi� <Eric.Espie@free.fr> 1.1.0-2
- improved specfile

* Sat Jul 13 2002 Eric Espi� <Eric.Espie@free.fr> 1.1.0
- initial RPM
