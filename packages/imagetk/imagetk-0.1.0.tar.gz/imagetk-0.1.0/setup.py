# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:36:58 2017

@author: a
"""
package='imagetk'
version='0.1.0'

from setuptools import setup, Extension
import os, importlib
from setuptools.command.build_ext import build_ext
import shutil
import platform

#不用编译的资源文件
try:
    resource=importlib.import_module(package).resource
except:
    resource=[]

with open('MANIFEST.in','w') as f:
    for i in resource:
        f.write('recursive-include '+package+'/'+i+' *\n')

#排除掉 __开头的文件及文件夹 或在 resource 中的文件夹
paths=[package]+[os.path.join(package,i) for i in os.listdir(package) if os.path.isdir(os.path.join(package,i)) and not i.startswith('__') and i not in resource]
files=sum([[i+'/'+ii.replace('\\','/') for ii in os.listdir(i)] for i in paths],[])
py=[i for i in files if i.endswith('__init__.py')]
c=[i for i in files if i.endswith('.c')]
pyd=[i for i in files if i.endswith('.pyd')]

class CustomBuildExt(build_ext):
    def run(self):
        if platform.system() == "Windows":
            for i in pyd:
                print('i',i)
                shutil.copy2(i, os.path.join(self.build_lib, i))

setup(
    #基本信息
    name = package,
    version = version,
    keywords = (),
    description = "",  
    long_description = "",  
    url = "",  
    author = "",
    author_email = "",
    
    #协议
    license = "Licence",
    
    #环境依赖
    platforms = "any",
    install_requires = ['numpy>=1.14.0', 'pandas>=2.2.0', 'scipy>=1.0.0'],

    #打包范围
    packages=[package+'.'+i for i in resource],#如果加上'elect'，则会把源码打包
    package_dir={package: package},
    py_modules=[i.replace('.py','') for i in py],
    ext_modules=[Extension(i.replace('.c','').replace('/','.'),sources=[i]) for i in c],
    cmdclass={'build_ext': CustomBuildExt},
    include_package_data = True,
    )

# python setup.py bdist_wheel -universal
# python setup.py sdist

