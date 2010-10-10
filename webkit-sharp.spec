%define name webkit-sharp
%define version 0.3
%define release %mkrel 2

Summary: WebKit bindings for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: MIT
Group: Development/Other
Url: http://mono.ximian.com/monobuild/preview/sources/webkit-sharp/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libwebkitgtk-devel
BuildRequires: mono-devel
BuildRequires: gtk-sharp2-devel
BuildRequires: gtk-sharp2
BuildRequires: monodoc
Requires: libwebkitgtk >= 1.1.1
BuildArch: noarch

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE, and used
primarily in Apple's Safari browser. It is made to be embedded in other
applications, such as mail readers, or web browsers.

This package provides Mono bindings for WebKit libraries.

%package doc
Summary:	Development documentation for %name
Group:		Development/Other
Requires(post):		mono-tools >= 1.1.9
Requires(postun):	mono-tools >= 1.1.9

%description doc
This package contains the API documentation for %name in
Monodoc format.

%package devel
Summary:	Development files for %name
Group:		Development/Other
Requires: %name = %version

%description devel
This package contains the development files needed to build with %{name}.

%prep
%setup -q

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
make

%install
rm -rf %{buildroot}
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf %{buildroot}

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%files
%defattr(-,root,root)
%doc AUTHORS
%_prefix/lib/mono/gac/webkit-sharp
%_prefix/lib/mono/webkit-sharp

%files devel
%defattr(-,root,root)
#gw this contains a dep on pkgconfig(gtk-sharp-2.0)
%_datadir/pkgconfig/*.pc

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/%{name}*


