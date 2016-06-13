%bcond_without python2

Summary:	Template tag library for Django

Name:		python-django-macros
Version:	0.4.0
Release:	1
Source0:	https://pypi.python.org/packages/fd/be/9f6fcc55259c6b536d19d571dbec1577966c7c82f273f9dad157996f681c/django-macros-%{version}.zip
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/django-macros
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-distribute
Requires:	python-django

%description
Template tag library for Django

%if %{with python2}
%package -n python2-django-macros
Summary:	Template tag library for Django
Group:		Development/Python
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
Requires:	python2-django

%description -n python2-django-macros
Template tag library for Django
%endif

%prep
%setup -qc
mv django-macros-%{version} python3

%if %{with python2}
cp -r python3 python2
%endif

%build
%if %{with python2}
cd python2
python2 setup.py build
cd ..
%endif

cd python3
python setup.py build
cd ..

%install
%if %{with python2}
cd python2
python2 setup.py install --skip-build --root %{buildroot}
cd ..
%endif

cd python3
python setup.py install --skip-build --root=%{buildroot} 
cd ..

%files
%{py_puresitedir}/*

%if %{with python2}
%files -n python2-django-macros
%{py2_puresitedir}/*
%endif
