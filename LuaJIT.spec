#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : LuaJIT
Version  : 2.1.0.beta3
Release  : 14
URL      : file:///aot/build/clearlinux/packages/LuaJIT/LuaJIT-v2.1.0-beta3.tar.gz
Source0  : file:///aot/build/clearlinux/packages/LuaJIT/LuaJIT-v2.1.0-beta3.tar.gz
Summary  : Just-in-time compiler for Lua
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MPL-1.1
Requires: LuaJIT-bin = %{version}-%{release}
Requires: LuaJIT-data = %{version}-%{release}
Requires: LuaJIT-lib = %{version}-%{release}
Requires: LuaJIT-man = %{version}-%{release}
BuildRequires : binutils-dev
BuildRequires : buildreq-cmake
BuildRequires : cairo
BuildRequires : cairo-dev
BuildRequires : cups-dev
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : e2fsprogs-dev
BuildRequires : elfutils-dev
BuildRequires : findutils
BuildRequires : freetype
BuildRequires : freetype-dev
BuildRequires : fribidi-dev
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdk-pixbuf
BuildRequires : gdk-pixbuf-dev
BuildRequires : gettext
BuildRequires : glib
BuildRequires : glib-dev
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : gmp
BuildRequires : gmp-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gsettings-desktop-schemas
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : gtk3
BuildRequires : gtk3-dev
BuildRequires : ibus
BuildRequires : ibus-dev
BuildRequires : ibus-libpinyin
BuildRequires : krb5-dev
BuildRequires : libXcursor-dev
BuildRequires : libXinerama-dev
BuildRequires : libgcc1
BuildRequires : libinput-dev
BuildRequires : libpng
BuildRequires : libpng-dev
BuildRequires : libstdc++
BuildRequires : libxkbcommon-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : mpc
BuildRequires : mpc-dev
BuildRequires : mpfr
BuildRequires : mpfr-dev
BuildRequires : ncurses
BuildRequires : ncurses-dev
BuildRequires : perl
BuildRequires : perl(Moo::Role)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(XML::Parser)
BuildRequires : perl-Parallel-ForkManager
BuildRequires : pixman
BuildRequires : pixman-dev
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(atk-bridge-2.0)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(fribidi)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : pkgconfig(rest-0.7)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xrandr)
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : sassc
BuildRequires : sqlite-autoconf
BuildRequires : sqlite-autoconf-dev
BuildRequires : sqlite-autoconf-staticdev
BuildRequires : wayland-dev
BuildRequires : wayland-protocols-dev
BuildRequires : xorgproto-dev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
-----------------------------
LuaJIT is a Just-In-Time (JIT) compiler for the Lua programming language.

%package bin
Summary: bin components for the LuaJIT package.
Group: Binaries
Requires: LuaJIT-data = %{version}-%{release}

%description bin
bin components for the LuaJIT package.


%package data
Summary: data components for the LuaJIT package.
Group: Data

%description data
data components for the LuaJIT package.


%package dev
Summary: dev components for the LuaJIT package.
Group: Development
Requires: LuaJIT-lib = %{version}-%{release}
Requires: LuaJIT-bin = %{version}-%{release}
Requires: LuaJIT-data = %{version}-%{release}
Provides: LuaJIT-devel = %{version}-%{release}
Requires: LuaJIT = %{version}-%{release}

%description dev
dev components for the LuaJIT package.


%package lib
Summary: lib components for the LuaJIT package.
Group: Libraries
Requires: LuaJIT-data = %{version}-%{release}

%description lib
lib components for the LuaJIT package.


%package man
Summary: man components for the LuaJIT package.
Group: Default

%description man
man components for the LuaJIT package.


%package staticdev
Summary: staticdev components for the LuaJIT package.
Group: Default
Requires: LuaJIT-dev = %{version}-%{release}

%description staticdev
staticdev components for the LuaJIT package.


%prep
%setup -q -n LuaJIT
cd %{_builddir}/LuaJIT

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620944857
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FCFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export CXXFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export LDFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
make  %{?_smp_mflags}  amalg V=1 VERBOSE=1 MULTILIB=lib64 CFLAGS="${CFLAGS}" CXXFLAGS="${CXXFLAGS}" LDFLAGS="${LDFLAGS}"

#make install V=1 VERBOSE=1 PREFIX=$PWD MULTILIB=lib64 CFLAGS="${CFLAGS}" CXXFLAGS="${CXXFLAGS}" LDFLAGS="${LDFLAGS}"
./run-tests -j 16 $PWD || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
make  %{?_smp_mflags}  amalg V=1 VERBOSE=1 MULTILIB=lib64 CFLAGS="${CFLAGS}" CXXFLAGS="${CXXFLAGS}" LDFLAGS="${LDFLAGS}"


%install
export SOURCE_DATE_EPOCH=1620944857
rm -rf %{buildroot}
%make_install V=1 VERBOSE=1 MULTILIB=lib64 CFLAGS="${CFLAGS}" CXXFLAGS="${CXXFLAGS}" LDFLAGS="${LDFLAGS}"
## install_append content
ln -sf luajit-2.1.0-beta3 %{buildroot}/usr/bin/luajit
cp src/*.h %{buildroot}/usr/include/luajit-2.1/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/luajit
/usr/bin/luajit-2.1.0

%files data
%defattr(-,root,root,-)
/usr/share/luajit-2.1.0/jit/bc.lua
/usr/share/luajit-2.1.0/jit/bcsave.lua
/usr/share/luajit-2.1.0/jit/dis_arm.lua
/usr/share/luajit-2.1.0/jit/dis_arm64.lua
/usr/share/luajit-2.1.0/jit/dis_arm64be.lua
/usr/share/luajit-2.1.0/jit/dis_mips.lua
/usr/share/luajit-2.1.0/jit/dis_mips64.lua
/usr/share/luajit-2.1.0/jit/dis_mips64el.lua
/usr/share/luajit-2.1.0/jit/dis_mipsel.lua
/usr/share/luajit-2.1.0/jit/dis_ppc.lua
/usr/share/luajit-2.1.0/jit/dis_x64.lua
/usr/share/luajit-2.1.0/jit/dis_x86.lua
/usr/share/luajit-2.1.0/jit/dump.lua
/usr/share/luajit-2.1.0/jit/p.lua
/usr/share/luajit-2.1.0/jit/v.lua
/usr/share/luajit-2.1.0/jit/vmdef.lua
/usr/share/luajit-2.1.0/jit/zone.lua

%files dev
%defattr(-,root,root,-)
/usr/include/luajit-2.1/lauxlib.h
/usr/include/luajit-2.1/lj_alloc.h
/usr/include/luajit-2.1/lj_arch.h
/usr/include/luajit-2.1/lj_asm.h
/usr/include/luajit-2.1/lj_asm_arm.h
/usr/include/luajit-2.1/lj_asm_arm64.h
/usr/include/luajit-2.1/lj_asm_mips.h
/usr/include/luajit-2.1/lj_asm_ppc.h
/usr/include/luajit-2.1/lj_asm_x86.h
/usr/include/luajit-2.1/lj_bc.h
/usr/include/luajit-2.1/lj_bcdef.h
/usr/include/luajit-2.1/lj_bcdump.h
/usr/include/luajit-2.1/lj_buf.h
/usr/include/luajit-2.1/lj_carith.h
/usr/include/luajit-2.1/lj_ccall.h
/usr/include/luajit-2.1/lj_ccallback.h
/usr/include/luajit-2.1/lj_cconv.h
/usr/include/luajit-2.1/lj_cdata.h
/usr/include/luajit-2.1/lj_char.h
/usr/include/luajit-2.1/lj_clib.h
/usr/include/luajit-2.1/lj_cparse.h
/usr/include/luajit-2.1/lj_crecord.h
/usr/include/luajit-2.1/lj_ctype.h
/usr/include/luajit-2.1/lj_debug.h
/usr/include/luajit-2.1/lj_def.h
/usr/include/luajit-2.1/lj_dispatch.h
/usr/include/luajit-2.1/lj_emit_arm.h
/usr/include/luajit-2.1/lj_emit_arm64.h
/usr/include/luajit-2.1/lj_emit_mips.h
/usr/include/luajit-2.1/lj_emit_ppc.h
/usr/include/luajit-2.1/lj_emit_x86.h
/usr/include/luajit-2.1/lj_err.h
/usr/include/luajit-2.1/lj_errmsg.h
/usr/include/luajit-2.1/lj_ff.h
/usr/include/luajit-2.1/lj_ffdef.h
/usr/include/luajit-2.1/lj_ffrecord.h
/usr/include/luajit-2.1/lj_folddef.h
/usr/include/luajit-2.1/lj_frame.h
/usr/include/luajit-2.1/lj_func.h
/usr/include/luajit-2.1/lj_gc.h
/usr/include/luajit-2.1/lj_gdbjit.h
/usr/include/luajit-2.1/lj_ir.h
/usr/include/luajit-2.1/lj_ircall.h
/usr/include/luajit-2.1/lj_iropt.h
/usr/include/luajit-2.1/lj_jit.h
/usr/include/luajit-2.1/lj_lex.h
/usr/include/luajit-2.1/lj_lib.h
/usr/include/luajit-2.1/lj_libdef.h
/usr/include/luajit-2.1/lj_mcode.h
/usr/include/luajit-2.1/lj_meta.h
/usr/include/luajit-2.1/lj_obj.h
/usr/include/luajit-2.1/lj_parse.h
/usr/include/luajit-2.1/lj_prng.h
/usr/include/luajit-2.1/lj_profile.h
/usr/include/luajit-2.1/lj_recdef.h
/usr/include/luajit-2.1/lj_record.h
/usr/include/luajit-2.1/lj_serialize.h
/usr/include/luajit-2.1/lj_snap.h
/usr/include/luajit-2.1/lj_state.h
/usr/include/luajit-2.1/lj_str.h
/usr/include/luajit-2.1/lj_strfmt.h
/usr/include/luajit-2.1/lj_strscan.h
/usr/include/luajit-2.1/lj_tab.h
/usr/include/luajit-2.1/lj_target.h
/usr/include/luajit-2.1/lj_target_arm.h
/usr/include/luajit-2.1/lj_target_arm64.h
/usr/include/luajit-2.1/lj_target_mips.h
/usr/include/luajit-2.1/lj_target_ppc.h
/usr/include/luajit-2.1/lj_target_x86.h
/usr/include/luajit-2.1/lj_trace.h
/usr/include/luajit-2.1/lj_traceerr.h
/usr/include/luajit-2.1/lj_udata.h
/usr/include/luajit-2.1/lj_vm.h
/usr/include/luajit-2.1/lj_vmevent.h
/usr/include/luajit-2.1/lua.h
/usr/include/luajit-2.1/lua.hpp
/usr/include/luajit-2.1/luaconf.h
/usr/include/luajit-2.1/luajit.h
/usr/include/luajit-2.1/lualib.h
/usr/lib64/libluajit-5.1.so
/usr/lib64/pkgconfig/luajit.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libluajit-5.1.so.2
/usr/lib64/libluajit-5.1.so.2.1.0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/luajit.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libluajit-5.1.a
