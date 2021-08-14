# Maven Usage

## Get Started ##

### show version ###

`mvn --version`

```console
Apache Maven 3.6.3 (cecedd343002696d0abb50b32b541b8a6ba2883f)
Maven home: D:\Program Files\JetBrains\IntelliJ IDEA 2021.1.3\plugins\maven\lib\maven3
Java version: 11.0.9, vendor: Oracle Corporation, runtime: D:\Program Files\Java\jdk-11.0.9
Default locale: zh_CN, platform encoding: UTF-8
OS name: "windows 10", version: "10.0", arch: "amd64", family: "windows"
```

### Running Maven Tools ###

Although hardly a comprehensive list, these are the most common *default* lifecycle phases executed.

- **validate**: validate the project is correct and all necessary information is available
- **compile**: compile the source code of the project
- **test**: test the compiled source code using a suitable unit testing framework. These tests should not require the code be packaged or deployed
- **package**: take the compiled code and package it in its distributable format, such as a JAR.
- **integration-test**: process and deploy the package if necessary into an environment where integration tests can be run
- **verify**: run any checks to verify the package is valid and meets quality criteria
- **install**: install the package into the local repository, for use as a dependency in other projects locally
- **deploy**: done in an integration or release environment, copies the final package to the remote repository for sharing with other developers and projects.

There are two other Maven lifecycles of note beyond the *default* list above. They are

- **clean**: cleans up artifacts created by prior builds

- **site**: generates site documentation for this project

### pom.xml ###

编译源文件： `mvn compile`

编译测试源文件和执行单元测试： `mvn test`

编译测试源文件但不执行： `mvn test-compile`

将编译之后的JAR安装到本地： `mvn install`

生成站点： `mvn site`

### use plugins ###

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-compiler-plugin</artifactId>
      <version>3.3</version>
      <configuration>
        <source>1.5</source>
        <target>1.5</target>
      </configuration>
    </plugin>
  </plugins>
</build>
```

### filter resource files ###

```xml
<build>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <filtering>true</filtering>
        </resource>
    </resources>
</build>
```

为了让resources文件能引用pom.xml文件中的属性，需要如上设置，然后可以使用：

```properties
application.name=${project.name}
application.version=${project.version}
```

有了它，你可以执行下面的命令(process-resources是构建生命周期阶段，在这里复制和过滤资源):

```shell
mvn process-resources
```

**提供属性的几种方式**

maven 还支持在pom.xml 引入外部属性，在resources目录创建 src/main/filters/filter.properties：

```properties
# filter.properties
my.filter.value=hello!
```

```xml
<build>
    <filters>
        <filter>src/main/filters/filter.properties</filter>
    </filters>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <filtering>true</filtering>
        </resource>
    </resources>
</build>

<properties>
    <maven.compiler.source>11</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
    <!--        <maven.compiler.release>11</maven.compiler.release>-->
    <demo.message>Hello.</demo.message>
</properties>
```

在props中：

```properties
message=${my.filter.value}
```

**还可以在命令行提供**

```shell
mvn process-resources "-Dcommand.line.prop=hello again"
```

```properties
# application.properties
java.version=${java.version}
command.line.prop=${command.line.prop}
```

### use external dependencies ###

......

### 我如何一次构建多个项目? ###

add a parent  `pom.xml`

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>com.mycompany.app</groupId>
  <artifactId>app</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>pom</packaging>
 
  <modules>
    <module>my-app</module>
    <module>my-webapp</module>
  </modules>
</project>
```

We'll need a dependency on the JAR from the webapp, so add this to `my-webapp/pom.xml`:

```xml
<dependencies>
    <dependency>
        <groupId>com.mycompany.app</groupId>
        <artifactId>my-app</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
</dependencies>
```

Finally, add the following `<parent>` element to both of the other `pom.xml` files in the subdirectories:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <parent>
    <groupId>com.mycompany.app</groupId>
    <artifactId>app</artifactId>
    <version>1.0-SNAPSHOT</version>
  </parent>
</project>
```

然后进行验证： `mvn verify`

## Build lifecycle ##

#### 1. 基础 ####

三个内置的lifecycle： default clean site

其中 default 的生命周期如下：

validate compile test package verify install deploy

这些生命周期阶段(加上这里没有显示的其他生命周期阶段)依次执行，以完成默认的生命周期。

**build phase由Plugin Goal组成**

尽管一个phase负责lifecycle的一个阶段，但执行这些阶段的方式可能会不同，这是通过把plugin goals绑定到phase上完成的。
一个goal代表着用于构建和管理一个项目的一个特定任务（比phase粒度要细）。

**设置项目使用的Build Lifecycle**

build lifecycle使用起来很简单，但在maven项目构建时，我们怎么给每个phase指定任务呢？

①第一种方式：通过packaging元素设置项目的打包方式来指定任务，maven支持的打包方式有：jar, war, ear 和 pom。如果不指定，默认为jar。

例如，jar的打包方式会绑定下面的goal到default lifecycle的phase上：

| Phase                    | plugin:goal               |
| :----------------------- | :------------------------ |
| `process-resources`      | `resources:resources`     |
| `compile`                | `compiler:compile`        |
| `process-test-resources` | `resources:testResources` |
| `test-compile`           | `compiler:testCompile`    |
| `test`                   | `surefire:test`           |
| `package`                | `jar:jar`                 |
| `install`                | `install:install`         |
| `deploy`                 | `deploy:deploy`           |

② 第二种方式： add goals to phases is to configure plugins in your project.

```xml
 <plugin>
   <groupId>org.codehaus.modello</groupId>
   <artifactId>modello-maven-plugin</artifactId>
   <version>1.8.1</version>
   <executions>
     <execution>
       <configuration>
         <models>
           <model>src/main/mdo/maven.mdo</model>
         </models>
         <version>4.0.0</version>
       </configuration>
       <goals>
         <goal>java</goal>
       </goals>
     </execution>
   </executions>
 </plugin>
```

## The POM ##

项目对象模型或POM是Maven中的基本工作单元.

它是一个XML文件，包含Maven用于构建项目的项目信息和配置细节。它包含大多数项目的默认值。

### Super POM ###

Super POM是Maven的默认POM。除非显式设置，否则所有POM都会扩展Super POM，这意味着Super POM中指定的配置将由您为项目创建的POM继承。

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
 
  <repositories>
    <repository>
      <id>central</id>
      <name>Central Repository</name>
      <url>https://repo.maven.apache.org/maven2</url>
      <layout>default</layout>
      <snapshots>
        <enabled>false</enabled>
      </snapshots>
    </repository>
  </repositories>
 
  <pluginRepositories>
    <pluginRepository>
      <id>central</id>
      <name>Central Repository</name>
      <url>https://repo.maven.apache.org/maven2</url>
      <layout>default</layout>
      <snapshots>
        <enabled>false</enabled>
      </snapshots>
      <releases>
        <updatePolicy>never</updatePolicy>
      </releases>
    </pluginRepository>
  </pluginRepositories>
 
  <build>
    <directory>${project.basedir}/target</directory>
    <outputDirectory>${project.build.directory}/classes</outputDirectory>
    <finalName>${project.artifactId}-${project.version}</finalName>
    <testOutputDirectory>${project.build.directory}/test-classes</testOutputDirectory>
    <sourceDirectory>${project.basedir}/src/main/java</sourceDirectory>
    <scriptSourceDirectory>${project.basedir}/src/main/scripts</scriptSourceDirectory>
    <testSourceDirectory>${project.basedir}/src/test/java</testSourceDirectory>
    <resources>
      <resource>
        <directory>${project.basedir}/src/main/resources</directory>
      </resource>
    </resources>
    <testResources>
      <testResource>
        <directory>${project.basedir}/src/test/resources</directory>
      </testResource>
    </testResources>
    <pluginManagement>
      <!-- NOTE: These plugins will be removed from future versions of the super POM -->
      <!-- They are kept for the moment as they are very unlikely to conflict with lifecycle mappings (MNG-4453) -->
      <plugins>
        <plugin>
          <artifactId>maven-antrun-plugin</artifactId>
          <version>1.3</version>
        </plugin>
        <plugin>
          <artifactId>maven-assembly-plugin</artifactId>
          <version>2.2-beta-5</version>
        </plugin>
        <plugin>
          <artifactId>maven-dependency-plugin</artifactId>
          <version>2.8</version>
        </plugin>
        <plugin>
          <artifactId>maven-release-plugin</artifactId>
          <version>2.5.3</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>
 
  <reporting>
    <outputDirectory>${project.build.directory}/site</outputDirectory>
  </reporting>
 
  <profiles>
    <!-- NOTE: The release profile will be removed from future versions of the super POM -->
    <profile>
      <id>release-profile</id>
 
      <activation>
        <property>
          <name>performRelease</name>
          <value>true</value>
        </property>
      </activation>
 
      <build>
        <plugins>
          <plugin>
            <inherited>true</inherited>
            <artifactId>maven-source-plugin</artifactId>
            <executions>
              <execution>
                <id>attach-sources</id>
                <goals>
                  <goal>jar-no-fork</goal>
                </goals>
              </execution>
            </executions>
          </plugin>
          <plugin>
            <inherited>true</inherited>
            <artifactId>maven-javadoc-plugin</artifactId>
            <executions>
              <execution>
                <id>attach-javadocs</id>
                <goals>
                  <goal>jar</goal>
                </goals>
              </execution>
            </executions>
          </plugin>
          <plugin>
            <inherited>true</inherited>
            <artifactId>maven-deploy-plugin</artifactId>
            <configuration>
              <updateReleaseInfo>true</updateReleaseInfo>
            </configuration>
          </plugin>
        </plugins>
      </build>
    </profile>
  </profiles>
 
</project>
```

### Minimal POM ###

- `project` root
- `modelVersion` - should be set to 4.0.0
- `groupId` - the id of the project's group.
- `artifactId` - the id of the artifact (project)
- `version` - the version of the artifact under the specified group

### Project 继承 ###

POM中被合并的元素如下:

- dependencies
- developers and contributors
- plugin lists (including reports)
- plugin executions with matching ids
- plugin configuration
- resources

**A demo:**

module POM:

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
 
  <parent>
    <groupId>com.mycompany.app</groupId>
    <artifactId>my-app</artifactId>
    <version>1</version>
  </parent>
 
  <groupId>com.mycompany.app</groupId>
  <artifactId>my-module</artifactId>
  <version>1</version>
</project>
```

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
 
  <parent>
    <groupId>com.mycompany.app</groupId>
    <artifactId>my-app</artifactId>
    <version>1</version>
  </parent>
 
  <artifactId>my-module</artifactId>
</project>
```

但是，如果父项目已经安装在我们的本地存储库中，或者在那个特定的目录结构中(父项目pomo .xml比模块的pomo .xml高一个目录)，那么这个方法是可行的。

但是，如果父目录还没有安装，并且目录结构如下例所示，该怎么办呢?

```console
.
 |-- my-module
 |   `-- pom.xml
 `-- parent
     `-- pom.xml
```

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
 
  <parent>
    <groupId>com.mycompany.app</groupId>
    <artifactId>my-app</artifactId>
    <version>1</version>
    <relativePath>../parent/pom.xml</relativePath>
  </parent>
 
  <artifactId>my-module</artifactId>
</project>
```

### Project Aggregation ###

但是它不是指定来自模块的父POM，而是指定来自父POM的模块。

通过这样做，父项目现在知道了它的模块，如果对父项目调用Maven命令，那么该Maven命令也将被执行到父项目的模块。要进行项目聚合，您必须执行以下操作:

- Change the parent POMs packaging to the value "pom".
- Specify in the parent POM the directories of its modules (children POMs).

**For Parent:**

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>com.mycompany.app</groupId>
  <artifactId>my-app</artifactId>
  <version>1</version>
  <packaging>pom</packaging>
 
  <modules>
    <module>my-module</module>
  </modules>
</project>
```

## Build Profiles ##

### profile有哪些不同类型?每个定义在哪里? ###

Per Project
- Defined in the POM itself (`pom.xml`).

Per User
- Defined in the Maven-settings (`%USER_HOME%/.m2/settings.xml`).

Global
- Defined in the global Maven-settings (`${maven.home}/conf/settings.xml`).

Profile descriptor
- a descriptor located in project basedir (`profiles.xml`) (no longer supported in Maven 3.0 and above; see Maven 3 compatibility notes)

### 如何触发配置文件?根据使用的概要文件的类型，这是如何变化的? ###

配置文件可以通过以下几种方式激活:

- From the command line
- Through Maven settings
- Based on environment variables
- OS settings
- Present or missing files

1，通过命令行参数激活：

```console
mvn clean package -Ptest
```

2，通过pom文件里的activation属性：

```xml
<profile>
    <id>prod</id>
    <properties>
        <profiles.active>prod</profiles.active>
    </properties>
    <!--activation用来指定激活方式，可以根据jdk环境，环境变量，文件的存在或缺失-->
    <activation>
        <!--配置默认激活-->
        <activeByDefault>true</activeByDefault>

        <!--通过jdk版本-->
        <!--当jdk环境版本为1.5时，此profile被激活-->
        <jdk>1.5</jdk>
        <!--当jdk环境版本1.5或以上时，此profile被激活-->
        <jdk>[1.5,)</jdk>

        <!--根据当前操作系统-->
        <os>
            <name>Windows XP</name>
            <family>Windows</family>
            <arch>x86</arch>
            <version>5.1.2600</version>
        </os>

        <!--通过系统环境变量，name-value自定义-->
        <property>
            <name>env</name>
            <value>test</value>
        </property>

        <!--通过文件的存在或缺失-->
        <file>
            <missing>target/generated-sources/axistools/wsdl2java/
                com/companyname/group</missing>
            <exists/>
        </file>
    </activation>
</profile>
```

3，settings.xml 中使用 activeProfiles指定

```xml
<activeProfiles>  
     <activeProfile>profileTest1</activeProfile>  
</activeProfiles>  
```

**失活一个profile**

```shell
mvn groupId:artifactId:goal -P !profile-1,!profile-2,!?profile-3
```

### pom可以被profile配置的areas ###

- <repositories>
- <pluginRepositories>
- <dependencies>
- <plugins>
- <properties> (not actually available in the main POM, but used behind the scenes)
- <modules>
- <reports>
- <reporting>
- <dependencyManagement>
- <distributionManagement>
- a subset of the <build> element, which consists of:
  - <defaultGoal>
  - <resources>
  - <testResources>
  - <directory>
  - <finalName>
  - <filters>
  - <pluginManagement>
  - <plugins>

来自活动概要文件的POM中的所有概要文件元素将覆盖与POM同名的全局元素，或者在集合的情况下扩展这些全局元素。如果在同一个POM或外部文件中有多个激活的概要文件，那么后面定义的将优先于前面定义的概要文件(与它们的概要文件id和激活顺序无关)。

**我如何知道在构建期间哪些概要文件是有效的?**

```console
mvn help:active-profiles
mvn help:active-profiles -Denv=dev // properites
mvn help:active-profiles -P appserverConfig-dev  // profiles
```

## Dependency Mechanism ##

### 传递依赖 ###

Maven通过自动包含传递依赖项，避免了发现和指定您自己的依赖项所需的库的需要。

可以从多少级别收集依赖项是没有限制的。只有在发现循环依赖项时才会出现问题。

通过传递依赖关系，包含的库的图可以迅速增长到相当大的规模。出于这个原因，有一些额外的特性来限制包含哪些依赖项:

- **Dependency mediation** 这将决定当遇到多个版本作为依赖项时，将选择工件的哪个版本。Maven选择“最接近的定义”。

  ```console
    A
    ├── B
    │   └── C
    │       └── D 2.0
    └── E
        └── D 1.0
  
  // 可以在A中定义个D
    A
    ├── B
    │   └── C
    │       └── D 2.0
    ├── E
    │   └── D 1.0
    │
    └── D 2.0      
  ```

- **Dependency management** 在前面的示例中部分依赖直接添加到即使它是不能直接使用的a .相反,可以包括D作为依赖dependencyManagement部分和直接控制哪个版本的D时使用,或者是引用。

- **Dependency scope** 这允许您只包含适合当前构建阶段的依赖项。

- **Excluded dependencies** 如果项目X依赖于项目Y，而项目Y依赖于项目Z，那么项目X的所有者可以使用“exclude”元素显式地将项目Z排除为依赖项。

- **Optional dependencies** 如果项目Y依赖于项目Z，项目Y的所有者可以使用“optional”元素将项目Z标记为可选依赖项。

尽管传递依赖关系可以隐式地包含所需的依赖关系，但最好还是显式地指定源代码直接使用的依赖关系

了解依赖关系：`mvn dependency:tree`

分析依赖关系： `mvn dependency:analyze`

### Dependency Scope ###

- **compile** : 编译依赖项在项目的所有类路径中都可用。
- **provided**: 具有此作用域的依赖项被添加到用于编译和测试的类路径，而不是运行时类路径。它不是传递性的。
- **runtime**: Maven在运行时和测试类路径中包含此作用域的依赖项，但不在编译类路径中。
- **test**: 
- **system**
- **import**

## Repositories ##

两种类型：local & remote

### using repositories ###

```xml
<project>
...
  <repositories>
    <repository>
      <id>my-repo1</id>
      <name>your custom repo</name>
      <url>http://jarsm2.dyndns.dk</url>
    </repository>
    <repository>
      <id>my-repo2</id>
      <name>your custom repo</name>
      <url>http://jarsm2.dyndns.dk</url>
    </repository>
  </repositories>
...
</project>
```

```xml
<settings>
  ...
  <mirrors>
    <mirror>
      <id>other-mirror</id>
      <name>Other Mirror Repository</name>
      <url>https://other-mirror.repo.other-company.com/maven2</url>
      <mirrorOf>central</mirrorOf>
    </mirror>
  </mirrors>
  ...
</settings>
```

离线使用： `mvn -o pakcage`

