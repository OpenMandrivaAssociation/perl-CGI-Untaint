%define upstream_name    CGI-Untaint
%define upstream_version 1.26

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	CGI-Untaint Perl module: process CGI input parameters 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(UNIVERSAL::exports)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
This module provides a simple, convenient, abstracted and extensible
manner for validating and untainting the input from web forms.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/CGI/Untaint.pm
%{perl_vendorlib}/CGI/Untaint
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.260.0-2mdv2011.0
+ Revision: 680700
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.260.0-1mdv2011.0
+ Revision: 406871
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.26-6mdv2009.0
+ Revision: 255832
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.26-4mdv2008.1
+ Revision: 136678
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-4mdv2008.0
+ Revision: 86064
- rebuild


* Wed Apr 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.26-3mdk
- Fix BuildRequires

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.26-2mdk
- Fix BuildRequires
- make rpmbuildupdate happy

* Mon Sep 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.26-1mdk
- 1.26

* Thu Jul 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.25-1mdk
- 1.25

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.00-1mdk
- initial Mandriva package

