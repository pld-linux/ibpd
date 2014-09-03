Summary:	InfiniBand Proxy Daemon
Summary(pl.UTF-8):	InfiniBand Proxy Daemon - demon proxy IB
Name:		ibpd
Version:	1.0.0
%define	subver	2
Release:	2
License:	GPL v2 or BSD
Group:		Daemons
Source0:	https://www.openfabrics.org/downloads/ibpd/%{name}-%{version}-%{subver}.tar.gz
# Source0-md5:	875113f31fb93e9488dede2b21c7c508
URL:		http://www.intel.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IB Proxy Daemon (ibpd) is a user-mode process for InfiniBand proxy
devices.

%description -l pl.UTF-8
IB Proxy Daemon (ibpd) to proces przestrzeni użytkownika dla urządzeń
proxy InfiniBand.

%prep
%setup -q -n %{name}-%{version}-%{subver}

%build
%{__make} ibpd \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D ibpd $RPM_BUILD_ROOT%{_sbindir}/ibpd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_sbindir}/ibpd
