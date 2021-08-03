# Node.js #

## Getting started ##

### 命令行运行 ###

```bash
node app.js
```

### 如何退出一个Node.js程序 ###

模块 process 提供了 `process.exit()` 方法退出运行。

```js
const express = require('express')

const app = express()

app.get('/', (req, res) => {
  res.send('Hi!')
})

const server = app.listen(3000, () => console.log('Server ready'))

process.on('SIGTERM', () => {
  server.close(() => {
    console.log('Process terminated')
  })
})
```

### 如何从Node.js读取环境变量 ###

> Note: process does not require a "require", it's automatically available.

process.env 中获取环境变量。

### Node.js REPL ###

node.js 的命令行模式

### Node.js 访问命令行参数 ###

process.argv

### 命令行输出 ###

console 模块

### 使用导出从Node.js文件中公开功能 ###

Node.js有一个内置的模块系统。

A Node.js file can import functionality exposed by other Node.js files.

When you want to import something you use

```js
const library = require('./library')
```

在此文件中，功能必须在其他文件导入之前公开。

默认情况下，文件中定义的任何其他对象或变量都是私有的，不对外公开。

JavaScript模块的管理：

- require
- exports

### npm introduce ###

**安装所有的依赖**

`npm install`

**安装单个package**

`npm install <package-name>`

- `--save-dev` 安装该条目并将其添加到包中。json文件devDependencies
- `--no-save` 安装但不将条目添加到包中。json文件的依赖关系

devDependencies和dependencies之间的区别在于前者包含开发工具，比如测试库，而后者是与生产中的应用绑定在一起的。

**更新包**

`npm update`

`npm update <package-name>`

**Running Tasks**

package.json 支持指定命令行任务的格式，可以使用:

`npm run <task-name>`

```json
{
  "scripts": {
    "start-dev": "node lib/server-development",
    "start": "node lib/server-production",
    "watch": "webpack --watch --progress --colors --config webpack.conf.js",
    "dev": "webpack --progress --colors --config webpack.conf.js",
    "prod": "NODE_ENV=production webpack -p --config webpack.conf.js",
  }
}
```

### npm 包安装的位置 ###

- `-g` 选项是全局开关

### 使用或者执行一个包 ###

对于可执行的包，it will put the executable file under the `node_modules/.bin/` folder.

可以执行的命令行。

### package.json ###

The `package.json` file is kind of a manifest for your project. It can do a lot of things, completely unrelated. It's a central repository of configuration for tools, for example. It's also where `npm` and `yarn` store the names and versions for all the installed packages.

- name: 它告诉应用程序或包的名称，它包含在这个文件所在的文件夹中。
- version: indicates the current version
- description
- main: set the entry point for the application
- private: if set to `true` prevents the app/package to be accidentally published on `npm`
- scripts: defines a set of node scripts you can run
- dependencies:
- devDependencies:
- engines: 设置该包/应用在哪个版本的Node.js上工作
- browserslist: 告诉您想要支持的浏览器(及其版本)
- author: 
- contributors:
- bugs:
- homepage
- license
- keywords
- repository

### package-lock.json ###

包锁的目标。Json文件是为了跟踪每个安装包的确切版本，以便即使包由其维护者更新，产品也能以相同的方式100%复制。

using the **semver** notation

- `~0.13.0`
- `^0.13.0`
- `0.13.0`

### 找到已安装的npm包版本 ###

`npm list` 

`npm list -g` 

`npm list --depth=0`

`npm install <package>@<version>`

`npm view <package> versions` 查看所有可以安装的版本。

### Semantic Versioning ###

