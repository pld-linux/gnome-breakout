Summary:	GNOME clone of Breakout the classic arcade game
Summary(pl):	GNOME klon klasycznej gry Breakout
Name:		gnome-breakout
Version:	0.5.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.tuial.com/~alcaron/software/%{name}-%{version}.tar.gz
Source1:	%{name}.png
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
URL:		http://www.senet.com.au/~alcaron/software.html
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GNOME clone of Breakout the classic arcade game.

%description -l pl
GNOME klon klasycznej gry Breakout.

%prep
%setup -q

%build
rm -rf missing
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_applnkdir}/Games

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gnome-breakout
%{_datadir}/gnome-breakout
%{_pixmapsdir}/gnome-breakout.png
%{_applnkdir}/Games/gnome-breakout.desktop
