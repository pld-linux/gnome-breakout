%define name     gnome-breakout
%define version  0.3.1
%define release  1mdk
%define prefix   /usr

Summary:	A cool game for GNOME.
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Applications/Games/Arcade
######		Unknown group!
Source0:	http://www.tuial.com/~alcaron/software/%{name}-%{version}.tar.bz2
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A breakout clone for GNOME.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
	./configure --prefix=%{_prefix}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-breakout
%{_datadir}/pixmaps/gnome-breakout/*
%{_applnkdir}/Games/gnome-breakout.desktop
