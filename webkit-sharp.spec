Summary:	WebKit bindings for Mono
Name:		webkit-sharp
Version:	0.3
Release:	9
Source0:	%{name}-%{version}.tar.bz2
License:	MIT
Group:		Development/Other
Url:		http://mono.ximian.com/monobuild/preview/sources/webkit-sharp/
BuildRequires:	pkgconfig(webkit-1.0)
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gtk-sharp2
BuildRequires:	monodoc
BuildArch:	noarch

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE, and used
primarily in Apple's Safari browser. It is made to be embedded in other
applications, such as mail readers, or web browsers.

This package provides Mono bindings for WebKit libraries.

%package doc
Summary:	Development documentation for %{name}
Group:		Development/Other
Requires(post):		mono-tools >= 1.1.9
Requires(postun):	mono-tools >= 1.1.9

%description doc
This package contains the API documentation for %{name} in
Monodoc format.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}

%description devel
This package contains the development files needed to build with %{name}.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --libdir=%{_prefix}/lib
make

%install
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig

%post doc
%{_bindir}/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %{_bindir}/monodoc ]; then %{_bindir}/monodoc --make-index > /dev/null
fi

%files
%doc AUTHORS
%{_prefix}/lib/mono/gac/webkit-sharp
%{_prefix}/lib/mono/webkit-sharp

%files devel
#gw this contains a dep on pkgconfig(gtk-sharp-2.0)
%{_datadir}/pkgconfig/*.pc

%files doc
%{_prefix}/lib/monodoc/sources/%{name}*

%changelog
* Wed May 09 2012 Götz Waschk <waschk@mandriva.org> 0.3-4mdv2012.0
+ Revision: 797712
- yearly rebuild

* Sat May 07 2011 Funda Wang <fwang@mandriva.org> 0.3-3
+ Revision: 672199
- update br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sun Oct 10 2010 Funda Wang <fwang@mandriva.org> 0.3-2mdv2011.0
+ Revision: 584547
- rebuild

* Thu Dec 10 2009 Götz Waschk <waschk@mandriva.org> 0.3-1mdv2010.1
+ Revision: 475946
- new version
- drop patch

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.2-3mdv2010.0
+ Revision: 427536
- rebuild

* Fri Mar 13 2009 Götz Waschk <waschk@mandriva.org> 0.2-2mdv2009.1
+ Revision: 354583
- update for new webkit

* Fri Jun 20 2008 Götz Waschk <waschk@mandriva.org> 0.2-1mdv2009.0
+ Revision: 227458
- fix buildrequires
- import webkit-sharp


