Name:           tpm2-tools
Version:        1.1 
Release:        0.1.beta1%{?dist}
Summary:        a TPM2.0 testing tool build upon TPM2.0-TSS

License:        BSD
URL:            https://github.com/01org/tpm2.0-tools
Source0:        https://github.com/01org/tpm2.0-tools/archive/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  openssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  tpm2-tss


#Requires:       

%description
tpm2-tools is a batch of testing tools for tpm2.0. It is based on tpm2-tss.

%prep
%setup -q


%build
./bootstrap
./configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_prefix}/local/sbin/tpm2_*

%doc


%changelog
* Mon Aug 22 2016 Sun Yunying <yunying.sun@intel.com> - 1.1beta1-1
- Initial version of the package