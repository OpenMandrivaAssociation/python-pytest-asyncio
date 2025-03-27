%global pypi_name pytest_asyncio

Name:           python-pytest-asyncio
Version:        0.26.0
Release:        1
Summary:        Pytest support for asyncio
Group:          Development/Python
License:        Apache 2.0
URL:            https://github.com/pytest-dev/pytest-asyncio
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python%{pyver}dist(setuptools)
%{?python_provide:%python_provide python-%{pypi_name}}
Requires:       python%{pyver}dist(async-generator) >= 1.3
Requires:       python%{pyver}dist(async-generator) >= 1.3
Requires:       python%{pyver}dist(coverage)
Requires:       python%{pyver}dist(hypothesis) >= 3.64
Requires:       python%{pyver}dist(pytest)
Requires:       python%{pyver}dist(setuptools)

%description
pytest-asyncio: pytest support for asyncio :alt: Supported Python versions

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

cat >>setup.cfg <<EOF
[options]
packages = pytest_asyncio
EOF

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_asyncio
%{python_sitelib}/pytest_asyncio-%{version}.dist-info
