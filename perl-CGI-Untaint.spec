%define real_name CGI-Untaint

Summary:	CGI-Untaint Perl module: process CGI input parameters 
Name:		perl-%{real_name}
Version:	1.26
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl-UNIVERSAL-exports
BuildRequires:  perl-CGI
BuildRequires:  perl-UNIVERSAL-require
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides a simple, convenient, abstracted and extensible
manner for validating and untainting the input from web forms.

%prep
%setup -q -n %{real_name}-%{version} 

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


