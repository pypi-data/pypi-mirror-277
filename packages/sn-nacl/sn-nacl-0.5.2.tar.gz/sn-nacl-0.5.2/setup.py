import os
import sys
import subprocess
import setuptools
from setuptools import setup, Extension


def detect_compiler():
    # Vérifier si un compilateur est spécifié dans les variables d'environnement
    compiler = os.environ.get('CC', None)
    if compiler:
        return compiler

    # gcc ?
    try:
        result = subprocess.run(['gcc', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return 'gcc'
    except FileNotFoundError:
        pass

    # clang ?
    try:
        result = subprocess.run(['clang', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return 'clang'
    except FileNotFoundError:
        pass

    # msvc ?
    if sys.platform == 'win32':
        try:
            result = subprocess.run(['cl'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if 'Microsoft (R) C/C++ Optimizing Compiler' in result.stderr:
                return 'msvc'
        except FileNotFoundError:
            pass

    return 'unknown compiler'

compiler = detect_compiler()
platform = sys.platform
print(f'compiling extension: {compiler} {platform}')

compile_args = ['-std=c11', '-O3', '-fopenmp']
link_args = []
if sys.platform == 'darwin':
    compile_args.extend(['-mmacosx-version-min=10.8', '-stdlib=libc++'])
    link_args.append('-lc++')


extensions = [
     Extension('nacl._libnacl',
               ['nacl/sparseutils.c',],
               extra_compile_args=compile_args,
               extra_link_args=link_args)]

setup(
    ext_modules=extensions,
)

# setup(name='sn-nacl',
#       #      packages=setuptools.find_packages(),
#       packages=['nacl', 'nacl.lib', 'nacl.models',
#                 'nacl.plotting', 'nacl.simulations',
#                 'nacl.data',
#                 'nacl.util'],
#       ext_modules=[Extension('nacl.lib._libnacl',
#                              ['nacl/lib/utils.c',],
#                              extra_compile_args=['-std=c11', '-O3'])],
#       version="0.3",
#       description="Supernova empirical model training package",
#       author='G. Augarde, N. Regnault, M. Betoule, S. Bongard',
#       author_email='nicolas.regnault@lpnhe.in2p3.fr',
#       #      package_dir={'': 'nacl'},
#       zip_safe=False,

#       install_requires=['numpy>=1.7', 'matplotlib', 'seaborn', 'cython', 'scikit-sparse', 'astropy', 'sparseqr'],
#       setup_requires=['pytest-runner'],
#       tests_require=['pytest-3'],
# )
