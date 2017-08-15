Name: tpm2-abrmd
Version: 1.1.0
Release: 4%{?dist}
Summary: A system daemon implementing TPM2 Access Broker and Resource Manager

License: BSD
URL:     https://github.com/01org/tpm2-abrmd
Source0: https://github.com/01org/tpm2-abrmd/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%{?systemd_requires}
BuildRequires: systemd
BuildRequires: libtool
BuildRequires: autoconf-archive
BuildRequires: pkgconfig(cmocka)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(sapi)
BuildRequires: pkgconfig(tcti-device)
BuildRequires: pkgconfig(tcti-socket)

# this package does not support big endian arch so far,
# and has been verified only on Intel platforms.
ExclusiveArch: %{ix86} x86_64

# tpm2-abrmd depends on tpm2-tss-devel for sapi/tcti-device/tcti-socket libs
Requires: tpm2-tss-devel%{?_isa} >= 1.1.0-1%{?dist} 

%description
tpm2-abrmd is a system daemon implementing the TPM2 access broker (TAB) and
Resource Manager (RM) spec from the TCG.

%prep
%autosetup -n %{name}-%{version}
autoreconf -vif

%build
%configure --disable-static --disable-silent-rules \
           --with-systemdsystemunitdir=%{_unitdir} \
           --with-udevrulesdir=%{_udevrulesdir}
%make_build

%install
%make_install
mv %{buildroot}/%{_udevrulesdir}/tpm-udev.rules %{buildroot}/%{_udevrulesdir}/60-tpm-udev.rules
find %{buildroot}%{_libdir} -type f -name \*.la -delete

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libtcti-tabrmd.so.*
%{_sbindir}/tpm2-abrmd
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/tpm2-abrmd.conf
%{_unitdir}/tpm2-abrmd.service
%{_udevrulesdir}/60-tpm-udev.rules
%{_mandir}/man3/tss2_tcti_tabrmd_init.3.gz
%{_mandir}/man3/tss2_tcti_tabrmd_init_full.3.gz
%{_mandir}/man7/tcti-tabrmd.7.gz
%{_mandir}/man8/tpm2-abrmd.8.gz


%package devel
Summary: Headers, static libraries and package config files of tpm2-abrmd 
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
This package contains headers, static libraries and package config files 
required to build applications that use tpm2-abrmd.

%files devel
%{_includedir}/tcti/tcti-tabrmd.h
%{_libdir}/libtcti-tabrmd.so
%{_libdir}/pkgconfig/tcti-tabrmd.pc

# on package installation
%post
/sbin/ldconfig
%systemd_post tpm2-abrmd.service

%preun
%systemd_preun tpm2-abrmd.service

%postun
/sbin/ldconfig
%systemd_postun tpm2-abrmd.service

%changelog
* Tue Aug 15 2017 Sun Yunying <yunying.sun@intel.com> - 1.1.0-4
- Rename and relocate udev rules file to _udevrulesdir
- Update scriptlet to add service name after systemd_postrun

* Tue Aug 1 2017 Sun Yunying <yunying.sun@intel.com> - 1.1.0-3
- Use config option with-systemdsystemunitdir to set systemd unit file location

* Mon Jul 31 2017 Sun Yunying <yunying.sun@intel.com> - 1.1.0-2
- Removed BuildRequires for gcc
- Move tpm2-abrmd systemd service to /usr/lib/systemd/system
- Added scriptlet for tpm2-abrmd systemd service
- Use autoreconf instead of bootstrap

* Wed Jul 26 2017 Sun Yunying <yunying.sun@intel.com> - 1.1.0-1
- Initial packaging
