#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	RSA
Summary:	Crypt::RSA Perl module - RSA public-key cryptosystem
Summary(pl):	Modu³ Perla Crypt::RSA - system kryptograficzny klucza publicznego RSA
Name:		perl-Crypt-RSA
Version:	1.50
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	422ee7bbb5b31b146c4fd8c5993af988
%if %{with tests}
BuildRequires:	perl-Convert-ASCII-Armour
BuildRequires:	perl-Class-Loader >= 2.00
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-CBC
BuildRequires:	perl-Crypt-Primes >= 0.38
BuildRequires:	perl-Crypt-Random >= 0.33
BuildRequires:	perl-Data-Buffer
BuildRequires:	perl-Digest-MD2
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-Tie-EncryptedHash
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Class-Loader >= 2.00
Requires:	perl-Crypt-Primes >= 0.38
Requires:	perl-Crypt-Random >= 0.33
Requires:	perl-Math-Pari >= 2.001804
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::RSA is a pure-perl, cleanroom implementation of the RSA
public-key cryptosystem.

%description -l pl
Modu³ Crypt::RSA jest czysto perlow± implementacj± systemu
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
%doc Changes TODO extradocs/*
%{perl_vendorlib}/Crypt/RSA.pm
%{perl_vendorlib}/Crypt/RSA
%{_mandir}/man3/*
