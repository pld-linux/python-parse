# NOTE: for versions >= 1.13.0 (for python 3.4+) see python3-parse.spec
#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-parse.spec)

Summary:	parse() - the opposite of format()
Summary(pl.UTF-8):	parse() - odwrotność format()
Name:		python-parse
# keep 1.13.x here for python2 support
# (despite classifiers, 1.13.1 works and passes test suite on python 2.7 and
#  is required for parse_type 0.6.2, which supports python 2.7)
Version:	1.13.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/parse/
Source0:	https://files.pythonhosted.org/packages/source/p/parse/parse-%{version}.tar.gz
# Source0-md5:	6591f6095516b2f0e0c105c76777ad32
URL:		https://pypi.org/project/parse/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse strings using a specification based on the Python format()
syntax.

%description -l pl.UTF-8
Rozkład łańcuchów znaków przy użyciu specyfikacji opartej na składni
pythonowej metody format().

%package -n python3-parse
Summary:	parse() - the opposite of format()
Summary(pl.UTF-8):	parse() - odwrotność format()
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-parse
Parse strings using a specification based on the Python format()
syntax.

%description -n python3-parse -l pl.UTF-8
Rozkład łańcuchów znaków przy użyciu specyfikacji opartej na składni
pythonowej metody format().

%prep
%setup -q -n parse-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} test_parse.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} test_parse.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/parse.py[co]
%{py_sitescriptdir}/parse-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-parse
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/parse.py
%{py3_sitescriptdir}/__pycache__/parse.cpython-*.py[co]
%{py3_sitescriptdir}/parse-%{version}-py*.egg-info
%endif
