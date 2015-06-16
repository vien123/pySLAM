from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension( 
        name="pySLAM.slam_system",
        # TODO: add source dir
        sources=['slam_system.pyx'],
        include_dirs = [
                        'lsd_slam/lsd_slam_core/src',
                        'lsd_slam/lsd_slam_core/thirdparty/Sophus', 
                        '/usr/include/eigen3'],
        libraries = ['lsdslam'],
        library_dirs = ['lsd_slam/lsd_slam_core/lib'],
        extra_link_args="",
        extra_compile_args="",
        language="c++")
]

setup( 
    name="pySLAM",
    version="0.1",
    packages = ['pySLAM'],
    description="OpenGL UI powered by Cython",
    url="https://github.com/pupil-labs/pySLAM",
    author='Pupil Labs',
    author_email='info@pupil-labs.com',
    license='MIT',
    ext_modules=cythonize(extensions)
)