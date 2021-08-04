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

### ES6 Modules ###

解析到 `<script type="module">` 标签后会立即下载模块文件，但执行会延迟到文档解析完成。

```html
<!-- 第二个执行 -->
<script type="module"></script>

<!-- 第三个执行 -->
<script type="module"></script>

<!-- 第一个执行 -->
<script></script>
```

#### 模块的行为 ####

- 模块代码只在加载后执行。
- 模块只能加载一次。
- 模块是单例。
- 模块可以定义公共接口，其他模块可以基于这个公共接口观察和交互。
- 模块可以请求加载其他模块。
- 支持循环依赖。

ES6 模块系统也增加了一些新行为。

- ES6 模块默认在严格模式下执行。
- ES6 模块不共享全局命名空间。
- 模块顶级 this 的值是 undefined （常规脚本中是 window ）。
- 模块中的 var 声明不会添加到 window 对象。
- ES6 模块是异步加载和执行的。

#### 模块导出 ####

ES6 模块支持两种导出：命名导出和默认导出。

```js
const foo = 'foo';
export {foo};

export const foo = 'foo';
export { foo as myFoo};

// ES6 命名导出可以将模块作为容器，所以可以在一个模块中声明多个命名导出。
export const foo = 'foo';
export const bar = 'bar';
export const baz = 'baz';


const foo = 'foo';
const bar = 'bar';
const baz = 'baz';
export { foo, bar as myBar, baz };
```

默认导出：

```js
const foo = 'foo';
export default foo;
// 等同于 export default foo;
export { foo as default };

// 命名导出和默认导出
const foo = 'foo';
const bar = 'bar';
export { bar };
export default foo;
```

#### 模块导入 ####

