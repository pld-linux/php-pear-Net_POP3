%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	POP3
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - POP3 class to access POP3 server
Summary(pl.UTF-8):	%{_pearname} - klasa POP3 dająca dostęp do serwerów POP3
Name:		php-pear-%{_pearname}
Version:	1.3.7
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	eda6572e03b955ae0ca4345ddf2e4e33
URL:		http://pear.php.net/package/Net_POP3/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0
Requires:	php-pear-PEAR-core >= 1:1.4.0
Suggests:	php-pear-Auth_SASL
Obsoletes:	php-pear-%{_pearname}-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Auth/SASL.*)

%description
Provides a POP3 class to access POP3 server. Support all POP3 commands
including UIDL listings, APOP authentication, DIGEST-MD5 and CRAM-MD5
using optional Auth_SASL package.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Dostarcza klasę POP3, dającą dostęp do serwerów POP3. Wspiera
wszystkie komendy POP3, włączając w to listy UIDL, uwierzytelnianie
APOP, DIGEST-MD5 i CRAM-MD5 z użyciem klasy Auth_SASL.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
