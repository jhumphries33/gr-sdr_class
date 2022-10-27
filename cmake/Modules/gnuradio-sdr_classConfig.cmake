find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_SDR_CLASS gnuradio-sdr_class)

FIND_PATH(
    GR_SDR_CLASS_INCLUDE_DIRS
    NAMES gnuradio/sdr_class/api.h
    HINTS $ENV{SDR_CLASS_DIR}/include
        ${PC_SDR_CLASS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_SDR_CLASS_LIBRARIES
    NAMES gnuradio-sdr_class
    HINTS $ENV{SDR_CLASS_DIR}/lib
        ${PC_SDR_CLASS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-sdr_classTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_SDR_CLASS DEFAULT_MSG GR_SDR_CLASS_LIBRARIES GR_SDR_CLASS_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_SDR_CLASS_LIBRARIES GR_SDR_CLASS_INCLUDE_DIRS)
