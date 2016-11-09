var app = angular.module('elantix', ['ngComponentRouter']);


app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.value('$routerRootComponent', 'catApp');

function getPersons($http) {
    return $http.get('api/v1/some/').then(function (response) {
        return response.data;
    });
}

function getsPersons($http, data) {
    return $http.get('api/v1/some/?word=' + data).then(function (response) {
        return response.data;
    });
}

function controllerPersons($http) {
    var self = this;

    self.$onInit = function () {
        getPersons($http).then(function (persones) {
            self.persons = persones;
            self.numPersons = self.persons.length
        })
    };

    self.sort = function (data) {
        self.rev = !self.rev;
        self.sortBy = data
    };
    
    self.submits = function (valid) {
        if (valid) {
            getsPersons($http, self.searchName).then(function (persones) {
                self.persons = persones;
                self.searchNumPersons = self.persons.length;
            })
        }
    };
    
    self.clear = function () {
        if (self.searchNumPersons < self.numPersons) {
            getPersons($http).then(function (persones) {
                self.persons = persones;
                self.searchNumPersons = self.numPersons;
                self.searchName = ''
            })
        }
    }
}

app.component('personsComponent', {
    templateUrl: 'static/app/views/persons.html',
    controllerAs: 'persons',
    controller: ['$http', controllerPersons]
});

app.component('catApp', {
    templateUrl: 'static/app/views/cat.html',
    $routeConfig: [
        {path: '/persons', component: 'personsComponent', name: 'Persons'},
        {path: '/**', redirectTo: ['Persons']}
    ]
});