const path = require('path')
const pkgJson = require('./package.json')

module.exports = function (grunt) {
  require('load-grunt-tasks')(grunt)

  grunt.registerTask('pre-build', ['check-synced-version-numbers'])

  grunt.registerTask('check-synced-version-numbers', () => {
    const packageJsonVersion = pkgJson.version

    const pyProjectToml = path.join(__dirname, 'pyproject.toml')
    if (!grunt.file.exists(pyProjectToml)) {
      grunt.log.error('file ' + pyProjectToml + ' not found')
      return false // abort
    }
    const pyProjectTomlFile = grunt.file.read(pyProjectToml)

    const { version } = /version\s*=\s*"(?<version>.*)"/.exec(
      pyProjectTomlFile
    ).groups

    if (packageJsonVersion !== version) {
      grunt.log.error(
        `package.json version ("${packageJsonVersion}") differs from pyproject.toml version ("${version}")`
      )
      return false // abort
    }
  })

  grunt.registerTask('post-build', ['process-licenses', 'create-umd-folder'])

  grunt.registerTask('process-licenses', () => {
    const licensesJson = path.join(
      __dirname,
      'yfiles_jupyter_graphs',
      'labextension',
      'static',
      'third-party-licenses.json'
    )

    if (!grunt.file.exists(licensesJson)) {
      grunt.log.error('file ' + licensesJson + ' not found')
      return false // abort
    }

    const project = grunt.file.readJSON(licensesJson)

    const packages = project['packages']
    // remove (empty) yfiles entry from the licenses.json
    project['packages'] = packages.filter((p) => p.name !== 'yfiles')

    grunt.file.write(licensesJson, JSON.stringify(project, null, 2))
  })

  grunt.registerTask('create-umd-folder', () => {
    const umdPath = './umd/'
    const buildOutputPath = path.join(
      __dirname,
      'yfiles_jupyter_graphs',
      'nbextension'
    )
    const cleanExcludes = ['README.md']

    // clean output folder
    grunt.file.recurse(umdPath, (abspath, rootdir, subdir, filename) => {
      if (!cleanExcludes.includes(filename)) {
        grunt.file.delete(abspath)
      }
    })

    // write build output to umd
    const copyExcludes = ['extension.js']

    grunt.file.copy(buildOutputPath, path.join(umdPath, 'dist'), {
      process: (content, src, dest) => {
        if (src.endsWith('map')) {
          // don't copy the file
          return false
        }

        for (let exclude of copyExcludes) {
          if (src.endsWith(exclude)) {
            return false
          }
        }

        return content
      },
    })

    // copy license file
    grunt.file.copy('./LICENSE.md', path.join(umdPath, 'LICENSE.md'))

    // write package.json
    const packageJsonPath = path.join(__dirname, 'package.json')
    if (!grunt.file.exists(packageJsonPath)) {
      grunt.log.error('file ' + packageJsonPath + ' not found')
      return false // abort
    }

    const packageJson = grunt.file.readJSON(packageJsonPath)
    const newPackage = {
      name: packageJson.name,
      version: packageJson.version,
      description: packageJson.description,
      keywords: packageJson.keywords,
      homepage: packageJson.homepage,
      bugs: packageJson.bugs,
      license: 'SEE LICENSE.md',
      author: packageJson.author,
      main: 'dist/index.js',
      repository: packageJson.repository,
    }

    grunt.file.write(
      path.join(umdPath, 'package.json'),
      JSON.stringify(newPackage, null, 2)
    )
  })
}
