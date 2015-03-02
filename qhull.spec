Summary:	Qhull - convex hulls, triangulations and related computations
Summary(pl.UTF-8):	Qhull - obliczanie powłok wypukłych, triangulacji i powiązanych rzeczy
Name:		qhull
Version:	2012.1
Release:	3
License:	distributable (see COPYING.txt)
Group:		Libraries
Source0:	http://www.qhull.org/download/%{name}-%{version}-src.tgz
# Source0-md5:	d0f978c0d8dfb2e919caefa56ea2953c
Patch0:		%{name}-cmake.patch
Patch1:		format-security.patch
URL:		http://www.qhull.org/
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.603
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qhull computes convex hulls, Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point. It runs in 2-d, 3-d, 4-d, or higher. It implements the
Quickhull algorithm for computing convex hulls. Qhull handles
round-off errors from floating point arithmetic. It can approximate a
convex hull.

%description -l pl.UTF-8
Qhull oblicza powłoki wypukłe, triangulacje Delaunaya, diagramy
Voronoi, diagramy Voronoi większych rzędów oraz przecięcia
półprzestrzeni. Działa w przestrzeniach dwu, trzy, cztero i więcej
wymiarowych. Ma zaimplementowany algorytm Quickhull do obliczania
powłok wypukłych. Obsługuje błędy zaokrągleń wynikłe z arytmetyki
zmiennoprzecinkowej. Może aproksymować powłoki wypukłe.

%package devel
Summary:	Header files for Qhull library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Qhull
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Qhull library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Qhull.

%package static
Summary:	Static Qhull library
Summary(pl.UTF-8):	Statyczna biblioteka Qhull
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Qhull library.

%description static -l pl.UTF-8
Statyczna biblioteka Qhull.

%package c++
Summary:	QhullCPP library
Summary(pl.UTF-8):	Biblioteka QhullCPP
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
QhullCPP library.

%description c++ -l pl.UTF-8
Biblioteka QhullCPP.

%package c++-devel
Summary:	Header files for QhullCPP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki QhullCPP
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for QhullCPP library.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki QhullCPP.

%package c++-static
Summary:	Static QhullCPP library
Summary(pl.UTF-8):	Statyczna biblioteka QhullCPP
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static QhullCPP library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka QhullCPP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake . \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DMAN_INSTALL_DIR=%{_mandir}/man1
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/qhull

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Announce.txt COPYING.txt README.txt REGISTER.txt index.htm
%attr(755,root,root) %{_bindir}/qconvex
%attr(755,root,root) %{_bindir}/qdelaunay
%attr(755,root,root) %{_bindir}/qhalf
%attr(755,root,root) %{_bindir}/qhull
%attr(755,root,root) %{_bindir}/qvoronoi
%attr(755,root,root) %{_bindir}/rbox
%attr(755,root,root) %{_libdir}/libqhull.so.6
%attr(755,root,root) %{_libdir}/libqhull_p.so.6
%{_mandir}/man1/qhull.1*
%{_mandir}/man1/rbox.1*

%files devel
%defattr(644,root,root,755)
%doc html/*.{htm,gif,jpg}
%attr(755,root,root) %{_libdir}/libqhull.so
%attr(755,root,root) %{_libdir}/libqhull_p.so
%{_includedir}/libqhull

%files static
%defattr(644,root,root,755)
%{_libdir}/libqhullstatic.a
%{_libdir}/libqhullstatic_p.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqhullcpp.so.6

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqhullcpp.so
%{_includedir}/libqhullcpp

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libqhullcppstatic.a
