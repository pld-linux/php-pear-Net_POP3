%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	POP3
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - POP3 class to access POP3 server
Summary(pl.UTF-8):	%{_pearname} - klasa POP3 dająca dostęp do serwerów POP3
Name:		php-pear-%{_pearname}
Version:	1.3.6
Release:	3
Epoch:		0
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dad6200744d2c8f326fbec1f5e0c8249
URL:		http://pear.php.net/package/Net_POP3/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a POP3 class to access POP3 server. Support all POP3 commands
including UIDL listings, APOP authentication, DIGEST-MD5 and CRAM-MD5
using optional Auth_SASL package.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Dostarcza klasę POP3, dającą dostęp do serwerów POP3. Wspiera
wszystkie komendy POP3, włączając w to listy UIDL, uwierzytelnianie APOP,
DIGEST-MD5 i CRAM-MD5 z użyciem klasy Auth_SASL.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
