%define         state          stable
%define         qtver           4.4.3
Summary:	KDE Guidance Power Manager
Summary(pl.UTF-8):	KDE Guidance Power Manager
Name:		guidance-power-manager
Version:	4.4.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{state}/%{version}/src/extragear/%{name}-%{version}.tar.bz2
# Source0-md5:	aa1e73fb8ca25cf5585a32e28e23508f
URL:		http://www.simonzone.com/software/guidance/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	python
BuildRequires:	python-PyKDE4 >= %{version}
BuildRequires:	python-sip-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel
Requires:	python-PyKDE4 >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A power management applet to indicate battery levels and perform
hibernate or suspend using HAL.

%description -l pl.UTF-8
A power management applet to indicate battery levels and perform
hibernate or suspend using HAL.

%prep
%setup -q

cat <<'EOF' > guidance-power-manager
#!/bin/sh
exec python %{_datadir}/apps/guidance-power-manager/guidance-power-manager.pyc $@
EOF

%build
install -d build
cd build

%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{_datadir}/apps/guidance-power-manager
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/apps/guidance-power-manager
%py_postclean
install guidance-power-manager $RPM_BUILD_ROOT/usr/bin

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/guidance-power-manager
%{py_sitedir}/ixf86misc.so
%{py_sitedir}/xf86misc.py[co]
%dir %{_datadir}/apps/guidance-power-manager
%{_datadir}/apps/guidance-power-manager/guidance-power-manager.py[co]
%{_datadir}/apps/guidance-power-manager/guidance-power-manager.ui
%{_datadir}/apps/guidance-power-manager/powermanage.py[co]
%{_datadir}/autostart/guidance-power-manager.desktop
