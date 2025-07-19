Summary:	LV2 port of the MDA effects and synths
Name:	mda-lv2
Version:	1.2.10
Release:	1
License:	GPLv3+
Group:	Sound
Url:	https://gitlab.com/drobilla/mda-lv2
Source0:	https://gitlab.com/drobilla/mda-lv2/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pkgconfig(lv2)

%description
This is an LV2 port of the well-known VST MDA plugins by Paul Kellett. 
It contains 36 high-quality effects and instruments, with one of the greatest
virtual pianos among them.
The full documentation of the original VST's is here:
http://mda.smartelectronix.com/vst/help/index.htm

%files
%doc NEWS README.md
%{_libdir}/lv2/mda.lv2/*.so
%{_libdir}/lv2/mda.lv2/*.ttl

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-v%{version}


%build
%meson -Dtests=disabled -Dlv2dir="%{_libdir}/lv2"
# Tests require 'autoship', which is not packaged nor vendored in the project
%meson_build 


%install
%meson_install
