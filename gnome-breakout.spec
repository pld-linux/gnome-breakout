Summary:	GNOME clone of Breakout the classic arcade game
Summary(pl):	GNOME klon klasycznej gry Breakout
Name:		gnome-breakout
Version:	0.5.2
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://users.senet.com.au/~alcaron/%{name}-%{version}.tar.gz
# Source0-md5:	3464e74aae8dce37da5336ed10ea6452
Source1:	%{name}.png
URL:		http://www.senet.com.au/~alcaron/software.html
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GNOME clone of Breakout the classic arcade game.

%description -l pl
GNOME klon klasycznej gry Breakout.

%prep
%setup -q

%build
rm -rf missing
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_desktopdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-breakout
%{_datadir}/gnome-breakout
%{_pixmapsdir}/gnome-breakout.png
%{_desktopdir}/gnome-breakout.desktop
