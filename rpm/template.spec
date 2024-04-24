%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-fields2cover
Version:        2.0.0
Release:        4%{?dist}%{?release_suffix}
Summary:        ROS fields2cover package

License:        BSD-3
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       gdal-devel
Requires:       git
Requires:       gtest-devel
Requires:       python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-matplotlib
Requires:       python%{python3_pkgversion}-tkinter
Requires:       ros-iron-ortools-vendor
Requires:       tbb-devel
Requires:       tinyxml2-devel
Requires:       ros-iron-ros-workspace
BuildRequires:  cmake3
BuildRequires:  eigen3-devel
BuildRequires:  gdal-devel
BuildRequires:  git
BuildRequires:  gtest-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-iron-ortools-vendor
BuildRequires:  tbb-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  lcov
%endif

%description
Robust and efficient coverage paths for autonomous agricultural vehicles. A
modular and extensible Coverage Path Planning library

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Wed Apr 24 2024 Gonzalo Mier <gonzalo.miermunoz@wur.nl> - 2.0.0-4
- Autogenerated by Bloom

* Wed Apr 17 2024 Gonzalo Mier <gonzalo.miermunoz@wur.nl> - 2.0.0-3
- Autogenerated by Bloom

* Wed Apr 17 2024 Gonzalo Mier <gonzalo.miermunoz@wur.nl> - 2.0.0-2
- Autogenerated by Bloom

* Fri Apr 05 2024 Gonzalo Mier <gonzalo.miermunoz@wur.nl> - 2.0.0-1
- Autogenerated by Bloom

* Thu Mar 28 2024 Gonzalo Mier <gonzalo.miermunoz@wur.nl> - 1.2.1-3
- Autogenerated by Bloom

* Wed Jan 10 2024 Gonzalo Mier <gonzalo.miermunoz@wur.nl> - 1.2.1-2
- Autogenerated by Bloom

* Wed Nov 15 2023 Gonzalo Mier <gonzalo.miermunoz@wur.nl> - 1.2.1-1
- Autogenerated by Bloom

