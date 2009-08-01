%define upstream_name    CGI-Untaint
%define upstream_version 1.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	CGI-Untaint Perl module: process CGI input parameters 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-CGI
BuildRequires:  perl-UNIVERSAL-exports
BuildRequires:  perl-UNIVERSAL-require
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a simple, convenient, abstracted and extensible
manner for validating and untainting the input from web forms.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/CGI/Untaint.pm
%{perl_vendorlib}/CGI/Untaint
%{_mandir}/*/*
