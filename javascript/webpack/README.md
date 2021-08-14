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

在 webpack 出现之前，前端开发人员会使用 grunt 和 gulp 等工具来处理资源，并将它们从 /src 文件夹移动到 /dist 或 /build 目录中。JavaScript 模块也遵循同样方式，但是，像 webpack 这样的工具，将动态打包所有依赖（创建所谓的 依赖图(dependency graph)）。这是极好的创举，因为现在每个模块都可以明确表述它自身的依赖，可以避免打包未使用的模块。

webpack 最出色的功能之一就是，除了引入 JavaScript，还可以通过 loader 或内置的 Asset Modules 引入任何其他类型的文件。

### settings ###

现在将index.html更改：

```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="utf-8"/>
    <title>管理资源</title>
    <!--<script src="https://unpkg.com/lodash@4.17.20"></script>-->
</head>
<body>
<!--<script src="./src/index.js"></script>-->
<script src="bundle.js"></script>
</body>
</html>
```

将 webpack.config.js 更改：

```js
const path = require('path');

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist'),
    },
};
```

### 加载CSS ###

为了在 JavaScript 模块中 import 一个 CSS 文件，你需要安装 style-loader 和 css-loader，并在 module 配置 中添加这些 loader：

```
npm install --save-dev style-loader css-loader
```

```js
 const path = require('path');

 module.exports = {
   entry: './src/index.js',
   output: {
     filename: 'bundle.js',
     path: path.resolve(__dirname, 'dist'),
   },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
 };
```

模块 loader 可以链式调用。链中的每个 loader 都将对资源进行转换。链会逆序执行。第一个 loader 将其结果（被转换后的资源）传递给下一个 loader，依此类推。最后，webpack 期望链中的最后的 loader 返回 JavaScript。

应保证 loader 的先后顺序：[`'style-loader'`](https://webpack.docschina.org/loaders/style-loader) 在前，而 [`'css-loader'`](https://webpack.docschina.org/loaders/css-loader) 在后。如果不遵守此约定，webpack 可能会抛出错误。

这使你可以在依赖于此样式的 js 文件中 `import './style.css'`。现在，在此模块执行过程中，含有 CSS 字符串的 `<style>` 标签，将被插入到 html 文件的 `<head>` 中。

### 加载image ###

在 webpack 5 中，可以使用内置的 [Asset Modules](https://webpack.docschina.org/guides/asset-modules/)，我们可以轻松地将这些内容混入我们的系统中：

```js
 const path = require('path');

 module.exports = {
   entry: './src/index.js',
   output: {
     filename: 'bundle.js',
     path: path.resolve(__dirname, 'dist'),
   },
   module: {
     rules: [
       {
         test: /\.css$/i,
         use: ['style-loader', 'css-loader'],
       },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
      },
     ],
   },
 };
```

现在，在 `import MyImage from './my-image.png'` 时，此图像将被处理并添加到 `output` 目录，*并且* `MyImage` 变量将包含该图像在处理后的最终 url。

在使用 [css-loader](https://webpack.docschina.org/loaders/css-loader) 时，如前所示，会使用类似过程处理你的 CSS 中的 `url('./my-image.png')`。loader 会识别这是一个本地文件，并将 `'./my-image.png'` 路径，替换为 `output` 目录中图像的最终路径。而 [html-loader](https://webpack.docschina.org/loaders/html-loader) 以相同的方式处理 `<img src="./my-image.png" />`。

我们向项目添加一个图像，然后看它是如何工作的，你可以使用任何你喜欢的图像：

```console
  webpack-demo
  |- package.json
  |- webpack.config.js
  |- /dist
    |- bundle.js
    |- index.html
  |- /src
   |- icon.png
    |- style.css
    |- index.js
  |- /node_modules
```

src/index.js:

```js
import _ from 'lodash';
import './style.css';
import Icon from './docschina-logo.59f03f74b3c450856c01.png';

function component() {
    const element = document.createElement('div');

    element.innerHTML = _.join(['Hello', 'webpack'], ' ');
    element.classList.add('hello');

    // 将图像添加到我们已经存在的 div 中。
    const myIcon = new Image();
    myIcon.src = Icon;
    element.appendChild(myIcon);
    return element;
}

document.body.appendChild(component());
```

在重新build之后，可以看到图片出现在文字的旁边。

### 加载数据 ###

此外，可以加载的有用资源还有数据，如 JSON 文件，CSV、TSV 和 XML。类似于 NodeJS，JSON 支持实际上是内置的，也就是说 import Data from './data.json' 默认将正常运行。要导入 CSV、TSV 和 XML，你可以使用 csv-loader 和 xml-loader。让我们处理加载这三类文件：

```
npm install --save-dev csv-loader xml-loader
```

next show `webpack.config.js`

```js
 const path = require('path');

 module.exports = {
   entry: './src/index.js',
   output: {
     filename: 'bundle.js',
     path: path.resolve(__dirname, 'dist'),
   },
   module: {
     rules: [
       {
         test: /\.css$/i,
         use: ['style-loader', 'css-loader'],
       },
       {
         test: /\.(png|svg|jpg|jpeg|gif)$/i,
         type: 'asset/resource',
       },
       {
         test: /\.(woff|woff2|eot|ttf|otf)$/i,
         type: 'asset/resource',
       },
      {
        test: /\.(csv|tsv)$/i,
        use: ['csv-loader'],
      },
      {
        test: /\.xml$/i,
        use: ['xml-loader'],
      },
     ],
   },
 };
```

#### 自定义JSON模块 parser ####

通过使用 自定义 parser 替代特定的 webpack loader，可以将任何 toml、yaml 或 json5 文件作为 JSON 模块导入。

首先安装 `toml`，`yamljs` 和 `json5` 的 packages：

```console
npm install toml yamljs json5 --save-dev
```

并在你的 webpack 中配置它们：

```js
const toml = require('toml');
const yaml = require('yamljs');
const json5 = require('json5');

      {
        test: /\.toml$/i,
        type: 'json',
        parser: {
          parse: toml.parse,
        },
      },
      {
        test: /\.yaml$/i,
        type: 'json',
        parser: {
          parse: yaml.parse,
        },
      },
      {
        test: /\.json5$/i,
        type: 'json',
        parser: {
          parse: json5.parse,
        },
      },
```

## 管理输出 ##

到目前为止，我们都是在 index.html 文件中手动引入所有资源，然而随着应用程序增长，并且一旦开始 在文件名中使用 hash 并输出 多个 bundle，如果继续手动管理 index.html 文件，就会变得困难起来。然而，通过一些插件可以使这个过程更容易管控。

### prepare ###

在project的src目录中加入新的js文件：

```console
  webpack-demo
  |- package.json
  |- webpack.config.js
  |- /dist
  |- /src
    |- index.js
   |- print.js
  |- /node_modules
```

在 index.js 中使用新的js文件：

```js
import _ from 'lodash';
import printMe from './print.js';

 function component() {
   const element = document.createElement('div');
  const btn = document.createElement('button');

   element.innerHTML = _.join(['Hello', 'webpack'], ' ');

  btn.innerHTML = 'Click me and check the console!';
  btn.onclick = printMe;

  element.appendChild(btn);

   return element;
 }

 document.body.appendChild(component());
```

还要更新 `dist/index.html` 文件，来为 webpack 分离入口做好准备：

```html
 <!DOCTYPE html>
 <html>
   <head>
     <meta charset="utf-8" />
    <title>管理输出</title>
    <script src="./print.bundle.js"></script>
   </head>
   <body>
    <script src="./index.bundle.js"></script>
   </body>
 </html>
```

然后更改webpack配置文件：

```js
const path = require('path');

module.exports = {
    entry: {
        index: './src/index.js',
        print: './src/print.js',
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'dist'),
    },
};
```

最后重新build：npm run build

### 设置 HtmlWebpackPlugin  ###

首先安装插件，并且调整 `webpack.config.js` 文件：

```
npm install --save-dev html-webpack-plugin
```

```js
 const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

 module.exports = {
   entry: {
     index: './src/index.js',
     print: './src/print.js',
   },
  plugins: [
    new HtmlWebpackPlugin({
      title: '管理输出',
    }),
  ],
   output: {
     filename: '[name].bundle.js',
     path: path.resolve(__dirname, 'dist'),
   },
 };
```

然后执行 npm run build

### 清理 dist 文件夹 ###

通常比较推荐的做法是，在每次构建前清理 /dist 文件夹，这样只会生成用到的文件。让我们使用 output.clean 配置项实现这个需求。

### manifest ###

webpack 和 webpack 插件似乎“知道”应该生成哪些文件。答案是，webpack 通过 manifest，可以追踪所有模块到输出 bundle 之间的映射。

## 开发环境 ##

在开始前，我们先将 mode 设置为 'development'，并将 title 设置为 'Development'。

```js
 const path = require('path');
 const HtmlWebpackPlugin = require('html-webpack-plugin');

 module.exports = {
  mode: 'development',
   entry: {
     index: './src/index.js',
     print: './src/print.js',
   },
   plugins: [
     new HtmlWebpackPlugin({
      title: 'Output Management',
      title: 'Development',
     }),
   ],
   output: {
     filename: '[name].bundle.js',
     path: path.resolve(__dirname, 'dist'),
     clean: true,
   },
 };
```

### 使用source map ###

在 webpack.config.js 中使用 devtool:

```js
module.exports = {
   mode: 'development',
   entry: {
     index: './src/index.js',
     print: './src/print.js',
   },
  devtool: 'inline-source-map',
```

### 选择一个开发工具 ###

webpack 提供几种可选方式，帮助你在代码发生变化后自动编译代码：

- webpack's Watch Mode
- webpack-dev-server
- webpack-dev-middleware

**使用 watch mode**

在package.json中添加命令: `webpack --watch`

该模式不能自动刷新页面。

**使用webpack-dev-server**

安装： `npm install --save-dev webpack-dev-server`

修改webpack.config.js:

```js
 module.exports = {
   mode: 'development',
   entry: {
     index: './src/index.js',
     print: './src/print.js',
   },
   devtool: 'inline-source-map',
  devServer: {
    contentBase: './dist',
  },
```

以上配置告知 `webpack-dev-server`，将 `dist` 目录下的文件 serve 到 `localhost:8080` 下。

`webpack-dev-server` 会从 `output.path` 中定义的目录为服务提供 bundle 文件，即，文件将可以通过 `http://[devServer.host]:[devServer.port]/[output.publicPath]/[output.filename]` 进行访问。

## 代码分离 ##

代码分离是 webpack 中最引人注目的特性之一。此特性能够把代码分离到不同的 bundle 中，然后可以按需加载或并行加载这些文件。代码分离可以用于获取更小的 bundle，以及控制资源加载优先级，如果使用合理，会极大影响加载时间。

常用的代码分离方法有三种：

- 入口起点：使用 [`entry`](https://webpack.docschina.org/configuration/entry-context) 配置手动地分离代码。
- 防止重复：使用 [Entry dependencies](https://webpack.docschina.org/configuration/entry-context/#dependencies) 或者 [`SplitChunksPlugin`](https://webpack.docschina.org/plugins/split-chunks-plugin) 去重和分离 chunk。
- 动态导入：通过模块的内联函数调用来分离代码。

### 入口起点 entry point ###

正如前面提到的，这种方式存在一些隐患：

- 如果入口 chunk 之间包含一些重复的模块，那些重复模块都会被引入到各个 bundle 中。
- 这种方法不够灵活，并且不能动态地将核心应用程序逻辑中的代码拆分出来。

以上两点中，第一点对我们的示例来说无疑是个问题，因为之前我们在 `./src/index.js` 中也引入过 `lodash`，这样就在两个 bundle 中造成重复引用。在下一章节会移除重复的模块。

### 防止重复 prevent duplication ###

#### 入口依赖 ####

配置 [`dependOn` option](https://webpack.docschina.org/configuration/entry-context/#dependencies) 选项，这样可以在多个 chunk 之间共享模块：

webpack.config.js:

```js
 const path = require('path');

 module.exports = {
   mode: 'development',
   entry: {
    index: {
      import: './src/index.js',
      dependOn: 'shared',
    },
    another: {
      import: './src/another-module.js',
      dependOn: 'shared',
    },
    shared: 'lodash',
   },
   output: {
     filename: '[name].bundle.js',
     path: path.resolve(__dirname, 'dist'),
   },
 };
```

如果我们要在一个 HTML 页面上使用多个入口时，还需设置 `optimization.runtimeChunk: 'single'`，否则还会遇到[这里](https://bundlers.tooling.report/code-splitting/multi-entry/)所述的麻烦。

```js
  optimization: {
    runtimeChunk: 'single',
  },
```

#### SplitChunksPlugin ####

[`SplitChunksPlugin`](https://webpack.docschina.org/plugins/split-chunks-plugin) 插件可以将公共的依赖模块提取到已有的入口 chunk 中，或者提取到一个新生成的 chunk。让我们使用这个插件，将之前的示例中重复的 `lodash` 模块去除：

```js
optimization: {
    splitChunks: {
        chunks: "all"
    }
},
```

### 动态导入 dynamic import ###

当涉及到动态代码拆分时，webpack 提供了两个类似的技术。第一种，也是推荐选择的方式是，使用符合 ECMAScript 提案 的 import() 语法 来实现动态导入。

src/index.js

```js
function getComponent() {
    return import('lodash')
        .then(({default: _}) => {
            const ele = document.createElement('div');
            ele.innerHTML = _.join(['Hello', 'webpack'], ' ');
            return ele;
        })
        .catch((error) => 'An error occurred while loading the component');
}

getComponent().then((com) => {
    document.body.appendChild(com);
})
```

我们之所以需要 `default`，是因为 webpack 4 在导入 CommonJS 模块时，将不再解析为 `module.exports` 的值，而是为 CommonJS 模块创建一个 artificial namespace 对象，

同样还可以使用async的方式来动态导入：

```js
async function getComponent() {
    const element = document.createElement('div');

    const {default: _} = await import('lodash');
    element.innerHTML = _.join(['Hello', 'webpack'], ' ');
    return element;
}
```

### 预获取/预加载 prefetch / preload module ###

### bundle分析  ###

一旦开始分离代码，一件很有帮助的事情是，分析输出结果来检查模块在何处结束。 [官方分析工具](https://github.com/webpack/analyse) 是一个不错的开始。

## 缓存 ##

此指南的重点在于通过必要的配置，以确保 webpack 编译生成的文件能够被客户端缓存，而在文件内容变化后，能够请求到新的文件。

### 输出文件的文件名 ###

配置 uouput.filename:

```js
filename: '[name].[contenthash].js',
```

### 提取引导模板 extracting boilerplate ###

正如我们在 [代码分离](https://webpack.docschina.org/guides/code-splitting) 中所学到的，[`SplitChunksPlugin`](https://webpack.docschina.org/plugins/split-chunks-plugin/) 可以用于将模块分离到单独的 bundle 中。webpack 还提供了一个优化功能，可使用 [`optimization.runtimeChunk`](https://webpack.docschina.org/configuration/optimization/#optimizationruntimechunk) 选项将 runtime 代码拆分为一个单独的 chunk。将其设置为 `single` 来为所有 chunk 创建一个 runtime bundle：

```js
optimization: {
    runtimeChunk: 'single',
},
```

将第三方库(library)（例如 `lodash` 或 `react`）提取到单独的 `vendor` chunk 文件中，是比较推荐的做法

以通过使用 [SplitChunksPlugin 示例 2](https://webpack.docschina.org/plugins/split-chunks-plugin/#split-chunks-example-2) 中演示的 [`SplitChunksPlugin`](https://webpack.docschina.org/plugins/split-chunks-plugin/) 插件的 [`cacheGroups`](https://webpack.docschina.org/plugins/split-chunks-plugin/#splitchunkscachegroups) 选项来实现。

### 模块标识符 module identifier ###

每个 [`module.id`](https://webpack.docschina.org/api/module-variables/#moduleid-commonjs) 会默认地基于解析顺序(resolve order)进行增量。也就是说，当解析顺序发生变化，ID 也会随之改变。

- `main` bundle 会随着自身的新增内容的修改，而发生变化。
- `vendor` bundle 会随着自身的 `module.id` 的变化，而发生变化。
- `manifest` runtime 会因为现在包含一个新模块的引用，而发生变化。

第一个和最后一个都是符合预期的行为，`vendor` hash 发生变化是我们要修复的。我们将 [`optimization.moduleIds`](https://webpack.docschina.org/configuration/optimization/#optimizationmoduleids) 设置为 `'deterministic'`：

```js
optimization: {
    moduleIds: 'deterministic',
}
```

## 创建 library ##

```js
const path = require('path');

module.exports = {
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'webpack-numbers.js',
        // library: 'webpackNumbers',
        library: {
            name: 'webpackNumbers',
            type: 'umd',
        },
    },
};
```

### 外部化lodash ###

我们更倾向于把 `lodash` 当作 `peerDependency`。也就是说，consumer(使用者) 应该已经安装过 `lodash` 。因此，你就可以放弃控制此外部 library ，而是将控制权让给使用 library 的 consumer。

```js
   externals: {
     lodash: {
       commonjs: 'lodash',
       commonjs2: 'lodash',
       amd: 'lodash',
       root: '_',
     },
   },
```

## 环境变量 ##

在命令行传入环境变量：

```shell
npx webpack --env goal=local --env production --progress
```

### 依赖管理 ###

> es6 modules

> commonJS

> amd

### 脚手架 ###

#### 创建脚手架 ####

在编写 `webpack-cli` 脚手架之前，请先考虑下要实现的目标和要使用的群体：

- 是否需要实现一个可被多种应用程序和项目使用的通用脚手架？
- 是否需要脚手架支持特定内容，例如同时编写 webpack.config.js 和框架代码的脚手架？
- 谁是潜在的用户，脚手架用户将会有什么样的用户体验？

