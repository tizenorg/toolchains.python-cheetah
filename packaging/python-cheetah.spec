%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-cheetah
Version:        2.4.4
Release:        1
Summary:        Template engine and code-generator

Group:          Development/Libraries
License:        MIT
URL:            http://cheetahtemplate.org/
Source:         http://pypi.python.org/packages/source/C/Cheetah/Cheetah-%{version}.tar.gz
Source1001: packaging/python-cheetah.manifest 

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  python-devel
%if 0%{?suse_version}
BuildRequires:  python-setuptools
%else
BuildRequires:  python-setuptools-devel
%endif
BuildRequires:  python-lxml, python-pygments, python-markdown

%description
Cheetah is an open source template engine and code generation tool,
written in Python. It can be used standalone or combined with other
tools and frameworks. Web development is its principle use, but
Cheetah is very flexible and is also being used to generate C++ game
code, Java, sql, form emails and even Python code.

%prep
%setup -q -n Cheetah-%{version}

%build
cp %{SOURCE1001} .
export CHEETAH_USE_SETUPTOOLS=1
%{__python} setup.py build

%install
export CHEETAH_USE_SETUPTOOLS=1
%if 0%{?suse_version}
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot} --record-rpm=INSTALLED_FILES  
%else
%{__python} setup.py install --skip-build --root %{buildroot} --prefix=%{_prefix}
%endif

%check
export PATH="%{buildroot}/%{_bindir}:$PATH"
export PYTHONPATH="%{buildroot}/%{python_sitearch}"
%{__python} %{buildroot}/%{python_sitearch}/Cheetah/Tests/Test.py

%clean
rm -rf %{buildroot}

%if 0%{?suse_version}
%files -f INSTALLED_FILES
%manifest python-cheetah.manifest
%defattr(-,root,root,-)
%else
%files
%manifest python-cheetah.manifest
%defattr(-,root,root,-)
%dir %{python_sitearch}/Cheetah
%{python_sitearch}/Cheetah/*.py
%{python_sitearch}/Cheetah/*.pyc
%{python_sitearch}/Cheetah/_namemapper.so
%{python_sitearch}/Cheetah/*.pyo

%dir %{python_sitearch}/Cheetah/Macros
%{python_sitearch}/Cheetah/Macros/*.py
%{python_sitearch}/Cheetah/Macros/*.pyc
%{python_sitearch}/Cheetah/Macros/*.pyo

%dir %{python_sitearch}/Cheetah/Templates
%{python_sitearch}/Cheetah/Templates/*.py
%{python_sitearch}/Cheetah/Templates/*.pyc
%{python_sitearch}/Cheetah/Templates/*.tmpl
%{python_sitearch}/Cheetah/Templates/*.pyo

%dir %{python_sitearch}/Cheetah/Tests
%{python_sitearch}/Cheetah/Tests/*.py
%{python_sitearch}/Cheetah/Tests/*.pyc
%{python_sitearch}/Cheetah/Tests/*.pyo

%dir %{python_sitearch}/Cheetah/Tools
%{python_sitearch}/Cheetah/Tools/*.py
%{python_sitearch}/Cheetah/Tools/*.pyc
%{python_sitearch}/Cheetah/Tools/*.txt
%{python_sitearch}/Cheetah/Tools/*.pyo

%dir %{python_sitearch}/Cheetah/Utils
%{python_sitearch}/Cheetah/Utils/*.py
%{python_sitearch}/Cheetah/Utils/*.pyc
%{python_sitearch}/Cheetah/Utils/*.pyo

%dir %{python_sitearch}/Cheetah-%{version}-*.egg-info
%{python_sitearch}/Cheetah-%{version}-*.egg-info/PKG-INFO
%{python_sitearch}/Cheetah-%{version}-*.egg-info/*.txt

%endif
%doc CHANGES LICENSE TODO
%{_bindir}/cheetah
%{_bindir}/cheetah-compile
%{_bindir}/cheetah-analyze

