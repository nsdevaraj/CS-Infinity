
# package.json
* **2 types of dependencies**
    * dev-dependency - required in development phase
    * Normal-dependency - used in production too along with development phase
* In dependencies in packages.json
    * ^ It automatically updates both minor and patch updates.
    * ~ Use ~ when you want to avoid minor version updates but still receive patch updates for bug fixes.

![[Pasted image 20241202133704.png]]



* Browserslist
    * The config to share target browsers and Node.js versions between different front-end tools.
    * All tools will find target browsers automatically, when you add the following to package.json:

# package-lock.json
* keeps a record of exact version of packages installed.

