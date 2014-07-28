materialsApp.controller('MainCtrl', function($scope){

});

materialsApp.controller('FormSubcategoryCtrl', function($scope, ApiService){
    $scope.subcategories = [];

    ApiService.getSubcategories('form').then(function(data){
        $scope.subcategories = data.subcategories;
    });
});

materialsApp.controller('CutSubcategoryCtrl', function($scope, ApiService){
    $scope.subcategories = [];

    ApiService.getSubcategories('cut').then(function(data){
        $scope.subcategories = data.subcategories;
    });
});

materialsApp.controller('JoinSubcategoryCtrl', function($scope, ApiService){
    $scope.subcategories = [];

    ApiService.getSubcategories('join').then(function(data){
        $scope.subcategories = data.subcategories;
    });
});

materialsApp.controller('FinishSubcategoryCtrl', function($scope, ApiService){
    $scope.subcategories = [];

    ApiService.getSubcategories('finish').then(function(data){
        $scope.subcategories = data.subcategories;
    });
});

materialsApp.controller('MaterialCategoryCtrl', function($scope, ApiService){
    $scope.categories = [];

    ApiService.getCategories('materials').then(function(data){
        $scope.categories = data.categories;
    });
});

materialsApp.controller('MaterialSubcategoryCtrl', function($scope, $routeParams, ApiService){
    $scope.subcategories = [];

    ApiService.getSubcategories('materials', $routeParams.categoryId).then(function(data){
        $scope.subcategories = data.subcategories;
    });

});

materialsApp.controller('DetailCtrl', function($scope, $routeParams, ApiService){
    $scope.detail = {};

    ApiService.getDetail($routeParams.detailId).then(function(data){
        $scope.detail = data;
    });
});