%define upstream_name    Catalyst-Plugin-StackTrace
Name:		perl-%{upstream_name}
Version:	0.12
Release:	4

Summary:	Display a stack trace on the debug screen
License:	Artistic/GPL
Group:		Development/Perl
URL:		https://metacpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-StackTrace-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.61
BuildRequires:	perl(Devel::StackTrace)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(MRO::Compat)
BuildArch:	noarch

%description
This plugin will enhance the standard Catalyst debug screen by
including a stack trace of your appliation up to the point where the
error occurred. Each stack frame is displayed along with the package
name, line number, file name, and code context surrounding the line
number.

This plugin is only active in -Debug mode.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


