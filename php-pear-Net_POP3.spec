%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	POP3
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - POP3 class to access POP3 server
Summary(pl):	%{_pearname} - klasa POP3 daj±ca dostêp do serverów POP3
Name:		php-pear-%{_pearname}
Version:	1.3.1
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8bc9ebefb7de13ab461f7cf6140b76ea
URL:		http://pear.php.net/package/Net_POP3/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a POP3 class to access POP3 server. Support all POP3 commands
including UIDL listings and APOP authentication.

In PEAR status of this package is: %{_status}.

%description -l pl
Dostarcza klasê POP3, daj±c± dostêp do serwerów POP3. Wspiera
wszystkie komendy POP3, w³±czaj±c w to listy UIDL oraz autentyfikacjê
APOP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/Net_POP3_example.php
%{php_pear_dir}/%{_class}/*.php
