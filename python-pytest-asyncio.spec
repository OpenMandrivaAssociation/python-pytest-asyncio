%global pypi_name pytest_asyncio

Name:           python-pytest-asyncio
Version:        1.3.0
Release:        1
Summary:        Pytest support for asyncio
Group:          Development/Python
License:        Apache 2.0
URL:            https://github.com/pytest-dev/pytest-asyncio
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools-scm)
BuildRequires:  python%{pyver}dist(pytest)
BuildRequires:  python%{pyver}dist(pluggy)
BuildRequires:	git-core
Requires:       python%{pyver}dist(async-generator) >= 1.3
Requires:       python%{pyver}dist(async-generator) >= 1.3
Requires:       python%{pyver}dist(coverage)
Requires:       python%{pyver}dist(hypothesis) >= 3.64
Requires:       python%{pyver}dist(pytest)
Requires:       python%{pyver}dist(setuptools)


%description
pytest-asyncio: pytest support for asyncio :alt: Supported Python versions

%prep -a
cat >>setup.cfg <<EOF
[options]
packages = pytest_asyncio
EOF

# setuptools-scm needs to see a "git tag" to determine the
# version -- even when building from tarball
git init
git config user.name "OpenMandriva Builder"
git config user.email builder@openmandriva.org
git add .
git commit -m "Import %{version}"
git tag -a %{version} -m %{version}

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_asyncio
%{python_sitelib}/pytest_asyncio-%{version}.dist-info
