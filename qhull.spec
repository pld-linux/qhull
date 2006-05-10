Summary:	Qhull - convex hulls, triangulations and related computations
Summary(pl):	Qhull - obliczanie pow³ok wypuk³ych, triangulacji i powi±zanych rzeczy
Name:		qhull
Version:	2003.1
Release:	1
License:	distributable (see COPYING.txt)
Group:		Libraries
Source0:	http://www.qhull.org/download/%{name}-%{version}-src.tgz
# Source0-md5:	3f301373539a55b8c7aa961b6c13d196
URL:		http://www.qhull.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qhull computes convex hulls, Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point. It runs in 2-d, 3-d, 4-d, or higher. It implements the
Quickhull algorithm for computing convex hulls. Qhull handles
round-off errors from floating point arithmetic. It can approximate a
convex hull.

%description -l pl
Qhull oblicza pow³oki wypuk³e, triangulacje Delaunaya, diagramy
Voronoi, diagramy Voronoi wiêkszych rzêdów oraz przeciêcia
pó³przestrzeni. Dzia³a w przestrzeniach dwu, trzy, cztero i wiêcej
wymiarowych. Ma zaimplementowany algorytm Quickhull do obliczania
pow³ok wypuk³ych. Obs³uguje b³êdy zaokr±gleñ wynik³e z arytmetyki
zmiennoprzecinkowej. Mo¿e aproksymowaæ pow³oki wypuk³e.

%package devel
Summary:	Header files for Qhull library
Summary(pl):	Pliki nag³ówkowe biblioteki Qhull
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Qhull library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Qhull.

%package static
Summary:	Static Qhull library
Summary(pl):	Statyczna biblioteka Qhull
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Qhull library.

%description static -l pl
Statyczna biblioteka Qhull.

%prep
%setup -q

%{__perl} -pi -e 's/\r//g;s/^echo Run/exit 0/' src/Make-config.sh
touch src/Makefile.txt
mv -f src/{Mborland,MBorland}

%build
cd src
./Make-config.sh
cd ..
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Announce.txt COPYING.txt README.txt REGISTER.txt index.htm
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%doc html/*.{htm,gif}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/qhull

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
