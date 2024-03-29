Summary: The Open Racing Car Simulator
Name: TORCS
Version: 1.3.4
Release: 1
Epoch: 1
Source: TORCS-%{version}-src.tgz
Group: Amusements/Games
BuildRoot: %{_tmppath}/%{name}-buildroot
Copyright: GPL
BuildArch: i386
URL: http://torcs.org
Packager: Eric Espi� <Eric.Espie@free.fr>
Requires: TORCS-data

%description
A 3D racing car simulator using OpenGL.

%prep
%setup -n torcs-1.3.4

%build
export TORCS_BASE=`pwd` MAKE_DEFAULT=`pwd`/Make-default.mk
./configure --prefix=%{_prefix}
make

%install
make install DESTDIR=$RPM_BUILD_ROOT/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/bin/*
%{_prefix}/lib/*
%{_prefix}/share/games/torcs/*

%changelog
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
