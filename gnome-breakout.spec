%define name     gnome-breakout
%define version  0.3.1
%define release  1mdk
%define prefix   /usr

Summary		: A cool game for GNOME.
Name		: %{name}
Version		: %{version}
Prefix 		: %{prefix}
Release         : %{release}
Copyright	: GPL
Group		: Games/Arcade
Source		: http://www.tuial.com/~alcaron/software/%{name}-%{version}.tar.bz2
Buildroot	: %{_tmppath}/%{name}-%{version}-root

%description
A breakout clone for GNOME.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build
CFLAGS="$RPM_OPT_FLAGS" \
	./configure --prefix=%{prefix}
make


%install
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{prefix}/bin/gnome-breakout
%{prefix}/share/pixmaps/gnome-breakout/*
%{prefix}/share/gnome/apps/Games/gnome-breakout.desktop

%changelog
* Tue Apr 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-1mdk
- first spec
- new in contribs
