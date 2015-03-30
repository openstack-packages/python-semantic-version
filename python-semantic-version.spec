# Created by pyp2rpm-1.1.1
%global pypi_name semantic_version

Name:           python-%{pypi_name}
Version:        2.3.1
Release:        1%{?dist}
Summary:        A library implementing the 'SemVer' scheme

License:        BSD
URL:            https://github.com/rbarrois/python-semanticversion
Source0:        https://pypi.python.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx


%description
This small python library provides a few tools to handle `SemVer`_ in Python.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs 
#sphinx-build docs html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Mar 30 2015 Dan Prince - 2.3.1-1
- Initial package.
