import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='creator-admin-next',  
     version='0.1',
     scripts=['creator-admin-next'] ,
     author="Victor Silva",
     author_email="victor@nextdesign-e.com",
     description="A Creator package to get all of your modules",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/victorsilvanext/creator",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
