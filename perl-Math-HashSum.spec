#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	HashSum
Summary:	Math::HashSum - sum a list of key-value pairs on a per-key basis
Summary(pl):	Math::HashSum - sumowanie listy par klucz-warto¶æ na podstawie klucza
Name:		perl-Math-HashSum
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fe474ff52a3ce086e9887d821f784f5a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to sum a list of key-value pairs on a per-key
basis. It adds up all the values associated with each key in the given
list and returns a hash containing the sum associated with each key.

%description -l pl
Ten modu³ pozwala zsumowaæ listê par klucz-warto¶æ na podstawie
klucza. Dodaje wszystkie warto¶ci zwi±zane z ka¿dym kluczem z podanej
listy i zwraca hash zawieraj±cy sumê zwi±zan± z ka¿dym kluczem.

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
%doc CHANGES README
%{perl_vendorlib}/Math/HashSum.pm
%{_mandir}/man3/*
