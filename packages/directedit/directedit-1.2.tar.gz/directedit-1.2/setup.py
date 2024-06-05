from setuptools import setup, find_packages
from directedit import version

setup(
    name='directedit',
    version=version,
    long_description='''
<a href="https://pypi.org/project/directedit" rel="nofollow"><img alt="PyPI - Python Version" src="https://pypi-camo.freetls.fastly.net/da6321181d9727b03c184c40a5f46773aca688df/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f706970"></a>
<br><p>directedit is a <b>powerful library</b> for easy folder management. <br>
Key features:
<ol>
<li>Create and manage folders: Create a new folder and easily manage its contents.</li>
<li>Create and Write Files: Create new files and write data to them.</li>
<li>Read files: Read the contents of files.</li>
<li>Rename files: Rename files and folders.</li>
<li>Deleting files: Delete files and folders.</li>
<li>Destroying a folder: Deleting the entire folder and its contents.</li>
<li>File Path Management: Obtaining the absolute path to a file.</li>
<li>Cache Management: Caches the contents of files to speed up access to them.</li>
<li>Folder Update: Updates the contents of the folder and cache.</li>
</ol><br>
Useful functions:<br>
<ul>
<li>makes(): Creates new files and writes data to them.</li>
<li>files(): Gets a dictionary of all files in a folder.</li>
<li>reads(): Reads the contents of certain files.</li>
<li>renames(): Renames files and folders.</li>
<li>unlinks(): Delete files.</li>
<li>abs_path(): Get the absolute path to a file.</li>
<li>update(): Updating the contents of the folder and cache.</li>
<li>clear(): Deleting all files in the folder.</li>
<li>destroy(): Deleting the entire folder and its contents.</li>
</ul>
Benefits:<br>
<ul>
<li>Developers: Use Folder Manager as a utility in your projects to simplify file and folder management.</li>
<li>Power users: Use Folder Manager to automate common file and folder operations.</li>
</ul>
    ''',
    author='Monsler',
    description='Lightweight folder management contents library',
    author_email='galileoru22@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

)
