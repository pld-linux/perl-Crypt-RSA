#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	RSA
Summary:	Crypt::RSA Perl module - RSA public-key cryptosystem
Summary(pl.UTF-8):	Moduł Perla Crypt::RSA - system kryptograficzny klucza publicznego RSA
Name:		perl-Crypt-RSA
Version:	1.99
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f675a07810d735e99d7894338aba8e87
URL:		http://search.cpan.org/dist/Crypt-RSA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Loader >= 2.00
BuildRequires:	perl-Convert-ASCII-Armour
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-CBC
BuildRequires:	perl-Crypt-Primes >= 0.38
BuildRequires:	perl-Crypt-Random >= 0.34
BuildRequires:	perl-Data-Buffer
BuildRequires:	perl-Digest-MD2
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-Tie-EncryptedHash
BuildRequires:	perl-Digest-SHA1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::RSA is a pure-perl, cleanroom implementation of the RSA
public-key cryptosystem.

%description -l pl.UTF-8
Moduł Crypt::RSA jest czysto perlową implementacją systemu
kryptograficznego klucza publicznego RSA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Crypt/*.pm
%{perl_vendorlib}/Crypt/RSA
%{_mandir}/man3/*
