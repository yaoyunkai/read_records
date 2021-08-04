# npm #

## Getting started ##

**配置registry**

```bash
npm config set registry https://registry.your-registry.npme.io/
```

## Packages and modules ##

公共npm registry 是一个JavaScript包的数据库，每个包都由软件和元数据组成。开源开发人员和公司的开发人员使用npm registry  将包贡献给整个社区或他们组织的成员，并下载包用于自己的项目中。

**About packages**

一个包是一个文件或者文件夹用 package.json 来描述。包必须包含 `package.json` 

包可以是未限定范围的，也可以是限定范围给用户或组织的，限定范围的包可以是私有的，也可以是公共的。

**包的格式**

- a) A folder containing a program described by a `package.json` file.
- b) A gzipped tarball containing (a).
- c) A URL that resolves to (b).
- d) A `<name>@<version>` that is published on the registry with (c).
- e) A `<name>@<tag>` that points to (d).
- f) A `<name>` that has a `latest` tag satisfying (e).
- g) A `git` url that, when cloned, results in (a).

**About modules**

模块是node_modules目录中可以由Node.js require()函数加载的任何文件或目录。

要被Node.js的require()函数加载，一个模块必须是以下条件之一:

- A folder with a `package.json` file containing a `"main"` field.
- A JavaScript file.

**About scopes**

`@npm/package-name`

这里scope就是npm

- Unscoped packages are always public.
- Private packages are always scoped.
- Scoped packages are private by default; you must pass a command-line flag when publishing to make them public.

### 从仓库获取包 ###

主要就是包的安装，更新，卸载操作。

## npm CLI ##

### CLI Commands ###

下面列出了npm的各种命令

### Configuring npm ###

#### package.json ####

- **files**: 可选的files字段是一个文件模式数组，描述了当您的包作为依赖项安装时要包含的条目。文件模式遵循与.gitignore相似的语法。您还可以在包的根目录或子目录中提供.npmignore文件，这将防止文件被包含。

- **main**: 主字段是模块ID，它是程序的主要入口点。也就是说，如果你的包名为foo，用户安装了它，然后require("foo")，那么你的主模块的exports对象将被返回。这应该是一个相对于包文件夹根目录的模块。如果main未设置，则默认为包根目录下的index.js。
- **bin**: 许多包都有一个或多个希望安装到PATH中的可执行文件。



### Using npm ###

