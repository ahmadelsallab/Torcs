Summary: TORCS - Extra car pack
Name: TORCS-data-cars-extra
Version: 1.3.4
Release: 1
Epoch: 1
Source: TORCS-%{version}-data-cars-extra.tgz
Group: Amusements/Games
BuildRoot: %{_tmppath}/%{name}-buildroot
Copyright: GPL
BuildArch: noarch
URL: http://torcs.org
Packager: Eric Espi� <Eric.Espie@free.fr>
Requires: TORCS

%description
Extra car pack for TORCS

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
* Thu Jan 02 2003 Eric Espi� <Eric.Espie@free.fr> 1.2.0
- car compiled
- new packaging
