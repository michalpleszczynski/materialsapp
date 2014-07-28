var materialsApp = angular.module('materialsApp', ['ngRoute']).
	config(function($routeProvider) {

        $routeProvider.

            when('/main', {
				controller: 'MainCtrl',
				templateUrl: getPartialUrl('home.html'),
				}).

			when('/form', {
				controller: 'FormSubcategoryCtrl',
				templateUrl: getPartialUrl('subcategory-list.html'),
				}).
			when('/form/detail/:detailId', {
				controller: 'DetailCtrl',
				templateUrl: getPartialUrl('detail.html'),
				}).

			when('/cut', {
				controller: 'CutSubcategoryCtrl',
				templateUrl: getPartialUrl('subcategory-list.html'),
				}).
		    when('/cut/detail/:detailId', {
				controller: 'DetailCtrl',
				templateUrl: getPartialUrl('detail.html'),
				}).

			when('/join', {
				controller: 'JoinSubcategoryCtrl',
				templateUrl: getPartialUrl('subcategory-list.html'),
				}).
			when('/join/detail/:detailId', {
				controller: 'DetailCtrl',
				templateUrl: getPartialUrl('detail.html'),
				}).

			when('/finish', {
				controller: 'FinishSubcategoryCtrl',
				templateUrl: getPartialUrl('subcategory-list.html'),
				}).
			when('/finish/detail/:detailId', {
				controller: 'DetailCtrl',
				templateUrl: getPartialUrl('detail.html'),
				}).

			when('/materials', {
				controller: 'MaterialCategoryCtrl',
				templateUrl: getPartialUrl('category-list.html'),
				}).
			when('/materials/:categoryId/subcategories', {
				controller: 'MaterialSubcategoryCtrl',
				templateUrl: getPartialUrl('subcategory-list.html'),
				}).
			when('/materials/detail/:detailId', {
				controller: 'DetailCtrl',
				templateUrl: getPartialUrl('detail.html'),
				}).

			otherwise({redirectTo: '/main'});
});