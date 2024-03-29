Summary: TORCS - K1999 Robots
Name: TORCS-robots-K1999
Version: 1.3.4
Release: 1
Epoch: 1
Source:  TORCS-%{version}-src.tgz
Source1: TORCS-%{version}-src-robots-K1999.tgz
Group: Amusements/Games
BuildRoot: %{_tmppath}/%{name}-buildroot
Copyright: GPL
BuildArch: i386
URL: http://torcs.org
Packager: Eric Espi� <Eric.Espie@free.fr>
Requires: TORCS

%description
K1999 Robots for TORCS
by R�mi Coulom <remi.coulom@free.fr>

%prep
%setup -n torcs-1.3.4
%setup -T -D -b 1 -n torcs-1.3.4
cd $RPM_BUILD_DIR/torcs-1.3.4/src/drivers
rm -rf human

%build
export TORCS_BASE=`pwd` MAKE_DEFAULT=`pwd`/Make-default.mk
./configure --prefix=%{_prefix}
make

%install
make install DESTDIR=%{_tmppath}/%{name}-ship
cd %{_tmppath}/%{name}-ship/%{_prefix}/share/games/torcs
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/games/torcs
cp -r drivers $RPM_BUILD_ROOT/%{_prefix}/share/games/torcs
cd -
cd %{_tmppath}/%{name}-ship/%{_prefix}/lib/torcs
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/lib/torcs
cp -r drivers $RPM_BUILD_ROOT/%{_prefix}/lib/torcs
cd -
rm -rf %{_tmppath}/%{name}-ship

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/share/games/torcs/*
%{_prefix}/lib/torcs/*

%changelog
* Mon Aug 25 2003 Eric Espi� <Eric.Espie@free.fr> 1.2.2
- added copying of libraries

* Mon Mar 24 2003 Eric Espi� <Eric.Espie@free.fr> 1.2.0
- new version

* Mon Jul 15 2002 Eric Espi� <Eric.Espie@free.fr> 1.1.0-2
- improved specfile

* Sat Jul 13 2002 Eric Espi� <Eric.Espie@free.fr> 1.1.0
- version 1.1.0

* Mon Dec 17 2001 Eric Espi� <Eric.Espie@free.fr> 1.0.0
- version 1.0.0 final

* Sun Dec  9 2001 Eric Espi� <Eric.Espie@free.fr> 1.0.0-rc5
- installation updates

* Sat Dec  8 2001 Eric Espi� <Eric.Espie@free.fr> 1.0.0-rc4
- initial RPM
