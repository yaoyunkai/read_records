# webapck #

## get started ##

首先我们创建一个目录，初始化 npm，然后 在本地安装 webpack，接着安装 webpack-cli（此工具用于在命令行中运行 webpack）：

```console
mkdir webpack-demo
cd webpack-demo
npm init -y
npm install webpack webpack-cli --save-dev
```

现在，我们将创建以下目录结构、文件和内容：

```console
  webpack-demo
  |- package.json
+ |- index.html
+ |- /src
+   |- index.js
```

### 创建一个bundle ###

首先，我们稍微调整下目录结构，创建分发代码(`./dist`)文件夹用于存放分发代码，源代码(`./src`)文件夹仍存放源代码。

要在 `index.js` 中打包 `lodash` 依赖，我们需要在本地安装 library：

```console
npm install --save lodash
```

现在，我们将会打包所有脚本，我们必须更新 `index.html` 文件。由于现在是通过 `import` 引入 lodash，所以要将 lodash `<script>` 删除，然后修改另一个 `<script>` 标签来加载 bundle，而不是原始的 `./src` 文件：

```html
 <!DOCTYPE html>
 <html>
   <head>
     <meta charset="utf-8" />
     <title>起步</title>
-    <script src="https://unpkg.com/lodash@4.17.20"></script>
   </head>
   <body>
-    <script src="./src/index.js"></script>
+    <script src="main.js"></script>
   </body>
 </html>
```

执行 npx webpack，会将我们的脚本 src/index.js 作为 入口起点，也会生成 dist/main.js 作为 输出。

### 模块 ###

事实上，webpack 在幕后会将代码 “**转译**”，以便旧版本浏览器可以执行。如果你检查 `dist/main.js`，你可以看到 webpack 具体如何实现，这是独创精巧的设计！除了 `import` 和 `export`，webpack 还能够很好地支持多种其他模块语法，更多信息请查看 [模块 API](https://webpack.docschina.org/api/module-methods)。

### 使用一个配置文件 ###

文件名： `webpack.config.js`

现在，让我们通过新的配置文件再次执行构建：

```console
npx webpack --config webpack.config.js
```

如果 `webpack.config.js` 存在，则 `webpack` 命令将默认选择使用它。我们在这里使用 `--config` 选项只是向你表明，可以传递任何名称的配置文件。

### npm scripts ###

```json
{
  "name": "start_webpack",
  "version": "1.0.0",
  "description": "",
  "private": "true",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack --config webpack.config.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "webpack": "^5.48.0",
    "webpack-cli": "^4.7.2"
  },
  "dependencies": {
    "lodash": "^4.17.21"
  }
}
```

## 资源管理 ##

