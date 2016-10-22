'use strict';   // See note about 'use strict'; below

var app = angular.module('app', [
    'ngMaterial', 'ui.router'
]);

app.config(function($stateProvider, $urlRouterProvider, $mdThemingProvider) {
        $mdThemingProvider.theme('customTheme')
                  .primaryPalette('blue-grey')
                  .accentPalette('orange')
                  .warnPalette('red');
        $urlRouterProvider.otherwise('/tab/dash');
        $stateProvider
        .state('containers', {
            url: "/containers",
            templateUrl: "/static/partials/404.html"
        })
        .state('images', {
            url: "/images",
            templateUrl: "/static/partials/images.html"
        });
    })
