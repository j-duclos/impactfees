// Include gulp
let gulp = require('gulp');

// Include plugins
let sass = require('gulp-sass');
let autoprefixer = require('gulp-autoprefixer');
let babel = require('gulp-babel');
let concat = require('gulp-concat');
let sourcemaps = require('gulp-sourcemaps');
let notify = require('gulp-notify');
let jshint = require('gulp-jshint');
let uglifyjs = require('gulp-uglify');
let uglifycss = require('gulp-uglifycss');

// Compile Sass, run autoprefixer, and create sourcemaps
function cotbootstrapstyle() {
  return (
    gulp.src("sass/**/*.scss")
      .pipe(sourcemaps.init())
      .pipe(sass().on("error", notify.onError("Error: <%= error.message %>")))
      .pipe(autoprefixer({        
        cascade: false
      }))
      .pipe(sourcemaps.write())
      .pipe(uglifycss({
        "maxLineLen": 0,
        "uglyComments": true
      }))
      .pipe(gulp.dest('css'))
      .pipe(notify({ message: 'sass task complete' }))
  );
}

function cotlint() {
  return (
    gulp.src('js/es6/*.js')
      .pipe(jshint('.jshintrc'))
      .pipe(sourcemaps.init())
      .pipe(jshint.reporter('default'))
  );
}

function cotconcat() {
  return (
    gulp.src('js/es6/*.js')
      .pipe(concat('concat.js'))
      .pipe(gulp.dest('js/concat/'))
  );
}

function cotbabel() {
  return (
    gulp.src('js/concat/*.js')
      .pipe(babel({
        presets: ['@babel/env']
      }))
      .pipe(concat('javascript.js'))
      .pipe(sourcemaps.write('.'))
      .pipe(uglifyjs())
      .pipe(gulp.dest('js'))
      .pipe(notify({ message: 'JS Parsing Complete' }))
  );
}

function copybootstrapjs() {
  return (
    gulp.src('node_modules/bootstrap/dist/js/bootstrap.min.js')
      .pipe(gulp.dest('js/vendor'))
  );
}

function copybootstrapmap() {
  return (
    gulp.src('node_modules/bootstrap/dist/js/bootstrap.min.js.map')
      .pipe(gulp.dest('js/vendor'))
  );
}

function copypopperjs() {
  return (
    gulp.src('node_modules/@popperjs/core/dist/umd/popper.min.js')
      .pipe(gulp.dest('js/vendor'))
  );
}

function copypoppermap() {
  return (
    gulp.src('node_modules/@popperjs/core/dist/umd/popper.min.js.map')
      .pipe(gulp.dest('js/vendor'))
  );
}

function copyjqueryjs() {
  return (
    gulp.src('node_modules/jquery/dist/jquery.min.js')
      .pipe(gulp.dest('js/vendor'))
  );
}

function copyjquerymap() {
  return (
    gulp.src('node_modules/jquery/dist/jquery.min.map')
      .pipe(gulp.dest('js/vendor'))
  );
}

function watch(){
  gulp.watch('sass/**/*.scss', cotbootstrapstyle);
  gulp.watch('js/es6/*.js', cotlint);
  gulp.watch('js/es6/*.js', cotconcat);
  gulp.watch('js/concat/*.js', cotbabel);
  gulp.watch('sass/**/*.scss', copyjqueryjs);
  gulp.watch('sass/**/*.scss', copypopperjs);
  gulp.watch('sass/**/*.scss', copybootstrapjs);
  gulp.watch('sass/**/*.scss', copyjquerymap);
  gulp.watch('sass/**/*.scss', copypoppermap);
  gulp.watch('sass/**/*.scss', copybootstrapmap);
}

exports.watch = watch;
exports.default = watch;