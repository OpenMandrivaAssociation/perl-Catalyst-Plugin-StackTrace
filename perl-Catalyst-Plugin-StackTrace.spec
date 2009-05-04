%define module Catalyst-Plugin-StackTrace
%define name	perl-%{module}
%define	modprefix Catalyst

%define version 0.10
%define release %mkrel 1

Summary:	Display a stack trace on the debug screen
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
BuildRequires:	perl(Catalyst) >= 5.61
BuildRequires:	perl(Devel::StackTrace)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(MRO::Compat)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This plugin will enhance the standard Catalyst debug screen by
including a stack trace of your appliation up to the point where the
error occurred. Each stack frame is displayed along with the package
name, line number, file name, and code context surrounding the line
number.

This plugin is only active in -Debug mode.


%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%__make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

